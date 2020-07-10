"""Launch the color space converter from the command line."""


import argparse
import os
import cv2
from .cvd_image_converter import convert_color_palette


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='python -m cvd_image_converter',
        description='Convert an image to a CVD safe color space')
    parser.add_argument(
        'input_image',
        action='store',
        help='Input image, not CVD safe')
    parser.add_argument(
        'output_image',
        action='store',
        help='Output image, CVD safe')
    args = parser.parse_args()
    if not os.path.isfile(args.input_image):
        raise Exception("Input image doesn't exist, please check the path.")
    input_image = cv2.imread(args.input_image)
    cv2.imwrite(args.output_image, convert_color_palette(input_image))
