import unittest

from fontParts.test import test_component
from objectGenerator import wbFontPartObjectGenerator

from wbFontParts.component import RComponent


class TestComponent(test_component.TestComponent):
    objectGenerator = wbFontPartObjectGenerator

    def test_wbFontPartObjects(self):
        component, _ = self.objectGenerator("component")
        self.assertIsInstance(component, RComponent)


if __name__ == "__main__":
    unittest.main()
