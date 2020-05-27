# Given an array of sorted numbers and a target sum, find a pair in the
# array whose sum is equal to the given target.
# Write a function to return the indices of the two numbers such that they
# add up to the given target

def pair_with_target_sum(nums, target_sum):
    left = 0
    right = len(nums) - 1

    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target_sum:
            return [left, right]
        elif curr_sum < target_sum:
            left += 1
        else:
            right -= 1
    return [-1, -1]

def main():
    arr = [1, 4, 6, 7, 9]
    t = 13
    print(pair_with_target_sum(arr, t))

if __name__ == '__main__':
    main()


