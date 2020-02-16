# Create your tests here.
from unittest import TestCase


class SampleTest(TestCase):
    def test_something(self):
        expected = 1
        actual = 2

        self.assertEqual(expected, actual)
