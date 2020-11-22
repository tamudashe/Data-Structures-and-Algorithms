# Given an array of positive numbers and a positive number 'k', find the maximum sum of any contiguous subarray of
# size 'k'

def max_sum_subarray(numbers, k):
    curr_window_sum = 0
    window_start = 0
    max_sum = 0

    for window_end, num in enumerate(numbers):
        curr_window_sum += num
        if window_end >= k - 1:
            max_sum = max(max_sum, curr_window_sum)
            curr_window_sum -= numbers[window_start]
            window_start += 1

    return max_sum


def main():
    numbers = [2, 1, 5, 1, 3, 2]
    k = 3
    print(max_sum_subarray(numbers, k))


main()
