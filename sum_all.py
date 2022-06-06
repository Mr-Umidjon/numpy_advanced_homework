import numpy as np


def sum_all(arr: np.ndarray) -> int:
    """
    Returns the sum of all numbers in the array
    Args:
        arr: np.ndarray
    Returns:
        int: sum of all numbers
    """
    return arr.sum()


print(sum_all(np.arange(10)))
