import unittest
import pytest
from src import utils
class PixelDataDecodeTests(unittest.TestCase):
    def test_can_decode_pixel(self):

        result = utils.decode_data_from_pixel((37, 121, 255, 1))

        expected = 0b01011101

        self.assertEqual(result, expected)
