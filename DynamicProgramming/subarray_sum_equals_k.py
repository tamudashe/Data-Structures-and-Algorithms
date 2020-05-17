# Given an array of integers and an integer k,
# you need to find the total number of continuous subarrays whose sum equals to k
# NB: just like the two-sum problem
# if the difference betwean two prefix sums is equal to the target sum, then the
# sum of the subarray betwean those points is = target sum

def subarray_sum(nums, target):
    conjugates = {}
    curr_sum = 0
    total_subarrays = 0
    for num in nums:
        curr_sum += num
        if curr_sum == target:
            total_subarrays += 1
        total_subarrays += conjugates.get(curr_sum - target, 0)
        conjugates[curr_sum] = conjugates.get(curr_sum, 0) + 1
    return total_subarrays

def max_unique_sum(nums, target):
    pass

def main():
    nums = [-1, 1, 1, 2, 1, 1, 1]
    k = 3
    print(subarray_sum(nums, k))
    print(max_unique_sum(nums, k))


if __name__ == "__main__":
    main()
