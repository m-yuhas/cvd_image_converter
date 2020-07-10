"""Module to convert charts and graphs to a CVD safe color palette"""


import cv2
import numpy


CVD_HUES = numpy.array([29, 143, 116, 40, 143, 19, 231])


def convert_color_palette(image: numpy.ndarray,
                          palette: numpy.ndarray = CVD_HUES) -> numpy.ndarray:
    """Convert the color palette of the input image to a palette of hues
    defined as a numpy array.  The conversion takes place by converting the
    image to the HSV color space and adjusting the hue of each pixel to the
    closest hue in the desired color palette.  The saturation and value are
    left unchanged so that shading and monochromatic pixels will not be
    affected.

    Args:
        image: Numpy array of the input image, in the RGB format.
        palette: Numpy array of the list of allowable hues in the output image,
            The hues are given as a fraction of the max hue value of 255, so to
            convert a hue given in degrees, divide it by 360 and then multiply
            by 255.  For example, green is 120 degrees, so in this array, it
            would be represented by int((120 / 360) * 255) = 85.

    Returns:
        A numpy array of the output image in the RGB format.
    """
    height, width, _ = image.shape
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    for row in range(height):
        for column in range(width):
            hsv_image[row, column, 0] = palette[numpy.argmin(
                numpy.abs((palette - hsv_image[row, column, 0]) % 255))]
    return cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
