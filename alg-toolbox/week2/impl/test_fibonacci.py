from unittest import TestCase
from fibonacci import calc_fib


class Test(TestCase):
    def test_zero(self):
        self.assertEqual(0, calc_fib(1))

    def test_one(self):
        self.assertEqual(1, calc_fib(2))

    def test_six(self):
        self.assertEqual(8, calc_fib(6))

