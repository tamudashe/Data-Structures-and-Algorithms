# Given an array, find the average of all contiguous subarrays of size 'K' in it.

def average_subarrays_bruit_force(numbers, k):
    result = []
    arr_size = len(numbers)
    for i in range(arr_size - k + 1):
        curr_sum = 0
        for j in range(k):
            curr_sum += numbers[i + j]
        result.append(curr_sum/5)
    return result


def average_subarrays(numbers, k):
    curr_sum = 0
    window_start = 0
    averages = []

    for window_end, num in enumerate(numbers):
        curr_sum += num
        if window_end < k - 1:
            continue
        averages.append(curr_sum/k)
        curr_sum -= numbers[window_start]
        window_start += 1

    return averages


def main():
    numbers = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    k = 5
    print(average_subarrays_bruit_force(numbers, k))
    print(average_subarrays(numbers, k))

if __name__ == '__main__':
    main()
