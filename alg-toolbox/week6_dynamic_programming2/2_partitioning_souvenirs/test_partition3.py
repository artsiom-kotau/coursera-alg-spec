import unittest
from partition3 import partition3

class MyTestCase(unittest.TestCase):

    def test_sample_1(self):
        self.assertEqual(0, partition3([3, 3, 3, 3]))

    def test_sample_2(self):
        self.assertEqual(0, partition3([40]))

    def test_sample_3(self):
        self.assertEqual(1, partition3([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]))

    def test_sample_4(self):
        self.assertEqual(1, partition3([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]))

    def test_sample_5(self):
        self.assertEqual(1, partition3([1, 1, 1, 2, 2, 3, 3, 4, 6, 7]))


if __name__ == '__main__':
    unittest.main()
