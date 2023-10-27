import random
import numpy as np
from typing import List, TypeVar

"""Create custom Generic types for each function."""
Matrix = TypeVar("Matrix", bound=List[List[float]])
Array1D = TypeVar("Array1D", List[float], np.ndarray)
Matrix2D = TypeVar("Matrix2D", bound=np.ndarray)


def create_random_matrix(rows: int, columns: int) -> Matrix:
    """
    Create a matrix filled with random numbers.

    Example use:
    >>> create_random_matrix(3, 4)
    """
    return [[random.randint(0, 10) for column in range(columns)] for row in range(rows)]


def transpose2d(input_matrix: Matrix) -> Matrix:
    """
    Transpose a 2D matrix using Python standard library, by swapping rows with columns.

    Parameters:
    - input_matrix (Matrix): The input is a 2D list of floats.

    Returns:
    - Matrix: The transposed matrix as a 2D list of floats.

    Raises:
    - Exception: If an error in matrix transposition occurs.

    Example use:
    >>> input_matrix = [[1, 2], [4, 5], [2, 15]]
    >>> transposed = transpose2d(input_matrix=input_matrix)
    >>> transposed
    [[1, 4, 2], [2, 5, 15]]
    """
    rows = len(input_matrix)
    columns = len(input_matrix[0])

    transposed = []
    for _ in range(columns):
        transposed.append([0] * rows)

    # Fill empty matrix with transposed elements using nested loops
    try:
        for row in range(rows):
            for col in range(columns):
                transposed[col][row] = input_matrix[row][col]
        return transposed
    except Exception as e:
        print("Error in transposition operation:", str(e))
        return None


def window1d(
    input_array: Array1D,
    size: int,
    shift: int = 1,
    stride: int = 1,
) -> List[Array1D]:
    """
    Create a windowed data set from a 1D array or list with slicing.

    Parameters:
    - input_array (Array1D): 1D np.array or list input array.
    - size (int) The number of objects per returned window.
    - shift (int, optional): The number of positions window steps between different windows.
    - stride (int, optional): The number of positions stepped within each window.

    Returns:
    - List[Array1D]: A list or 1D numpy array of windowed segments.

    Raises:
    - Exception: If an error occurs during time series windowing.

    Example use:
    >>> input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> windowed = window1d(input_array=input_array, size=2, shift=2, stride=2)
    >>> windowed
    [[1, 3], [3, 5], [5, 7], [7, 9]]
    """

    # Ensure inputs size, shift, and stride are positive
    if size <= 0 or shift <= 0 or stride <= 0:
        raise ValueError("Parameters size, shift and stride must be positive.")

    if (
        not isinstance(size, int)
        or not isinstance(shift, int)
        or not isinstance(stride, int)
    ):
        raise ValueError("size, shift and stride must be integer.")

    if not isinstance(input_array, (np.ndarray, list)):
        raise TypeError("input_array must be a list or a 1D np.ndarray")

    windows = []

    # Get the number of loops/windows
    num_loops = (len(input_array) - size * stride) // shift + 1

    # Use slicing and stride to extract each window
    try:
        for i in range(num_loops):
            start = i * shift
            end = start + size * stride
            window = input_array[start:end:stride]
            windows.append(window)
        return windows
    except Exception as e:
        print("Error occurred performing windowing:", str(e))
        return None


def convolution2d(
    input_matrix: Matrix2D, kernel: Matrix2D, stride: int = 1
) -> Matrix2D:
    """
    Compute the 2D cross-correlation between the input matrix and kernel, by sliding the kernel over the input matrix and computing the sum of element-wise products at each position.
    The positions where the input_matrix and the kernel cannot fully overlap are excluded from the output.

    Parameters:
    - input_matrix (Matrix2D): 2D numpy array input matrix.
    - kernel (Matrix2D): 2D numpy array convolution kernel.
    - stride (int, optional): Integer representing the stride of the convolution operation. Default is 1.

    Returns:
    - Matrix2D: 2D numpy array representing the result of the cross-correlation operation between the input matrix and the kernel.

    Raises:
    - ValueError: If stride is not a positive integer.
    - TypeError: If input_matrix or kernel is not a 2D np.ndarray.
    - ValueError: If kernel dimensions are bigger than input_matrix dimensions.

    Example use:
        >>> input_matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        >>> kernel = np.array([[1, 0], [1, 0]])
        >>> stride = 2
        >>> convolved = convolution2d(input_matrix=input_matrix, kernel=kernel, stride=2)
        >>> convolved
        [[ 7. 11.],
        [23. 27.]]

    """

    input_rows, input_cols = input_matrix.shape
    kernel_rows, kernel_cols = kernel.shape

    # Ensure inputs size, shift, and stride are positive
    if stride <= 0 or not isinstance(stride, int):
        raise ValueError("Stride must be a positive integer.")

    # Ensure inputs are 2D arrays
    if (
        not isinstance(input_matrix, np.ndarray)
        or input_matrix.ndim != 2
        or not isinstance(kernel, np.ndarray)
        or kernel.ndim != 2
    ):
        raise TypeError("input_matrix and kernel must 2D np.ndarray.")

    # Ensure matrix and kernel shapes are compatible
    if input_rows <= kernel_rows or input_cols <= kernel_cols:
        raise ValueError(
            "Input matrix dimensions must be greater or equal to kernel dimensions."
        )

    output_rows = (input_rows - kernel_rows) // stride + 1
    output_cols = (input_cols - kernel_cols) // stride + 1

    output = np.zeros((output_rows, output_cols))

    # Slide the kernel over the input matrix and compute the cross-correlation
    for i in range(output_rows):
        for j in range(output_cols):
            sum_val = 0
            for x in range(kernel_rows):
                for y in range(kernel_cols):
                    matrix = input_matrix[i * stride + x][j * stride + y]
                    sum_val += matrix * kernel[x][y]
            output[i][j] = sum_val

    return output
