import unittest
from dot_product import max_dot_product


class MyTestCase(unittest.TestCase):
    def test_single(self):
        self.assertEqual(897, max_dot_product([23], [39]))

    def test_with_negative(self):
        self.assertEqual(23, max_dot_product([1, 3, -5], [-2, 4, 1]))


if __name__ == '__main__':
    unittest.main()
