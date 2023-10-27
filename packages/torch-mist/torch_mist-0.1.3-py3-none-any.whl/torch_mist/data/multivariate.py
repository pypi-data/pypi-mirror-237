import torch
from torch.distributions import MultivariateNormal, Normal, Independent, Distribution

from torch_mist.distributions.joint import JointDistribution


class JointMultivariateNormal(JointDistribution):
    def __init__(
            self,
            n_dim: int,
            rho: float = 0.9,
            sigma: float = 1,
            device: torch.device = torch.device('cpu')
    ):
        loc = torch.zeros(n_dim, 2).to(device)
        covariance = torch.eye(2).to(device)
        covariance[0, 1] = covariance[1, 0] = rho
        covariance = covariance * sigma
        covariance = covariance.unsqueeze(0).repeat(n_dim, 1, 1)

        p_XY = Independent(
            MultivariateNormal(
                loc,
                covariance
            ), 1
        )

        self.p_X = Independent(
            Normal(
                torch.zeros(n_dim).to(device),
                sigma
            ), 1
        )

        super().__init__(joint_dist=p_XY, dims=[1, 1], support=['x', 'y'], squeeze=True)

    def _marginal(self, label: str) -> Distribution:
        return self.p_X

    def _mutual_information(self, label_1: str, label_2: str) -> float:
        true_mi = (
                self.p_X.entropy()*2 - self.p_XY.entropy()
        ).sum().item()
        return true_mi


