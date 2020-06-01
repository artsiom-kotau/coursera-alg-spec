# Uses python3
import sys


class ValueWeight:

    value = 0
    weight = 0
    value_per_weight = 0

    def decrease_value(self):
        if self.value > 0:
            self.value -= self.value_per_weight

    def decrease_weight(self):
        if self.weight > 0:
            self.weight -= 1


def get_optimal_value(capacity, weights, values):
    value = 0.
    value_per_weight = []

    for i in range(len(weights)):
        item = ValueWeight()
        item.value = values[i]
        item.weight = weights[i]
        item.value_per_weight = values[i]/weights[i]
        value_per_weight.append(item)
    value_per_weight.sort(key=lambda it: it.value_per_weight, reverse=True)

    i = 0
    while capacity > 0 and i < len(value_per_weight):
        item = value_per_weight[i]
        if item.weight > 0 and capacity > 0:
            capacity -= 1
            value += item.value_per_weight
            item.decrease_value()
            item.decrease_weight()
        else:
            i += 1
    return round(value, 4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
