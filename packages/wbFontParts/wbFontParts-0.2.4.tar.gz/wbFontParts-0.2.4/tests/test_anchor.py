import unittest

from fontParts.test import test_anchor
from objectGenerator import wbFontPartObjectGenerator

from wbFontParts.anchor import RAnchor
from wbFontParts.font import RFont
from wbFontParts.glyph import RGlyph
from wbFontParts.layer import RLayer


class TestAnchor(test_anchor.TestAnchor):
    objectGenerator = wbFontPartObjectGenerator

    def test_wbFontPartObjects(self):
        anchor, _ = self.objectGenerator("anchor")
        self.assertIsInstance(anchor, RAnchor)

        font, _ = self.objectGenerator("font")
        self.assertIsInstance(font, RFont)

        glyph, _ = self.objectGenerator("glyph")
        self.assertIsInstance(glyph, RGlyph)

        layer, _ = self.objectGenerator("layer")
        self.assertIsInstance(layer, RLayer)


if __name__ == "__main__":
    unittest.main()
