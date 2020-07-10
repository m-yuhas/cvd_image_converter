# CVD Image Converter
[中文指南](https://github.com/m-yuhas/cvd_image_converter/blob/master/doc/读我档案.md)

[Documentación en español](https://github.com/m-yuhas/cvd_image_converter/blob/master/doc/LÉAME.md)

[Documentation en français](https://github.com/m-yuhas/cvd_image_converter/blob/master/doc/LISEZ-MOI.md)

## Introduction
Color Vision Deficiency (CVD) more commonly known as colorblindness affects
between four and eight percent of the population[1].  This means anytime you
give a presentation or submit a publication there is a good chance that some
member of the audience will suffer from CVD.  Normally this can be dealt with by
creating figures, charts, and tables using a CVD friendly color palette.
However, sometimes you may have figures that need to be converted to a CVD
friendly color palette where the original data is not available to reproduce the
image, or recreating the image may be time consuming.  This python module allows
you to convert any image to an image using only hues in the CVD friendly color
palette designed by Okabe and Ito in [1].  This module preserves the saturation
and value of each pixel so that shading and monochromatic details still appear.

## Quick Start
* Install the package:

```
pip install cvd_image_converter
```

## API Documentation
For the complete API documentation, [click here](https://github.com/m-yuhas/cvd_image_converter/blob/master/doc/api_documentation.md).

## Theory of Operation


## Dependencies
The following Pypi packages are required:
* numpy
* opencv-python

## Contributing
Suggestions and pull requests are welcome.  If you find a bug and don't have
time to fix it yourself, feel free to open an issue.

## References
