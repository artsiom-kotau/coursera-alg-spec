import unittest
from car_fueling import compute_min_refills


class MyTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(2, compute_min_refills(950, 400, [200, 375, 550, 750]))

    def test_not_enough(self):
        self.assertEqual(-1, compute_min_refills(10, 3, [1, 2, 5, 9]))


if __name__ == '__main__':
    unittest.main()
