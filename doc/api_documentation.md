# cvd_image_converter
This module contains utilities to convert an image to CVD safe color
palette. The intended use is to convert the coloring of charts and figures
before publication in the event that only the figure is available and
replotting the data with a CVD safe color palette is not possible.
# convert_color_palette
```python
convert_color_palette(image: numpy.ndarray, palette: numpy.ndarray = array([ 29, 143, 116,  40, 143,  19, 231])) -> numpy.ndarray
```
Convert the color palette of the input image to a palette of hues
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

