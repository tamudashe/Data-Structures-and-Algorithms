# Write a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements
# in the array. If the sum can't be generated, the function should return 0.

def max_subset_sum_no_adjacent(array):
    if not array:
        return -1

    max_sum = 0
    prev = 0

    for i, num in enumerate(array):
        if i == 0:
            prev = num
            max_sum = num
        elif i == 1:
            prev = max_sum
            max_sum = max(num, prev)
        else:
            prev_prev = prev
            prev = max_sum
            max_sum = max(prev, prev_prev + num)

    return max_sum


def main():
    array = [7, 10, 12, 7, 9, 14]
    print(max_subset_sum_no_adjacent(array))   # 33 -> 7 + 12 + 14


if __name__ == '__main__':
    main()
