# Given an array nums, there is a sliding window of size k which is moving
# from the very left of the array to the very right.
# You can only see the k numbers in the window.
# Each time the sliding window moves right by one position.
# Return the max sliding window.
from collections import deque


def sliding_window_maximum_bruteForce(nums, k):
    result = []
    for i in range(len(nums) + 1):
        if i < k:
            continue
        curr_max = float("-inf")
        for j in range(i - k, i):
            curr_max = max(curr_max, nums[j])
        result.append(curr_max)
    return result


def sliding_window_maximum_deque(nums, k):
    result = []
    # an element is only usefull if it is in the current window and is
    # greater than all the other elements on the left side of it in curr window
    # maintain the usefull elements in sorted order
    # element at front (left) of queue is the largest in current window
    # element at back (right) of queue is the smallest in current window
    # store index of usefull element
    dq = deque()

    for i, num in enumerate(nums):
        if i < k:
            # for every element the previous smaller elements are useless
            while dq and num >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            continue

        # element at front of queue is the largest element of previous window
        result.append(nums[dq[0]])

        # remove elements out of the current window
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and num >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)
    result.append(nums[dq[0]])
    return result


def main():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(sliding_window_maximum_bruteForce(nums, k)) # [3,3,5,5,6,7]

    print(sliding_window_maximum_deque(nums, k)) # [3,3,5,5,6,7]

if __name__ == "__main__":
    main()
