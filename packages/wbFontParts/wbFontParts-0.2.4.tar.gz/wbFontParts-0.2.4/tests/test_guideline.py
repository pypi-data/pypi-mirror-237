import unittest

from fontParts.test import test_guideline
from objectGenerator import wbFontPartObjectGenerator

from wbFontParts.font import RFont
from wbFontParts.glyph import RGlyph
from wbFontParts.guideline import RGuideline
from wbFontParts.layer import RLayer


class TestGuideline(test_guideline.TestGuideline):
    objectGenerator = wbFontPartObjectGenerator

    def test_wbFontPartObjects(self):
        font, _ = self.objectGenerator("font")
        self.assertIsInstance(font, RFont)

        glyph, _ = self.objectGenerator("glyph")
        self.assertIsInstance(glyph, RGlyph)

        guideline, _ = self.objectGenerator("guideline")
        self.assertIsInstance(guideline, RGuideline)

        layer, _ = self.objectGenerator("layer")
        self.assertIsInstance(layer, RLayer)


if __name__ == "__main__":
    unittest.main()
