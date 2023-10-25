from typing import Union
import numpy as np

def window1d(input_array: Union[list, np.ndarray], size: int, shift: int = 1, stride: int = 1) -> Union[list[list], np.ndarray]:
    """
    Create 1D windows of data from an input array.

    Args:
        input_array (Union[list, np.ndarray]): The input data as a list or a 1D NumPy array.
        size (int): The size of each window.
        shift (int, optional): The shift value between windows. Defaults to 1.
        stride (int, optional): The stride value within each window. Defaults to 1.

    Returns:
        Union[list[list], np.ndarray]: A list of windows, where each window is a list or a 1D NumPy array.
    
    Raises:
        ValueError: If the input data type is not list or 1D NumPy array, 
        or if any of the size, shift, or stride values are not positive integers.
    """
    if not isinstance(input_array, (list, np.ndarray)):
        raise ValueError("Input must be a list or 1D NumPy array.")
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer.")
    if not isinstance(shift, int) or shift <= 0:
        raise ValueError("Shift must be a positive integer.")
    if not isinstance(stride, int) or stride <= 0:
        raise ValueError("Stride must be a positive integer.")
    
    if isinstance(input_array, list):
        input_array = np.array(input_array)

    num_samples = len(input_array)
    windows = []

    for start in range(0, num_samples - size + 1, shift):
        end = start + size
        window = input_array[start:end:stride]
        windows.append(window)

    return windows