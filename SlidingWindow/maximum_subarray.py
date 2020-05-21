# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.

# Note: use Kadane's algorithm
# Look at each index and look at the maximum sum ending at that index
# at each point, either continue the subarray or start a new one

def max_subarray(nums):
    curr_max = float('-inf')
    max_sum = float('-inf')
    for num in nums:
        curr_max = max(num, curr_max + num)
        max_sum = max(max_sum, curr_max)
    return max_sum

def main():
    nums = [-2, 1, -3, 4, -2, 1, -5, 4]
    print(max_subarray(nums))

if __name__ == '__main__':
    main()
