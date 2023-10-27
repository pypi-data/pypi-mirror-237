import re
import unittest

import drb.topics.resolver as resolver
import numpy as np
import rasterio
from drb.core.predicate import Predicate
from drb.drivers.image import DrbImageBaseNode
from drb.image import ImageAddon


class RegexNamePredicate(Predicate):
    def __init__(self, regex: str):
        super().__init__()
        self._regex = regex

    def matches(self, node) -> bool:
        return re.match(self._regex, node.name) is not None


class TestSentinel2Level1CImage(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.resource = "test/resources/S2A_MSIL1C_test.zip"
        cls.addon = ImageAddon()

    def test_available_images(self):
        zip_node = resolver.create(self.resource)
        safe_node = zip_node[0]
        images = self.addon.available_images(safe_node)
        images_names = [image[0] for image in images]
        self.assertIsNotNone(images)
        self.assertIsInstance(images, list)
        self.assertEqual(len(images), 5)
        self.assertTrue("preview" in images_names)
        self.assertTrue("TrueColorImage" in images_names)

    def test_preview_image(self):
        zip_node = resolver.create(self.resource)
        safe_node = zip_node[0]
        image = self.addon.apply(safe_node)
        addon_image_node = image.image_node()

        qi_data = safe_node["GRANULE"][0]["QI_DATA"]
        image_node = qi_data[RegexNamePredicate(".*_PVI.jp2$")][0]

        data1 = addon_image_node.get_impl(rasterio.DatasetReader).read()
        data2 = image_node.get_impl(rasterio.DatasetReader).read()
        data3 = image.get_impl(rasterio.DatasetReader).read()

        self.assertIsInstance(addon_image_node, DrbImageBaseNode)
        self.assertEqual(addon_image_node.name, image_node.name)

        np.testing.assert_array_equal(data1, data2)
        np.testing.assert_array_equal(data2, data3)

    def test_true_color_image(self):
        zip_node = resolver.create(self.resource)
        safe_node = zip_node[0]
        image = self.addon.apply(safe_node, image_name="TrueColorImage")
        addon_image_node = image.image_node()

        qi_data = safe_node["GRANULE"][0]["IMG_DATA"]
        image_node = qi_data[RegexNamePredicate(".*_TCI.jp2$")][0]

        data1 = addon_image_node.get_impl(rasterio.DatasetReader).read()
        data2 = image_node.get_impl(rasterio.DatasetReader).read()
        data3 = image.get_impl(rasterio.DatasetReader).read()

        self.assertIsInstance(addon_image_node, DrbImageBaseNode)
        self.assertEqual(addon_image_node.name, image_node.name)

        np.testing.assert_array_equal(data1, data2)
        np.testing.assert_array_equal(data2, data3)

    def test_band_image(self):
        zip_node = resolver.create(self.resource)
        safe_node = zip_node[0]
        image = self.addon.apply(
            safe_node, image_name="T31UDP_20230624T104621_B01.jp2"
        )
        addon_image_node = image.image_node()

        image_data = safe_node["GRANULE"][0]["IMG_DATA"]
        image_node = image_data["T31UDP_20230624T104621_B01.jp2"]

        data1 = addon_image_node.get_impl(rasterio.DatasetReader).read()
        data2 = image_node.get_impl(rasterio.DatasetReader).read()
        data3 = image.get_impl(rasterio.DatasetReader).read()

        self.assertIsInstance(addon_image_node, DrbImageBaseNode)
        self.assertEqual(addon_image_node.name, image_node.name)

        np.testing.assert_array_equal(data1, data2)
        np.testing.assert_array_equal(data2, data3)
