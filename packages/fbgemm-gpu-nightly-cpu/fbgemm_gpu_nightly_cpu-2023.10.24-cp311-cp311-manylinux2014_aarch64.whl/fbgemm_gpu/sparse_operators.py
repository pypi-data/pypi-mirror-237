# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from typing import Optional, Tuple

import torch
from torch import Tensor

try:
    # pyre-ignore
    from fbgemm_gpu import open_source  # noqa: F401
except Exception:
    torch.ops.load_library("//deeplearning/fbgemm/fbgemm_gpu:sparse_ops")
    torch.ops.load_library("//deeplearning/fbgemm/fbgemm_gpu:sparse_ops_cpu")


@torch.library.impl_abstract("fbgemm::permute_2D_sparse_data")
def permute_2D_sparse_data_meta(
    permute: Tensor,
    lengths: Tensor,
    values: Tensor,
    weights: Optional[Tensor] = None,
    permuted_lengths_sum: Optional[int] = None,
) -> Tuple[Tensor, Tensor, Optional[Tensor]]:
    torch._check(
        lengths.dim() == 2, lambda: f"expected lengths.dim() == 2, got {lengths.dim()}"
    )
    T = permute.numel()
    B = lengths.size(1)
    indices = values
    permuted_lengths = lengths.new_empty([T, B])
    permuted_indices_size = 0
    if permuted_lengths_sum is not None:
        permuted_indices_size = permuted_lengths_sum
    else:
        ctx = torch._custom_op.impl.get_ctx()
        permuted_indices_size = ctx.new_dynamic_size()
    # pyre-fixme
    permuted_indices = indices.new_empty(permuted_indices_size)
    permuted_weights = None
    if weights is not None:
        # pyre-fixme
        permuted_weights = weights.new_empty(permuted_indices_size)
    return permuted_lengths, permuted_indices, permuted_weights
