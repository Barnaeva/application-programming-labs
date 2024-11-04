import cv2

from numpy import ndarray


def rotation(img: ndarray, size: [int, int], angel: float) -> ndarray:
    """
    Rotates the input image by a specified angle and resizes it.

    :param img: Input image (ndarray).
    :param size: Desired output size (height, width).
    :param angel: Rotation angle in degrees.
    :return: Rotated and resized image (ndarray).
    """
    height, width = size
    matrix = cv2.getRotationMatrix2D(((height - 1) / 2.0, (width - 1) / 2.0), angel, 1)
    dst = cv2.warpAffine(img, matrix, (height, width))
    return dst