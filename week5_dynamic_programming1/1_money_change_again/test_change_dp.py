import unittest
from change_dp import get_change


class MyTestCase(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(0, get_change(0))

    def test_1(self):
        self.assertEqual(1, get_change(1))

    def test_3(self):
        self.assertEqual(1, get_change(3))

    def test_4(self):
        self.assertEqual(1, get_change(4))

    def test_2(self):
        self.assertEqual(2, get_change(2))

    def test_6(self):
        self.assertEqual(2, get_change(6))

    def test_9(self):
        self.assertEqual(3, get_change(9))

    def test_sample_1(self):
        self.assertEqual(9, get_change(34))


if __name__ == '__main__':
    unittest.main()
