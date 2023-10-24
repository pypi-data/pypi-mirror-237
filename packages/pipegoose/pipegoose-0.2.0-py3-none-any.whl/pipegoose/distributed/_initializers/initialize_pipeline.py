# Copyright 2021 HPC-AI Technology Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Modified by pipegoose's contributors.

import torch.distributed as dist

from pipegoose.distributed._initializers.initializer import (
    ProcessGroupInitializer,
    ProcessGroupResult,
)
from pipegoose.distributed.parallel_mode import ParallelMode


class PipelineParallelGroupInitializer(ProcessGroupInitializer):
    def init_dist_group(self) -> ProcessGroupResult:
        num_pipeline_parallel_groups = self.world_size // self.pipeline_parallel_size
        local_rank = None
        local_world_size = None
        ranks_in_group = None
        process_group = None
        parallel_mode = ParallelMode.PIPELINE

        for i in range(num_pipeline_parallel_groups):
            ranks = list(range(i, self.world_size, num_pipeline_parallel_groups))

            # NOTE: dist.new_group() must be called collectively by all the processes
            # that would be part of the group, which means every process in the group
            # needs to call this function. If only a subset of the processes call new_group(),
            # it will hang because it's waiting for the rest of the processes to join.
            group = dist.new_group(ranks=ranks)

            if self.rank in ranks:
                local_rank = ranks.index(self.rank)
                local_world_size = len(ranks)
                ranks_in_group = ranks
                process_group = group

        return {
            "local_rank": local_rank,
            "process_group": process_group,
            "local_world_size": local_world_size,
            "ranks_in_group": ranks_in_group,
            "parallel_mode": parallel_mode,
        }
