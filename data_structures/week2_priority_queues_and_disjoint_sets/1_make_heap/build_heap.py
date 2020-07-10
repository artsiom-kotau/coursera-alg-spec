# python3


def left_child_idx(i):
    return 2*i+1


def right_child_idx(i):
    return 2*i+2


def parent_idx(i):
    return i//2


def sift_down(heap, i, swaps):
    min_index = i
    size = len(heap)
    l_child = left_child_idx(i)
    if l_child < size and heap[l_child] < heap[min_index]:
        min_index = l_child
    r_child = right_child_idx(i)
    if r_child < size and heap[r_child] < heap[min_index]:
        min_index = r_child
    if min_index != i:
        swaps.append((i, min_index))
        heap[i], heap[min_index] = heap[min_index], heap[i]
        sift_down(heap, min_index, swaps)


def build_heap(data):
    swaps = []
    for i in range(len(data)//2, -1, -1):
        sift_down(data, i, swaps)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
