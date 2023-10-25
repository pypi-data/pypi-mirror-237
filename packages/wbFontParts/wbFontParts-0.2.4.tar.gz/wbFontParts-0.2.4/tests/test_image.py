import unittest

from fontParts.test import test_image
from objectGenerator import wbFontPartObjectGenerator

from wbFontParts.font import RFont
from wbFontParts.glyph import RGlyph
from wbFontParts.image import RImage
from wbFontParts.layer import RLayer


class TestImage(test_image.TestImage):
    objectGenerator = wbFontPartObjectGenerator

    def test_wbFontPartObjects(self):
        font, _ = self.objectGenerator("font")
        self.assertIsInstance(font, RFont)

        glyph, _ = self.objectGenerator("glyph")
        self.assertIsInstance(glyph, RGlyph)

        image, _ = self.objectGenerator("image")
        self.assertIsInstance(image, RImage)

        layer, _ = self.objectGenerator("layer")
        self.assertIsInstance(layer, RLayer)


if __name__ == "__main__":
    unittest.main()
