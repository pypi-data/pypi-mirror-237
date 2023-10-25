import unittest

from fontParts.test import test_kerning
from objectGenerator import wbFontPartObjectGenerator

from wbFontParts.font import RFont


class TestKerning(test_kerning.TestKerning):
    objectGenerator = wbFontPartObjectGenerator

    def test_wbFontPartObjects(self):
        font, _ = self.objectGenerator("font")
        self.assertIsInstance(font, RFont)


if __name__ == "__main__":
    unittest.main()
