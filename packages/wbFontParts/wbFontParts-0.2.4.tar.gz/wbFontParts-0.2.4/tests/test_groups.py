import unittest

from fontParts.test import test_groups
from objectGenerator import wbFontPartObjectGenerator

from wbFontParts.font import RFont
from wbFontParts.groups import RGroups


class TestGroups(test_groups.TestGroups):
    objectGenerator = wbFontPartObjectGenerator

    def test_wbFontPartObjects(self):
        font, _ = self.objectGenerator("font")
        self.assertIsInstance(font, RFont)

        groups, _ = self.objectGenerator("groups")
        self.assertIsInstance(groups, RGroups)


if __name__ == "__main__":
    unittest.main()
