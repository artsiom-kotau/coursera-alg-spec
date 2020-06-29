# Uses python3
import sys


def optimal_weight(capacity, gold_items):
    # write your code here
    result = []
    for i in range(len(gold_items)+1):
        result.append((capacity+1) * [0])

    for gold_idx in range(1, len(gold_items)+1):
        gold_w = gold_items[gold_idx-1]
        for weight in range(1, capacity+1):
            result[gold_idx][weight] = result[gold_idx-1][weight]
            if gold_w <= weight:
                result[gold_idx][weight] = max(result[gold_idx-1][weight-gold_w] + gold_w, result[gold_idx][weight])

    return result[len(gold_items)][capacity]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
