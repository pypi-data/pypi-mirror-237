from typing import Callable, Dict, List, Tuple, Union

import torch
import torch.distributed as dist

from pipegoose.core.bucket.bucket import Bucket
from pipegoose.core.bucket.utils import mb_size_to_num_elements
from pipegoose.distributed.functional import all_reduce
from pipegoose.distributed.parallel_context import ParallelContext
from pipegoose.distributed.parallel_mode import ParallelMode

OPERATOR_MAPPING = {dist.all_reduce: all_reduce}

DistOperator = Union[
    dist.broadcast,
    dist.all_reduce,
    dist.reduce,
    dist.all_gather,
    dist.gather,
    dist.scatter,
    dist.reduce_scatter,
    dist.all_to_all,
]


def _set_tensor_storage(orig_tensor: torch.Tensor, output_tensor: torch.Tensor):
    """After execute a distributed operation, set the tensor's storage to the resulting tensor."""
    # orig_tensor = output.clone()
    orig_tensor.copy_(output_tensor)


class BucketDistributor:
    """
    Perform an asynchronous, distributed operation on a bucket,
    filling it until full before executing the operation.

    NOTE: Inspired from the design of FairScale's ReduceScatterBucketer
    https://github.com/facebookresearch/fairscale/blob/164cc0f3170b4a3951dd84dda29c3e1504ac4d6e/fairscale/internal/reduce_scatter_bucketer.py#L74
    """

    # DIST_OPERATOR = [dist.broadcast, dist.all_reduce, dist.reduce, dist.all_gather, dist.gather, dist.scatter, dist.reduce_scatter, dist.all_to_all]

    def __init__(self, op: DistOperator, bucket_size_mb: Union[int, float], parallel_context: ParallelContext = None):
        assert op in OPERATOR_MAPPING, f"Operation must be one of {OPERATOR_MAPPING}."
        assert bucket_size_mb > 0, "Bucket size must be greater than 0."

        self.op = op
        self.bucket_size_mb = bucket_size_mb
        self.parallel_context = parallel_context
        self.buckets: Dict[Tuple[torch.dtype, ParallelMode], Bucket] = {}
        self.callbacks: List[Callable] = []

    @torch.no_grad()
    def execute(self, tensor: torch.Tensor, parallel_mode: ParallelMode):
        bucket_size_in_tensor_dtype = mb_size_to_num_elements(self.bucket_size_mb, tensor.dtype)
        if tensor.numel() > bucket_size_in_tensor_dtype:
            # NOTE: execute the operation if the tensor is larger than the bucket size
            OPERATOR_MAPPING[self.op](tensor, parallel_context=self.parallel_context, parallel_mode=parallel_mode)
            return

        # NOTE: execute the bucket if the tensor is larger than the available space,
        # then empty and refill the bucket with the tensor
        key = (tensor.dtype, parallel_mode)
        if key not in self.buckets:
            num_elements = mb_size_to_num_elements(self.bucket_size_mb, tensor.dtype)
            self.buckets[key] = Bucket(num_elements, tensor.dtype)

        bucket = self.buckets[key]
        if tensor.numel() > bucket.available_size:
            # NOTE: execute the operation on the available tensors in the bucket
            # then clear the bucket
            # and append the tensor to the bucket
            self._execute_bucket(bucket, parallel_mode)

        start = bucket._offset
        bucket.add_tensor(tensor)
        end = bucket._offset
        self.callbacks.append(lambda: _set_tensor_storage(tensor, bucket.data[start:end]))

    def _execute_bucket(self, bucket: Bucket, parallel_mode: ParallelMode):
        data = bucket.data
        OPERATOR_MAPPING[self.op](data, parallel_context=self.parallel_context, parallel_mode=parallel_mode)

        for callback in self.callbacks:
            callback()

        assert 1 == 1
        bucket.clear()
        # return data
