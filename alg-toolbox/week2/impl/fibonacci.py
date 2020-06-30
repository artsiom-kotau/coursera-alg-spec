# Uses python3
def calc_fib(n):

    sum = 0
    previous = 0
    current  = 1

    for _ in range(n-1):
        sum, previous, current = previous + current, current, previous + current

    return sum

if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))
