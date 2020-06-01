import unittest
from change import get_change

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, get_change(1))

    def test_5(self):
        self.assertEqual(1, get_change(5))

    def test_10(self):
        self.assertEqual(1, get_change(10))

    def test_4(self):
        self.assertEqual(4, get_change(4))

    def test_20(self):
        self.assertEqual(2, get_change(20))

    def test_2(self):
        self.assertEqual(2, get_change(2))

    def test_28(self):
        self.assertEqual(6, get_change(28))

if __name__ == '__main__':
    unittest.main()
