# Uses python3
import sys


def construct_min_operates(n):
    operates = (n+1) * [0]
    for i in range(2, n+1):
        for_minus = operates[i-1]
        for_div_2 = sys.maxsize
        for_div_3 = sys.maxsize
        if i % 3 == 0:
            for_div_3 = operates[i // 3]
        elif i % 2 == 0:
            for_div_2 = operates[i // 2]

        operates[i] = min(for_div_3, for_div_2, for_minus) + 1

    return operates


def optimal_sequence(n):
    sequence = []
    operates_amount = construct_min_operates(n)
    while n >= 1:
        sequence.append(n)
        if n % 3 != 0 and n % 2 != 0:
            n = n - 1
        elif n % 3 == 0 and n % 2 == 0:
            n = n // 3
        elif n % 3 == 0:
            if operates_amount[n - 1] < operates_amount[n // 3]:
                n = n - 1
            else:
                n = n // 3
        else:
            if operates_amount[n - 1] < operates_amount[n // 2]:
                n = n - 1
            else:
                n = n // 2
    sequence.reverse()
    return sequence


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
