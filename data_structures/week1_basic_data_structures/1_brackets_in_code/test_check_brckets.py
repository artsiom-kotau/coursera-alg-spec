import unittest
from check_brackets import find_mismatch


class MyTestCase(unittest.TestCase):
    def test_test_1(self):
        self.assertEqual(-1, find_mismatch("[]"))

    def test_test_2(self):
        self.assertEqual(-1, find_mismatch("()"))

    def test_test_3(self):
        self.assertEqual(-1, find_mismatch("{}"))

    def test_test_4(self):
        self.assertEqual(-1, find_mismatch("{}[]"))

    def test_test_5(self):
        self.assertEqual(-1, find_mismatch("{}()"))

    def test_test_6(self):
        self.assertEqual(-1, find_mismatch("[]()"))

    def test_test_7(self):
        self.assertEqual(-1, find_mismatch("[()]"))

    def test_test_8(self):
        self.assertEqual(1, find_mismatch("{"))

    def test_test_9(self):
        self.assertEqual(1, find_mismatch("}"))

    def test_test_10(self):
        self.assertEqual(6, find_mismatch("({()(})"))


if __name__ == '__main__':
    unittest.main()
