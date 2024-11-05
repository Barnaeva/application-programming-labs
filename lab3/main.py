import argparse

from histogram import make_histogram, make_pic
from img_processing import look_img, read, size
from task import rotation


def pars() -> (str, float):
    """
    Parses command-line arguments for the image file name and rotation angle.
    :return: A tuple containing the image file name (str) and the rotation angle (float).
    """
    parser = argparse.ArgumentParser(description='Process an image with optional rotation.')
    parser.add_argument('name_file', type=str, help='Name of the image file.')
    parser.add_argument('-a', '--angle', type=float, help='Rotation angle in degrees.')
    args = parser.parse_args()

    return args.name_file, args.angle


def main():
    try:
        name_file, angle = pars()

        img = read(name_file)
        look_img(img)
        size_img = size(img)

        hist = make_histogram(img)
        make_pic(hist)

        if angle is not None:
            dst = rotation(img, size_img, angle)
            look_img(dst)

        print(f"Image size: {size_img}")
    except Exception as exc:
        print(f"Error: {exc}")

if __name__ == "__main__":
    main()
