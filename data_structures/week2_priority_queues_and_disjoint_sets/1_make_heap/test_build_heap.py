import unittest
from build_heap import build_heap


class MyTestCase(unittest.TestCase):

    def test_sample_1(self):
        self.assertEqual([(1, 4), (0, 1), (1, 3)], build_heap([5, 4, 3, 2, 1]))

    def test_sample_2(self):
        self.assertEqual([], build_heap([1, 2, 3, 4, 5]))


if __name__ == '__main__':
    unittest.main()
