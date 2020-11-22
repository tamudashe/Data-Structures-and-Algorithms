# Given an array, find the average of all contiguous subarrays of size 'K' in it.

def average_contiguous_subarrays(arr, k):
    result = []
    window_start = 0
    window_sum = 0

    for window_end, num in enumerate(arr):
        window_sum += num
        if window_end >= k - 1:
            result.append(window_sum/k)
            window_sum -= arr[window_start]
            window_start += 1

    return result


def main():
    test1 = [2, 4, 5, 3, 2]
    print(average_contiguous_subarrays(test1, 5))


main()
