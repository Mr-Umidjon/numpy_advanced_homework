import numpy as np


def max_all(arr: np.ndarray) -> int:
    """
    Returns the max of all numbers in the array
    Args:
        arr: np.ndarray
    Returns:
        int: max of all numbers
    """
    return arr.max()


# print(max_all(np.array([[1, 2, 34, 45], [2, 23, 34, 1]])))
