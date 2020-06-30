# python3
import sys


def compute_min_refills(distance, tank, stops):
    stop_amount = 0
    last_fuel = 0
    impossible = False
    stops.append(distance)
    i = 0
    while i < len(stops)-1 and not impossible:
        if stops[i+1] - last_fuel > tank:
            last_fuel = stops[i]
            stop_amount += 1
        impossible = stops[i + 1] - last_fuel > tank
        i += 1

    return -1 if impossible else stop_amount

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
