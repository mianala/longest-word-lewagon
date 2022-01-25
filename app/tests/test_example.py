# tests/test_example.py
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

from unittest import TestCase
import pylint


class TestExample(TestCase):

    def test_example(self):
        self.assertIsNotNone(pylint)
