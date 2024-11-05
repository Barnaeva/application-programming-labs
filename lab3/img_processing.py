import cv2

from numpy import ndarray


def read(name_file: str) -> ndarray:
    """
    Reads an image from a file.
    :param name_file: Name of the image file.
    :return: The image read from the file (ndarray).
    """
    my_img = cv2.imread(name_file)
    return my_img


def look_img(my_img: ndarray) -> None:
    """
    Displays the image in a window.
    :param my_img: The image to display (ndarray).
    """
    cv2.imshow('image', my_img)
    cv2.waitKey(2000)


def size(my_img: ndarray) -> [int, int]:
    """
    Returns the dimensions of the image.
    :param my_img: The image to measure (ndarray).
    :return: A tuple of (height, width).
    """
    height, width, num = my_img.shape
    return height, width
