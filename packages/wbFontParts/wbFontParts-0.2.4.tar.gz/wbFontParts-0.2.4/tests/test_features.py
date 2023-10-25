import unittest

from fontParts.test import test_features
from objectGenerator import wbFontPartObjectGenerator

from wbFontParts.features import RFeatures
from wbFontParts.font import RFont


class TestFeatures(test_features.TestFeatures):
    objectGenerator = wbFontPartObjectGenerator

    def test_wbFontPartObjects(self):
        features, _ = self.objectGenerator("features")
        self.assertIsInstance(features, RFeatures)

        font, _ = self.objectGenerator("font")
        self.assertIsInstance(font, RFont)


if __name__ == "__main__":
    unittest.main()
