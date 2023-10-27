import numpy as np
import torch
from pyro.distributions import Independent
from torch.distributions import (
    MultivariateNormal,
    MixtureSameFamily,
    Categorical,
    Normal,
    Distribution,
)

from torch_mist.distributions.joint import JointDistribution


class MultivariateCorrelatedNormalMixture(JointDistribution):
    def __init__(
        self,
        rho: float = 0.95,
        sigma: float = 0.1,
        epsilon: float = 0.15,
        delta: float = 1.5,
        n_dim: int = 5,
        n_mi_samples: int = 100000
    ):

        self.n_dim = n_dim
        self.rho = rho
        self.sigma = sigma
        self.epsilon = epsilon
        self.delta = delta
        self.n_mi_samples = n_mi_samples

        covariance = torch.eye(2)
        covariance[0, 1] = covariance[1, 0] = rho
        covariance = covariance * sigma

        mu = torch.zeros(n_dim, 4, 2)

        mu[:, 0, 0] = epsilon + delta
        mu[:, 0, 1] = -epsilon + delta
        mu[:, 1, 0] = -epsilon - delta
        mu[:, 1, 1] = epsilon - delta
        mu[:, 2, 0] = epsilon - delta
        mu[:, 2, 1] = -epsilon - delta
        mu[:, 3, 0] = -epsilon + delta
        mu[:, 3, 1] = epsilon + delta

        self.x_component_dist = Normal(mu[:, :, 0], sigma**0.5)

        # Store the marginal distribution for one dimension
        self.p_X = Independent(
            MixtureSameFamily(
                Categorical(logits=torch.zeros(n_dim, 4)),
                self.x_component_dist,
            ),
            1,
        )

        self.component_dist = MultivariateNormal(
            mu, covariance.unsqueeze(0).unsqueeze(1)
        )

        p_XY = Independent(
            MixtureSameFamily(
                Categorical(logits=torch.zeros(n_dim, 4)),
                self.component_dist,
            ),
            1,
        )

        self._cached_mi = None

        super().__init__(
            joint_dist=p_XY, dims=[1, 1], support=["x", "y"], squeeze=True
        )

    def _marginal(self, label: str) -> Distribution:
        return self.p_X

    def _approximate_mutual_information(self) -> float:
        if self.n_dim > 1:
            p_XY = MultivariateCorrelatedNormalMixture(
                n_dim=1,
                rho=self.rho,
                delta=self.delta,
                sigma=self.sigma,
                epsilon=self.epsilon
            )
        else:
            p_XY = self

        p_X = p_XY.marginal('x')

        estimates = []

        for i in range(100):
            # Sample from the joint
            samples = p_XY.sample([self.n_mi_samples])

            # Compute the log-probability of each sample pair
            log_p_xy = p_XY.log_prob(**samples)

            # And the marginal log-probability
            log_p_x = p_X.log_prob(samples['x'])

            # MC estimation of the joint and marginal entropies
            entropy_xy = -torch.mean(log_p_xy)
            entropy_x = -torch.mean(log_p_x)
            entropy_y = entropy_x

            # I(x;y) = H(x) + H(y) - H(x,y)
            mutual_information = entropy_x + entropy_y - entropy_xy

            estimates.append(mutual_information)

        estimated_mi = np.mean(estimates) * self.n_dim
        mi_std = np.std(estimates) * self.n_dim
        rounding = -int(np.log10(mi_std))
        return np.round(estimated_mi, rounding)

    def _mutual_information(self, label_1: str, label_2: str) -> float:
        if self._cached_mi is None:
            self._cached_mi = self._approximate_mutual_information()

        return self._cached_mi
