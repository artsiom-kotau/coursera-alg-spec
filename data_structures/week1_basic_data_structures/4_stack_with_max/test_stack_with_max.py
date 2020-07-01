import unittest
from stack_with_max_naive import StackWithMax


class MyTestCase(unittest.TestCase):

    def test_sample_1(self):
        stack = StackWithMax()
        stack.Push(2)
        stack.Push(1)
        self.assertEqual(2, stack.Max())
        stack.Pop()
        self.assertEqual(2, stack.Max())

    def test_sample_2(self):
        stack = StackWithMax()
        stack.Push(1)
        stack.Push(2)
        self.assertEqual(2, stack.Max())
        stack.Pop()
        self.assertEqual(1, stack.Max())

    def test_sample_3(self):
        stack = StackWithMax()
        stack.Push(2)
        stack.Push(3)
        stack.Push(9)
        stack.Push(7)
        stack.Push(2)
        self.assertEqual(9, stack.Max())
        self.assertEqual(9, stack.Max())
        self.assertEqual(9, stack.Max())
        stack.Pop()
        self.assertEqual(9, stack.Max())

    def test_sample_5(self):
        stack = StackWithMax()
        stack.Push(7)
        stack.Push(1)
        stack.Push(7)
        self.assertEqual(7, stack.Max())
        stack.Pop()
        self.assertEqual(7, stack.Max())



if __name__ == '__main__':
    unittest.main()
