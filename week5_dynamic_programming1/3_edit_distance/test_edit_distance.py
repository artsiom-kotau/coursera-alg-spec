import unittest
from edit_distance import edit_distance


class MyTestCase(unittest.TestCase):

    def test_single_same(self):
        self.assertEqual(0, edit_distance('a', 'a'))

    def test_single_diff(self):
        self.assertEqual(1, edit_distance('a', 'b'))

    def test_sample_1(self):
        self.assertEqual(0, edit_distance('ab', 'ab'))

    def test_sample_2(self):
        self.assertEqual(3, edit_distance('short', 'ports'))

    def test_sample_3(self):
        self.assertEqual(5, edit_distance('editing', 'distance'))

if __name__ == '__main__':
    unittest.main()
