import unittest

from fontParts.test import test_lib
from objectGenerator import wbFontPartObjectGenerator

from wbFontParts.font import RFont
from wbFontParts.glyph import RGlyph
from wbFontParts.layer import RLayer
from wbFontParts.lib import RLib


class TestLib(test_lib.TestLib):
    objectGenerator = wbFontPartObjectGenerator

    def test_wbFontPartObjects(self):

        font, _ = self.objectGenerator("font")
        self.assertIsInstance(font, RFont)

        glyph, _ = self.objectGenerator("glyph")
        self.assertIsInstance(glyph, RGlyph)

        layer, _ = self.objectGenerator("layer")
        self.assertIsInstance(layer, RLayer)

        lib, _ = self.objectGenerator("lib")
        self.assertIsInstance(lib, RLib)


if __name__ == "__main__":
    unittest.main()
