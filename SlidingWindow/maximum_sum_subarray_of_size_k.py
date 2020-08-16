# Given an array of positive numbers and a positive number 'k', fimd the
# maximum sum of any contiguous subarray of size 'k'

def max_sum_subarray(numbers, k):
    max_sum = float('-inf')
    curr_sum = 0
    window_start = 0
    for window_end, num in enumerate(numbers):
        curr_sum += num
        if window_end < k - 1:
            continue
        max_sum = max(max_sum, curr_sum)
        curr_sum -= numbers[window_start]
        window_start += 1
    return max_sum


def main():
    numbers = [2, 1, 5, 1, 3, 2]
    k = 3
    print(max_sum_subarray(numbers, k))

    numbers2 = [2, 3, 4, 1, 5]
    k2 = 2
    print(max_sum_subarray(numbers2, k2))


if __name__ == '__main__':
    main()
