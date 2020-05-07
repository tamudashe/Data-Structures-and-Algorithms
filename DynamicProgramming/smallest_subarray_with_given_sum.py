# find the smallest subarray with given sum
def smallest_subarray(arr, target_sum):
    window_start = 0
    curr_window_sum = 0
    min_window_size = float("inf")

    for window_end, num in enumerate(arr):
        curr_window_sum += num
        while curr_window_sum >= target_sum:
            min_window_size = min(min_window_size, window_end - window_start + 1)
            curr_window_sum -= arr[window_start]
            window_start += 1

    return min_window_size


def main():
    arr = [4, 2, 2, 7, 8, 1, 2, 8, 1, 0]
    target_sum = 8
    print(smallest_subarray(arr, target_sum))


if __name__ == "__main__":
    main()
