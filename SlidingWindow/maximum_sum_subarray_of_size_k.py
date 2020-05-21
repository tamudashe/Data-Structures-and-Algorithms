# Given an array of positive numbers and a positive number 'k', fimd the
# maximum sum of any contiguous subarray of size 'k'

def max_sum_subarray(numbers, k):
    curr_sum = 0
    curr_max = 0
    start = 0
    for end, num in enumerate(numbers):
        curr_sum += num
        if end >= k - 1:
            curr_max = max(curr_max,curr_sum)
            curr_sum -= numbers[start]
            start += 1
    return curr_max

def main():
    numbers = [2, 3, 4, 1, 5]
    k = 5
    print(max_sum_subarray(numbers, k))

if __name__ == '__main__':
    main()
