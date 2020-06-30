import unittest
from fractional_knapsack import get_optimal_value

class MyTestCase(unittest.TestCase):
    def test_sample_1(self):
        self.assertEqual(180, get_optimal_value(50, [20, 50, 30], [60, 100, 120]))

    def test_sample_2(self):
        self.assertEqual(166.6667, get_optimal_value(10, [30], [500]))


if __name__ == '__main__':
    unittest.main()
