# Create your tests here.
from unittest import TestCase

from Sample import views


class SampleTest(TestCase):
    def test_something(self):
        expected = 1
        actual = 1

        self.assertEqual(expected, actual)

    def test_get_jo_name(self):
        target_func = views.get_jo_name

        arg = '우석'

        expected = '조' + arg
        actual = target_func(arg)

        self.assertEqual(expected, actual)
