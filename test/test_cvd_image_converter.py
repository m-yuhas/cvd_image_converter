"""Unit test cases for the cvd_image_converter module."""


import os
import unittest
import cv2
import numpy
import cvd_image_converter


class TestConvertColorPalette(unittest.TestCase):
    """Test case for the convert_color_palette function."""

    def setUp(self) -> None:
        """Get this file's path so that the test resources can be loaded."""
        self.dirname = os.path.dirname(os.path.realpath(__file__))

    def check_conversion(self, test_path: str, expected_path: str) -> None:
        """Check the conversion to a CVD safe color set.  The conversion result
        should be the same as the expected output image.

        Args:
            test_path: String of the path to the test image.
            expected_path: String of the path to the expected output image.
        """
        self.assertTrue(
            numpy.array_equal(
                cvd_image_converter.convert_color_palette(
                    cv2.imread(os.path.join(self.dirname, test_path))),
                cv2.imread(os.path.join(self.dirname, expected_path))),
            'Actual output does not match expectation.')

    def test_line_graph(self) -> None:
        """Test a line graph."""
        self.check_conversion('line_graph.png', 'line_graph_cvd.png')

    def test_heat_map(self) -> None:
        """Test a heat map."""
        self.check_conversion('heat_map.png', 'heat_map_cvd.png')

    def test_scatter_plot(self) -> None:
        """Test a scatter plot."""
        self.check_conversion('scatter_plot.png', 'scatter_plot_cvd.png')

    def test_bar_chart(self) -> None:
        """Test a bar chart."""
        self.check_conversion('bar_chart.png', 'bar_chart_cvd.png')

    def test_photograph(self) -> None:
        """Test a photograph."""
        self.check_conversion('photograph.png', 'photograph_cvd.png')
