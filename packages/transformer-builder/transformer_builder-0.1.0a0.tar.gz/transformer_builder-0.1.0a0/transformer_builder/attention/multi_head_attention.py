from typing import List

import torch
from torch import nn

from .self_attention import SelfAttention


class MultiHeadAttention(nn.Module):
    """
    This class implements the Multi-Head Attention.
    """

    def __init__(
        self,
        layer_before: nn.Module = nn.Identity(),
        self_attention_heads: List[nn.Module] = None,
        layer_after: nn.Module = nn.Identity(),
    ) -> None:
        """
        Args:
            layer_before: Used before the attention heads.

            self_attention_heads: A list of SelfAttention heads.

            layer_after: Used after the attention heads.
        """
        super().__init__()
        self.layer_before = layer_before

        self.self_attention_heads = self_attention_heads or [SelfAttention()]

        if not self.self_attention_heads:
            raise ValueError("self_attention_heads must not be empty")

        self.layer_after = layer_after

    def forward(
        self,
        x: torch.Tensor,
        mask: torch.Tensor = None,
    ) -> torch.Tensor:
        """
        This method implements the forward pass of the Multi-Head Attention.
        Args:
            x: The input tensor of shape
            (optional_batch_size, sequence_length, embedding_dim).

            mask: The mask tensor of shape
            (optional_batch_size, sequence_length, sequence_length).
            Used to mask the attention.

        Returns:
            Tensor: The output tensor.
        """
        x = self.layer_before(x)
        heads_output = [
            self_attention_head(x, mask)
            for self_attention_head in self.self_attention_heads
        ]

        x = torch.concat(heads_output, dim=-1)

        return self.layer_after(x)
