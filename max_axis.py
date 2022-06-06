import numpy as np


def max_axis_1(arr: np.ndarray) -> int:
    """
    Returns the max of rows in the array
    Args:
        arr: np.ndarray
    Returns:
        np.ndarray: max of each row
    """
    return arr.max(axis=1)


# print(max_axis_1(np.array([[13, 2, 3], [1, 2, 3]])))
