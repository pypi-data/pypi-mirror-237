import unittest

from fontParts.test import test_info
from objectGenerator import wbFontPartObjectGenerator

from wbFontParts.font import RFont
from wbFontParts.info import RInfo


class TestInfo(test_info.TestInfo):
    objectGenerator = wbFontPartObjectGenerator

    def test_wbFontPartObjects(self):
        info, _ = self.objectGenerator("info")
        self.assertIsInstance(info, RInfo)

        font, _ = self.objectGenerator("font")
        self.assertIsInstance(font, RFont)


if __name__ == "__main__":
    unittest.main()
