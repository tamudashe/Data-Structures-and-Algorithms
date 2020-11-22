# Given an array containing 0s and 1s, if you are allowed to replace no more than 'k' 0s with 1s, find the length of
# the longest contiguous subarray of all 1s.

# Grov window up to a certain point and slide it.

def length_of_longest_subarray(arr, k):
    window_start = 0
    window_ones_count = 0
    max_window = float('-inf')

    for window_end, num in enumerate(arr):
        if num == 1:
            window_ones_count += 1

        if (window_end - window_start + 1) - window_ones_count > k:
            if arr[window_start] == 1:
                window_ones_count -= 1
            window_start += 1

        max_window = max(max_window, window_end - window_start + 1)
    return max_window


def main():
    arr = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    k = 3
    print(length_of_longest_subarray(arr, k))


main()
