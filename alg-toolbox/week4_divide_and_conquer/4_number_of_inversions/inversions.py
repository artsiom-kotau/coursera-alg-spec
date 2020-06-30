# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    left_i = left
    right_i = ave
    b_i = left

    while left_i < ave and right_i < right:
        if a[left_i] <= a[right_i]:
            b[b_i] = a[left_i]
            left_i, b_i = left_i + 1, b_i + 1
        elif a[left_i] > a[right_i]:
            b[b_i] = a[right_i]
            number_of_inversions += (ave - left_i)
            right_i, b_i = right_i + 1, b_i + 1

    for i in range(left_i, ave):
        b[b_i] = a[i]
        b_i += 1

    for i in range(right_i, right):
        b[i] = a[i]
        b_i += 1

    for i in range(left, right):
        a[i] = b[i]

    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
