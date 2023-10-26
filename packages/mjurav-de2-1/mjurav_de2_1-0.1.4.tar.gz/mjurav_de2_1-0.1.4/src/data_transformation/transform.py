import numpy as np
from data_transformation.input import Convolution2DInput, Transpose2DInput, Window1DInput
from pydantic import ValidationError


def transpose2d(input_matrix: list[list[float]]) -> list:
    """Transpose a 2D matrix.

    This function takes a 2D matrix represented as a list of lists and
    returns its transpose. The input matrix should contain rows with equal lengths.

    Args:
        input_matrix: A 2D matrix where each inner list represents a row.

    Returns:
        (list): The transposed matrix.

    Example::
        transpose2d([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
        [[1.0, 3.0, 5.0], [2.0, 4.0, 6.0]]

    """
    Transpose2DInput(input_matrix=input_matrix)
    return [list(row) for row in zip(*input_matrix)]


def window1d(
    input_array: list | np.ndarray,
    size: int,
    shift: int = 1,
    stride: int = 1,
) -> list[list | np.ndarray]:
    """Generate windows from a 1D input array.

    This function takes a 1D list or Numpy array, and generates a list of windows,
    each of a specified size, shift, and stride.

    Args:
        input_array: A 1D list or Numpy array of real numbers.
        size: The size (length) of each window.
        shift: The shift (step size) between different windows. Defaults to 1.
        stride: The stride (step size) within each window. Defaults to 1.

    Returns:
        A list of windows, where each window a list or 1D Numpy array of real numbers.

    Examples:
        window1d([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=3, shift=2, stride=2)
        > [[1, 3, 5], [3, 5, 7], [5, 7, 9], [7, 9], [9]]

    """
    Window1DInput(
        input_array=input_array,
        size=size,
        shift=shift,
        stride=stride,
    )
    windows = []
    for start in range(0, len(input_array), shift):
        windows.append(input_array[start:start + (size * stride):stride])
    return windows


def convolution2d(
    input_matrix: np.ndarray,
    kernel: np.ndarray,
    stride: int = 1,
) -> np.ndarray:
    """Applies a 2D convolution operation over an input matrix.

    Args:
        input_matrix: The input matrix to be convolved. It should be a 2D numpy array.
        kernel: The convolution kernel. It should be a 2D numpy array with shape
            (k_height, k_width).
        stride: The stride of the convolution. It determines the step size to slide
            the kernel over the input matrix. Default is 1.

    Returns:
        The output matrix after applying the convolution operation. The shape of the
            output depends on the size of the input matrix, kernel, and stride.

    Example:
        input_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        kernel = np.array([[1, 0], [0, -1]])
        convolution2d(input_matrix, kernel)
        array([[ 3.,  1.], [11.,  9.]])

    """
    Convolution2DInput(
        input_matrix=input_matrix,
        kernel=kernel,
        stride=stride,
    )
    m_height, m_width = input_matrix.shape
    k_height, k_width = kernel.shape
    # (W-F+2P)/S+1 formula to calculate output matrix shape.
    output_height = (m_height - k_height) // stride + 1
    output_width = (m_width - k_width) // stride + 1

    output = np.zeros((output_height, output_width))

    for h in range(0, output_height):
        for w in range(0, output_width):
            output[h, w] = np.sum(
                input_matrix[
                    h * stride : h * stride + k_height,
                    w * stride : w * stride + k_width,
                ]
                * kernel,
            )
    return output
