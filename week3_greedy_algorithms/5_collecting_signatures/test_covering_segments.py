import unittest
from covering_segments import optimal_points
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


class MyTestCase(unittest.TestCase):
    def test_sample_1(self):
        self.assertEqual([3], optimal_points([Segment(1, 3), Segment(2, 5), Segment(3, 6)]))

    def test_sample_2(self):
        self.assertEqual([3, 6], optimal_points([Segment(4, 7), Segment(1, 3), Segment(2, 5), Segment(5, 6)]))


if __name__ == '__main__':
    unittest.main()
