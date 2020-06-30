# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    mid = (right + left) // 2
    left_major = get_majority_element(a, left, mid)
    right_major = get_majority_element(a, mid, right)

    left_major_count = 0
    right_major_count = 0
    for i in range(left, right):
        if a[i] == left_major:
            left_major_count += 1
        if a[i] == right_major:
            right_major_count += 1
    major = (right - left) / 2

    if left_major_count > major:
        return left_major

    if right_major_count > major:
        return right_major
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
