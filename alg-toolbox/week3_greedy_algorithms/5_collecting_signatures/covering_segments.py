# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def sort_key(x):
    return x.end


def optimal_points(segments):
    points = []
    segments.sort(key=sort_key)
    point = segments[0].end
    points.append(point)

    for i in range(1, len(segments)):
        if segments[i].start > point or segments[i].end < point:
            point = segments[i].end
            points.append(point)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
