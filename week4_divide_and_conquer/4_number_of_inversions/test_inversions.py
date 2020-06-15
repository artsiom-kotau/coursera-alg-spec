import unittest
from inversions import get_number_of_inversions


class MyTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(0, get_number_of_inversions([], [], 0, 0))

    def test_single(self):
        self.assertEqual(0, get_number_of_inversions([1], [0], 0, 1))

    def test_two_asc(self):
        self.assertEqual(0, get_number_of_inversions([1, 2], [0, 0], 0, 2))

    def test_two_desc(self):
        self.assertEqual(1, get_number_of_inversions([2, 1], [0, 0], 0, 2))

    def test_three_desc(self):
        self.assertEqual(3, get_number_of_inversions([3, 2, 1], [0, 0, 0], 0, 3))

    def test_sample(self):
        self.assertEqual(2, get_number_of_inversions([2, 3, 9, 2, 9], [0, 0, 0, 0, 0], 0, 5))

    def test_sample(self):
        self.assertEqual(15, get_number_of_inversions([9, 8, 7, 3, 2, 1], [0, 0, 0, 0, 0, 0], 0, 6))


if __name__ == '__main__':
    unittest.main()
