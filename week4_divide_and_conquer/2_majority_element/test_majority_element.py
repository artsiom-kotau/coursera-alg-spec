import unittest
from majority_element import get_majority_element


class MyTestCase(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(-1, get_majority_element([], 0, 0))

    def test_single(self):
        self.assertEqual(2, get_majority_element([2], 0, 1))

    def test_two_diff(self):
        self.assertEqual(-1, get_majority_element([2, 1], 0, 2))

    def test_two_same(self):
        self.assertEqual(4, get_majority_element([4, 4], 0, 2))

    def test_sample_1(self):
        self.assertEqual(2, get_majority_element([2, 3, 9, 2, 2], 0, 5))

    def test_sample_2(self):
        self.assertEqual(-1, get_majority_element([1, 2, 3, 4], 0, 4))

    def test_sample_3(self):
        self.assertEqual(-1, get_majority_element([1, 2, 3, 1], 0, 4))

if __name__ == '__main__':
    unittest.main()
