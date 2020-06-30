import unittest
from sorting import randomized_quick_sort


class MyTestCase(unittest.TestCase):
    def test_sample_1(self):
        a = [2, 3, 9, 2, 2]
        randomized_quick_sort(a, 0, 4)
        self.assertEqual([2, 2, 2, 3, 9], a)

    def test_sample_2(self):
        a = [9, 8, 7, 6, 5, 4]
        randomized_quick_sort(a, 0, 5)
        self.assertEqual([4, 5, 6, 7, 8, 9], a)


    def test_sample_3(self):
        a = [6, 6, 6, 9, 8, 7, 6, 5, 4, 6, 6]
        randomized_quick_sort(a, 0, 10)
        self.assertEqual([4, 5, 6, 6, 6, 6, 6, 6, 7, 8, 9], a)

    def test_sample_empty(self):
        a = []
        randomized_quick_sort(a, 0, 0)
        self.assertEqual([], a)

    def test_sample_single(self):
        a = [1]
        randomized_quick_sort(a, 0, 0)
        self.assertEqual([1], a)

    def test_sample_all_eq(self):
        a = [1, 1, 1, 1, 1]
        randomized_quick_sort(a, 0, 4)
        self.assertEqual([1, 1, 1, 1, 1], a)


if __name__ == '__main__':
    unittest.main()
