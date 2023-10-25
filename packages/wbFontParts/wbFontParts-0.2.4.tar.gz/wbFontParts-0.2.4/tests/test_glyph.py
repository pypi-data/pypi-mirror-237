import unittest

from fontParts.test import test_glyph
from objectGenerator import wbFontPartObjectGenerator

from wbFontParts.bPoint import RBPoint
from wbFontParts.contour import RContour
from wbFontParts.font import RFont
from wbFontParts.glyph import RGlyph
from wbFontParts.layer import RLayer
from wbFontParts.point import RPoint

# orphan glyphs are not selectable in wbDefcon
del test_glyph.TestGlyph.test_selected_true

class TestGlyph(test_glyph.TestGlyph):
    objectGenerator = wbFontPartObjectGenerator

    def test_wbFontPartObjects(self):
        bPoint, _ = self.objectGenerator("bPoint")
        self.assertIsInstance(bPoint, RBPoint)

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


    def test_removeOverlap(self):
        # use assertEqual instead of assertEquals to prevent DeprecationWarning
        glyph = self.getGlyph_generic()
        self.assertEqual(len(glyph), 2)
        glyph.removeOverlap()
        self.assertEqual(len(glyph), 1)


if __name__ == "__main__":
    unittest.main()
