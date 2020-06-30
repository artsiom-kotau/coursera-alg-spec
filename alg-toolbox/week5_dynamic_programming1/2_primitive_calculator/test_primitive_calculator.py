import unittest
from primitive_calculator import optimal_sequence


class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual([1], optimal_sequence(1))

    def test_5(self):
        self.assertEqual([1, 2, 4, 5], optimal_sequence(5))

    def test_96234(self):
        self.assertEqual([1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234], optimal_sequence(96234))

    def test_14(self):
        self.assertEqual([1, 2, 6, 7, 14], optimal_sequence(14))

if __name__ == '__main__':
    unittest.main()
