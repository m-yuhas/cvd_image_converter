"""This module contains utilities to convert an image to CVD safe color
palette. The intended use is to convert the coloring of charts and figures
before publication in the event that only the figure is available and
replotting the data with a CVD safe color palette is not possible."""

from .cvd_image_converter import convert_color_palette, CVD_HUES
