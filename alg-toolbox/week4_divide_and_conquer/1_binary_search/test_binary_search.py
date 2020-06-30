import unittest
from binary_search import binary_search

class MyTestCase(unittest.TestCase):
    def test_search_8(self):
        self.assertEqual(2, binary_search([1, 5, 8, 12, 13], 8))

    def test_search_1(self):
        self.assertEqual(0, binary_search([1, 5, 8, 12, 13], 1))

    def test_search_23(self):
        self.assertEqual(-1, binary_search([1, 5, 8, 12, 13], 23))

    def test_search_1(self):
        self.assertEqual(0, binary_search([1, 5, 8, 12, 13], 1))

    def test_search_11(self):
        self.assertEqual(-1, binary_search([1, 5, 8, 12, 13], 11))

    def test_search_4(self):
        self.assertEqual(3, binary_search([1, 2, 3, 4, 5], 4))

    def test_search_5(self):
        self.assertEqual(4, binary_search([1, 2, 3, 4, 5], 5))

    def test_search_6(self):
        self.assertEqual(-1, binary_search([1, 2, 3, 4, 5], 6))

    def test_search_0(self):
        self.assertEqual(-1, binary_search([1, 2, 3, 4, 5], 0))
if __name__ == '__main__':
    unittest.main()
