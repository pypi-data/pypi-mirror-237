from dataclasses import dataclass

import torch

from pipegoose.nn.pipeline_parallel._job.job_type import JobType


@dataclass
class TrainingMetadata:
    is_training: bool
    is_grad_enabled: bool


@dataclass
class Metadata:
    """Metadata for the output of a job."""

    # pipeline
    # the index of the microbatch and partition that return this package
    microbatch_idx: int
    partition_idx: int

    job_type: JobType

    training: TrainingMetadata

    # global rank
    src: int
    dst: int


class Package:
    """A data package that will be sent from one pipeline stage to another."""

    def __init__(self, data: torch.Tensor, metadata: Metadata):
        self.data = data
        self.metadata = metadata
