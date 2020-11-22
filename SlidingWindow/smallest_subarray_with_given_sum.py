# Given an array of positive numbers and a positive number 's', find the length of the smallest contiguous subarray
# whose sum is >= 's'.

# O(N) time O(1) space
def smallest_subarray_with_given_sum(numbers, s):
    smallest_subarray = float("inf")
    window_start = 0
    curr_window_sum = 0

    for window_end, num in enumerate(numbers):
        curr_window_sum += num
        while curr_window_sum >= s:
            smallest_subarray = min(smallest_subarray, window_end - window_start + 1)
            curr_window_sum -= numbers[window_start]
            window_start += 1

    if smallest_subarray == float("inf"):
        return 0

    return smallest_subarray


def main():
    numbers = [2, 1, 5, 2, 3, 2]
    s = 10
    print(smallest_subarray_with_given_sum(numbers, s))


main()
