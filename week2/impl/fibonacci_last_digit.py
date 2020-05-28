# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):

    new_n = n % 60

    if new_n <= 1:
        return new_n

    previous = 0
    current  = 1

    for _ in range(new_n):
        previous, current = current, previous + current

    return new_n % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
