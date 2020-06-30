import unittest
from knapsack import optimal_weight


class MyTestCase(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(9, optimal_weight(10, [1, 4, 8]))


if __name__ == '__main__':
    unittest.main()
