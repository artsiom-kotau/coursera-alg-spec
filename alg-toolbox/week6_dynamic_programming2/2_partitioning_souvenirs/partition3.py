# Uses python3
import sys
import itertools

def subsetSum(S, n, a, b, c, lookup):

    # return true if subset is found
    if a == 0 and b == 0 and c == 0:
        return True

    # base case: no items left
    if n < 0:
        return False

    # construct an unique dict key from dynamic elements of the input
    key = (a, b, c, n)

    # if sub-problem is seen for the first time, solve it and
    # store its result in a dict
    if key not in lookup:

        # Case 1. current item becomes part of first subset
        A = False
        if a - S[n] >= 0:
            A = subsetSum(S, n - 1, a - S[n], b, c, lookup)

        # Case 2. current item becomes part of second subset
        B = False
        if not A and (b - S[n] >= 0):
            B = subsetSum(S, n - 1, a, b - S[n], c, lookup)

        # Case 3. current item becomes part of third subset
        C = False
        if (not A and not B) and (c - S[n] >= 0):
            C = subsetSum(S, n - 1, a, b, c - S[n], lookup)

        # return true if we get solution
        lookup[key] = A or B or C

    # return the sub-problem solution from the dictionary
    return lookup[key]


def partition3(S):
    if len(S) < 3:
        return 0

        # create a dictionary to store solutions of subproblems
    lookup = {}

    # get sum of all elements in the set
    total = sum(S)

    # return true if sum is divisible by 3 and the set can can
    # be divided into three subsets with equal sum
    result = (total % 3) == 0 and subsetSum(S, len(S) - 1, total / 3,
                                          total / 3, total / 3, lookup)

    return 1 if result else 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

