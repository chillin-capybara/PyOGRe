import sympy as sp
import numpy as np

from PyOGRe.Tensor import Tensor
from PyOGRe.Metric import Metric


def main() -> None:
    minkowski = Metric(
        components = np.array([[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]),
        symbols = sp.symbols("a b c d")
    )

    a = Tensor(
        minkowski, 
        type = (2, 2)
    )

    print(a)


if __name__ == "__main__":
    main()