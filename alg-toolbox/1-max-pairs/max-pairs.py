# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    first_index = -1
    second_index = -1
    current_max = 0

    # if n == 2:
    #     return numbers[0] * numbers[1]

    for i in range(n):
        if current_max <= numbers[i]:
            current_max = numbers[i]
            first_index = i

    current_max = 0
    for i in range(n):
        if i != first_index and current_max <= numbers[i]:
            current_max = numbers[i]
            second_index = i

    return numbers[first_index] * numbers[second_index]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
