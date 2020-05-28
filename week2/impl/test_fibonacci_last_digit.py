from unittest import TestCase
from fibonacci_last_digit import get_fibonacci_last_digit


class Test(TestCase):
    def test_4(self):
        self.assertEqual(2, get_fibonacci_last_digit(4))

    def test_64(self):
        self.assertEqual(2, get_fibonacci_last_digit(64))

    def test_124(self):
        self.assertEqual(2, get_fibonacci_last_digit(124))

    def test_100(self):
        self.assertEqual(6, get_fibonacci_last_digit(100))

    def test_150(self):
        self.assertEqual(9, get_fibonacci_last_digit(150))

    def test_200(self):
        self.assertEqual(1, get_fibonacci_last_digit(200))