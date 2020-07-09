# python3

from collections import deque


def max_sliding_window(sequence, k):
    maximums = []
    q_index = deque()

    for i in range(k):
        while q_index and sequence[i] >= sequence[q_index[-1]]:
            q_index.pop()
        q_index.append(i)

    for i in range(k, len(sequence)):
        maximums.append(sequence[q_index[0]])
        if q_index[0] <= i - k:
            q_index.popleft()
        while q_index and sequence[i] >= sequence[q_index[-1]]:
            q_index.pop()
        q_index.append(i)
    maximums.append(sequence[q_index[0]])
    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))

