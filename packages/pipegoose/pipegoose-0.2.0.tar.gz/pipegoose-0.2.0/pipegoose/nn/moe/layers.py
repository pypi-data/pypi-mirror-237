from torch import nn
from torchtyping import TensorType

from pipegoose.distributed.parallel_context import ParallelContext
from pipegoose.nn.expert_parallel.routers import Router


class ExpertLayer:
    """An MoE layer."""

    def __init__(self, num_experts: int, expert: nn.Module, router: Router, parallel_context: ParallelContext):
        self.num_experts = num_experts
        self.expert = expert
        self.router = router
        self.parallel_context = parallel_context

    def forward(self, inputs: TensorType["batch", "seq_len", "d_model"]) -> TensorType["batch", "seq_len", "d_model"]:
        pass
