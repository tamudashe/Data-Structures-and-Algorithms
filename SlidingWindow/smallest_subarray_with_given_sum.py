# Given an array of positive numbers and a positive number 's',
# find the length of the smallest contiguous subarray whose sum is
# >= 's'.


# O(N) time O(1) space
def smallest_subarray_with_given_sum(numbers, s):
    window_start = 0
    curr_sum = 0
    min_window_size = float('inf')

    for window_end, num in enumerate(numbers):
        curr_sum += num

        while(curr_sum >= s):
            min_window_size = min(min_window_size, window_end - window_start + 1)
            curr_sum -= numbers[window_start]
            window_start += 1

    return min_window_size


def main():
    numbers = [3, 4, 1, 1, 6, 5, 10, 3, 6, 9, 7]
    s = 19
    print(smallest_subarray_with_given_sum(numbers, s))


if __name__ == '__main__':
    main()
