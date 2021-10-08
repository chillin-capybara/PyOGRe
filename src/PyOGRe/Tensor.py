from dataclasses import dataclass
import numpy.typing as npt
from typing import Optional, Tuple

from PyOGRe.Metric import Metric


@dataclass
class Tensor:
    """
    Generic Tensor class used to represent Tensors in General Relativity
    Defines operations between Tensors
    """

    metric: Metric
    type: Tuple[int, int] = (1, 0)
    components: Optional[npt.ArrayLike] = None

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __str__(self):
        return f"Type: {self.type}, Metric:\n{self.metric}\nComponents: {self.components}"
