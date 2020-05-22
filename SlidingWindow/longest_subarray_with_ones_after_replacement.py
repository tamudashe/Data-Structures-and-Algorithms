# Given an array containing 0s and 1s, if you are allowed to replace no more than
# 'k' 0s with 1s, find the length of the longest contiguous subarray of all 1s

# When the replacements we have made is equal to k, start moving the start pointer
# with the end pointer until we eliminate one zero

def length_of_longest_subarray_alternative(arr, k):
    max_length = 0
    start = 0
    replacements = 0

    for end, num in enumerate(arr):
        if num == 0:
            replacements += 1
        if replacements > k:
            if arr[start] == 0:
                replacements -= 1
            start += 1
        max_length = max(max_length, end - start + 1)

    return max_length

def length_of_longest_subarray(arr, k):
    max_length = 0
    start = 0
    curr_ones_count = 0

    for end, num in enumerate(arr):
        if num == 1:
            curr_ones_count += 1

        if (end - start + 1 - curr_ones_count) > k:
            if arr[start] == 1:
                curr_ones_count -= 1
            start += 1

        max_length = max(max_length, end - start + 1)
    return max_length

def main():
    arr1 = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
    k1 = 2

    arr2 = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    k2 = 3

    assert length_of_longest_subarray(arr1, k1) == 6
    assert length_of_longest_subarray(arr2, k2) == 9

    print("Passed all test cases!")

if __name__ == '__main__':
    main()
