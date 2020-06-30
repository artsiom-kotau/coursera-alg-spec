# Uses python3
import sys
import math


def do_search(left, right, a, x):
    mid = math.ceil((right + left) / 2)
    length = right - left
    if length == 0:
        return -1
    if length == 1:
        return -1 if a[left] != x else left
    if a[mid] == x:
        return mid
    elif a[mid] < x:
        return do_search(mid + 1, right, a, x)
    else:
        return do_search(left, mid, a, x)


def binary_search(a, x):
    return do_search(0, len(a), a, x)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
