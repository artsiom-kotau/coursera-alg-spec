# Uses python3
import sys


def do_exchange(money, coins_amount):
    if coins_amount[money] != -1:
        return coins_amount[money]
    coins_amount[money] = sys.maxsize
    for coin in [4, 3, 1]:
        if coin <= money:
            amount = do_exchange(money - coin, coins_amount) + 1
            if amount < coins_amount[money]:
                coins_amount[money] = amount
    return coins_amount[money]


def get_change(m):
    if m == 0:
        return 0
    number = m + 1
    coins_amount = number * [-1]
    coins_amount[0] = 0
    for i in range(0, number):
        do_exchange(i, coins_amount)
    return coins_amount[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
