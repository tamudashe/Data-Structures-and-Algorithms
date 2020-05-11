# Given an array of integers and an integer k,
# you need to find the total number of continuous subarrays whose sum equals to k
# NB: just like the two-sum problem
# if the difference betwean two prefix sums is equal to the target sum, then the
# sum of the subarray betwean those points is = target sum

def subarray_sum(arr, target_sum):
    prefix_sum_table = {}
    prefix_sum = 0
    total_subarrays = 0
    for num in arr:
        prefix_sum += num
        if prefix_sum == target_sum:
            total_subarrays += 1
        if prefix_sum - target_sum in prefix_sum_table:
            total_subarrays += prefix_sum_table.get(prefix_sum - target_sum)
        prefix_sum_table[prefix_sum] = prefix_sum_table.get(prefix_sum, 0) + 1
    return total_subarrays


def main():
    arr = [0, 0, 0, 0, 0, 0]
    k = 0
    print(subarray_sum(arr, k))


if __name__ == "__main__":
    main()
