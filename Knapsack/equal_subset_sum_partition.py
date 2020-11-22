"""
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both
subsets is equal.
"""


def can_partition(nums):
    s = sum(nums)
    if not nums or s % 2 != 0:
        return False

    # initialize the cache array, -1 for default, 1 for True, 0 for False
    cache = [[-1 for i in range(s//2 + 1)] for j in range(len(nums))]

    if can_partition_recursive(cache, nums, s//2, 0) == 1:
        return True
    return False


def can_partition_recursive(cache, nums, target_sum, curr_index):
    # base check
    if target_sum == 0:
        return 1

    n = len(nums)
    if n == 0 or curr_index >= n:
        return 0

    # if we have not already processed a similar problem
    if cache[curr_index][target_sum] == -1:
        # recursive call after chosing the number at the current index
        # if the number at current index exceeds the sum, we will not process it
        if nums[curr_index] <= target_sum:
            if can_partition_recursive(cache, nums, target_sum - nums[curr_index], curr_index + 1):
                cache[curr_index][target_sum] = 1
                return 1

    # recursive call after excluding he number at the current index
    cache[curr_index][target_sum] = can_partition_recursive(cache, nums, target_sum, curr_index + 1)

    return cache[curr_index][target_sum]


def main():
    nums = [1, 2, 3, 4]
    print(can_partition(nums))


if __name__ == '__main__':
    main()
