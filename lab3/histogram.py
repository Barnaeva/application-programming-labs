import cv2
import matplotlib.pyplot as plt


from numpy import ndarray


def make_histogram(img: ndarray) -> list:
    """
    Calculates the histogram for each color channel of the image.
    :param img: Input image (ndarray).
    :return: A list of histograms for each color channel.
    """
    hist = []
    for i in range(3):
        hist.append(cv2.calcHist([img], [i], None, [256], [0, 256]))
    return hist


def make_pic(hist: list) -> None:
    """
    Plots the histograms for the color channels.
    :param hist: List of histograms for each color channel.
    """
    colors = ['blue', 'green', 'red']
    for i, col in enumerate(colors):
        plt.plot(hist[i], label=col, color=col)

    plt.title('Color Histogram')
    plt.xlabel('Pixel Intensity (0-255)')
    plt.ylabel('Number of Pixels')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.legend()
    plt.show()