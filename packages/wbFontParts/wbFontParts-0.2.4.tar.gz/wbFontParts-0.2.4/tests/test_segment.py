import unittest

from fontParts.test import test_segment
from objectGenerator import wbFontPartObjectGenerator

from wbFontParts.contour import RContour


class TestSegment(test_segment.TestSegment):
    objectGenerator = wbFontPartObjectGenerator

    def test_wbFontPartObjects(self):
        contour, _ = self.objectGenerator("contour")
        self.assertIsInstance(contour, RContour)


if __name__ == "__main__":
    unittest.main()
