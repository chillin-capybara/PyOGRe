import sympy as sp

from dataclasses import dataclass
import numpy.typing as npt
from typing import Optional


@dataclass
class Metric:
    """Generic Metric class used to represent Metrics in General Relativity"""

    components: npt.ArrayLike
    symbols: Optional[sp.symbols] = sp.symbols("t x y z")

    def __abs__(self):
        pass

    def __str__(self):
        return self.components, self.symbols
