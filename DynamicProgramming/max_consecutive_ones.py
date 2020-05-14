# Given an array A of 0s and 1s, we may change up to K values from 0 to 1
# Return the length of the longest(contiguous) subarray that contains only 1s.

def longestOnes(A, K):
    longest_ones = 0
    start_window = 0
    replacements = 0

    for end_window, num in enumerate(A):
        if num == 0:
            replacements += 1
        while replacements > K:
            if A[start_window] == 0:
                replacements -= 1
            start_window += 1
        longest_ones = max(longest_ones, end_window - start_window + 1)
    return longest_ones

def main():
    A = [1,1,1,0,0,0,1,1,1,1,0]
    K = 2
    print(longestOnes(A, K))  # 6


if __name__ == "__main__":
    main()
