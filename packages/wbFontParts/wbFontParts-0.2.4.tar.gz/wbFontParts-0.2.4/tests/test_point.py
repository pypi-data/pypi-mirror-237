import unittest

from fontParts.test import test_point
from objectGenerator import wbFontPartObjectGenerator

from wbFontParts.contour import RContour
from wbFontParts.font import RFont
from wbFontParts.glyph import RGlyph
from wbFontParts.layer import RLayer
from wbFontParts.point import RPoint


class TestPoint(test_point.TestPoint):
    objectGenerator = wbFontPartObjectGenerator

    def test_wbFontPartObjects(self):
        contour, _ = self.objectGenerator("contour")
        self.assertIsInstance(contour, RContour)

        font, _ = self.objectGenerator("font")
        self.assertIsInstance(font, RFont)

        glyph, _ = self.objectGenerator("glyph")
        self.assertIsInstance(glyph, RGlyph)

        layer, _ = self.objectGenerator("layer")
        self.assertIsInstance(layer, RLayer)

        point, _ = self.objectGenerator("point")
        self.assertIsInstance(point, RPoint)


if __name__ == "__main__":
    unittest.main()
