from typing import List, Optional

import torch
from torch.distributions import Distribution
from pyro.distributions import ConditionalDistribution

from torch_mist.estimators.generative.base import GenerativeMIEstimator
from torch_mist.utils.caching import cached, reset_cache_before_call


class DoE(GenerativeMIEstimator):
    def __init__(
        self,
        q_Y_given_X: ConditionalDistribution,
        q_Y: Distribution,
    ):
        super().__init__(
            q_Y_given_X=q_Y_given_X,
        )
        self.q_Y = q_Y

    @cached
    def approx_log_p_y(
        self, y: torch.Tensor, x: Optional[torch.Tensor] = None
    ) -> torch.Tensor:
        log_q_y = self.q_Y.log_prob(y)
        assert log_q_y.shape == y.shape[:-1]
        return log_q_y

    @reset_cache_before_call
    def loss(
        self,
        x: torch.Tensor,
        y: torch.Tensor,
    ) -> torch.Tensor:
        log_q_y_given_x = self.approx_log_p_y_given_x(x=x, y=y)
        log_q_y = self.approx_log_p_y(x=x, y=y)

        loss = -log_q_y - log_q_y_given_x

        assert loss.shape == y.shape[:-1]

        return loss.mean()

    def __repr__(self):
        s = self.__class__.__name__ + "(\n"
        s += (
            "  "
            + "(q_Y_given_X): "
            + str(self.q_Y_given_X).replace("\n", "  \n")
            + "\n"
        )
        s += "  " + "(q_Y): " + str(self.q_Y).replace("\n", "  \n") + "\n"
        s += ")" + "\n"
        return s


def doe(
    x_dim: Optional[int] = None,
    y_dim: Optional[int] = None,
    hidden_dims: Optional[List[int]] = None,
    q_Y_given_X: Optional[ConditionalDistribution] = None,
    q_Y: Optional[Distribution] = None,
    conditional_transform_name: str = "conditional_linear",
    n_conditional_transforms: int = 1,
    marginal_transform_name: str = "linear",
    n_marginal_transforms: int = 1,
) -> DoE:
    from torch_mist.distributions.utils import (
        conditional_transformed_normal,
        transformed_normal,
    )

    if q_Y_given_X is None:
        if x_dim is None or y_dim is None or hidden_dims is None:
            raise ValueError(
                "Either q_Y_given_X or x_dim, y_dim and hidden_dims must be specified."
            )
        q_Y_given_X = conditional_transformed_normal(
            input_dim=y_dim,
            context_dim=x_dim,
            hidden_dims=hidden_dims,
            transform_name=conditional_transform_name,
            n_transforms=n_conditional_transforms,
        )

    if q_Y is None:
        if y_dim is None or hidden_dims is None:
            raise ValueError(
                "Either q_Y or y_dim and hidden_dims must be specified."
            )
        q_Y = transformed_normal(
            input_dim=y_dim,
            hidden_dims=hidden_dims,
            transform_name=marginal_transform_name,
            n_transforms=n_marginal_transforms,
        )

    return DoE(
        q_Y_given_X=q_Y_given_X,
        q_Y=q_Y,
    )
