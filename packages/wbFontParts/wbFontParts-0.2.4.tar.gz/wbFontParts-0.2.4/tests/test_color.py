import unittest

from fontParts.test import test_color
from objectGenerator import wbFontPartObjectGenerator

from wbFontParts.color import Color

test_color.Color = Color


class TestColor(test_color.TestComponent):
    objectGenerator = wbFontPartObjectGenerator


if __name__ == "__main__":
    unittest.main()
