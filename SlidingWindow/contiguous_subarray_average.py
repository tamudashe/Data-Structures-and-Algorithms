# Given an array, find the average of all contiguous subarrays of size 'K' in it.

def average_subarrays(numbers, k):
    averages = []
    window_sum = 0
    start = 0
    for i, num in enumerate(numbers):
        window_sum += num
        if i >= k - 1:
            averages.append(window_sum / k)
            window_sum -= numbers[start]
            start += 1
    return averages

def main():
    numbers = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    k = 5
    print(average_subarrays(numbers, k))

if __name__ == '__main__':
    main()
