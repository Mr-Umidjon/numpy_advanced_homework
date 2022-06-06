import numpy as np


def sum_all(arr: np.ndarray) -> int:
    """
    Returns the sum of all numbers in the array
    Args:
        arr: np.ndarray
    Returns:
        int: sum of all numbers
    """
    S = 0
    r, c = arr.shape
    for i in range(r):
        for j in range(c):
            S += arr[i, j]
    return S


print(sum_all(np.array([[1, 2, 3]])))
