import os
import unittest

from fontParts.test import test_font
from objectGenerator import wbFontPartObjectGenerator

from wbFontParts.font import RFont
from wbFontParts.glyph import RGlyph
from wbFontParts.guideline import RGuideline


class TestFont(test_font.TestFont):
    objectGenerator = wbFontPartObjectGenerator

    def test_wbFontPartObjects(self):
        font, _ = self.objectGenerator("font")
        self.assertIsInstance(font, RFont)

        glyph, _ = self.objectGenerator("glyph")
        self.assertIsInstance(glyph, RGlyph)

        guideline, _ = self.objectGenerator("guideline")
        self.assertIsInstance(guideline, RGuideline)

    # ------------------------------------------------------------
    # default UFOFileStructure is ZIP in wbDefcon not PACKAGE
    # ------------------------------------------------------------
    def test_save(self):
        def testCases(path):
            self.assertTrue(os.path.exists(path) and os.path.isfile(path))

        self._save(testCases)

    def test_save_fileStructure(self):
        from fontTools.ufoLib import UFOFileStructure, UFOReader

        for fileStructure in [None, "package", "zip"]:

            def testCases(path):
                reader = UFOReader(path)
                expectedFileStructure = fileStructure
                if fileStructure is None:
                    expectedFileStructure = UFOFileStructure.ZIP
                else:
                    expectedFileStructure = UFOFileStructure(fileStructure)
                self.assertEqual(reader.fileStructure, expectedFileStructure)

            self._save(testCases, fileStructure=fileStructure)


if __name__ == "__main__":
    unittest.main()
