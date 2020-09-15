# Given an array of positive numbers and a positive number 'k',
# find the maximum sum of any contiguous subarray of size 'k'

def max_sum_subarray(numbers, k):
    max_sum = float('-inf')
    curr_sum = 0

    for i, num in enumerate(numbers):
        curr_sum += num

        if i < k - 1:
            continue

        max_sum = max(max_sum, curr_sum)
        curr_sum = curr_sum - numbers[i - k + 1]

    return max_sum


def main():
    numbers = [2, 1, 5, 1, 3, 2]
    k = 3
    print(max_sum_subarray(numbers, k))


if __name__ == '__main__':
    main()
