import unittest

from fontParts.test import test_world
from objectGenerator import wbFontPartObjectGenerator

from wbFontParts.font import RFont

class TestFontList(test_world.TestFontList):
    objectGenerator = wbFontPartObjectGenerator

    def test_wbFontPartObjects(self):
        font, _ = self.objectGenerator("font")
        self.assertIsInstance(font, RFont)

class TestFontOpen(test_world.TestFontOpen):
    objectGenerator = wbFontPartObjectGenerator

    def test_wbFontPartObjects(self):
        font, _ = self.objectGenerator("font")
        self.assertIsInstance(font, RFont)

class TestOpenFonts(test_world.TestOpenFonts):
    objectGenerator = wbFontPartObjectGenerator

    def test_wbFontPartObjects(self):
        font, _ = self.objectGenerator("font")
        self.assertIsInstance(font, RFont)


if __name__ == "__main__":
    unittest.main()
