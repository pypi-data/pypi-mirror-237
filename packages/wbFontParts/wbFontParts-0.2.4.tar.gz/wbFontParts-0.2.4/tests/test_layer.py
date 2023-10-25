import unittest

from fontParts.test import test_layer
from objectGenerator import wbFontPartObjectGenerator

from wbFontParts.glyph import RGlyph
from wbFontParts.layer import RLayer


class TestLayer(test_layer.TestLayer):
    objectGenerator = wbFontPartObjectGenerator

    def test_wbFontPartObjects(self):
        glyph, _ = self.objectGenerator("glyph")
        self.assertIsInstance(glyph, RGlyph)

        layer, _ = self.objectGenerator("layer")
        self.assertIsInstance(layer, RLayer)


if __name__ == "__main__":
    unittest.main()
