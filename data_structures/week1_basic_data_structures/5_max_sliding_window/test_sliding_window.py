import unittest
from max_sliding_window import max_sliding_window

class MyTestCase(unittest.TestCase):

    def test_sample(self):
        self.assertEqual([1], max_sliding_window([1], 1))

    def test_sample_0(self):
        self.assertEqual([7], max_sliding_window([2, 7, 3, 1], 4))

    def test_sample_1(self):
        self.assertEqual([7, 8], max_sliding_window([2, 7, 8], 2))

    def test_sample_2(self):
        self.assertEqual([7, 7, 5, 6, 6], max_sliding_window([2, 7, 3, 1, 5, 2, 6, 2], 4))

    def test_sample_3(self):
        self.assertEqual([78, 90, 90, 90, 89], max_sliding_window([12, 1, 78, 90, 57, 89, 56], 3))



if __name__ == '__main__':
    unittest.main()
