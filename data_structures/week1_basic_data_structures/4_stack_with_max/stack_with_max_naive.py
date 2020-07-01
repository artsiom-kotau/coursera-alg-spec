#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__stack_prev_max = []
        self.__current_max = None

    def Push(self, a):
        self.__stack.append(a)
        if self.__current_max is None:
            self.__current_max = a
        elif self.__current_max <= a:
            self.__stack_prev_max.append(self.__current_max)
            self.__current_max = a



    def Pop(self):
        assert(len(self.__stack))
        value = self.__stack.pop()
        if value == self.__current_max:
            self.__current_max = self.__stack_prev_max.pop()

    def Max(self):
        return self.__current_max


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
