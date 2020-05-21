# Given an array of positive numbers and a positive number 'S', find the length
# of the smallest contiguous subarray whose sum if greater that or equal to 'S'

# update min_length each time the window is increased or decreased

# The outer for loop runs for all elements and the inner while loop processes
# each element only once, therefore the time complexity of the algorithm
# will be O(N + N) which is asymptotically equivalent to O(N).

# O(N) time O(1) space
def smallest_subarray_with_given_sum(arr, s):
    curr_sum = 0
    start = 0
    min_length = float('inf')

    for end, num in enumerate(arr):
        curr_sum += num
        while curr_sum >= s:
            min_length = min(min_length, end - start + 1)
            curr_sum -= arr[start]
            start += 1

    if min_length == float('inf'):
        return 0

    return min_length

def main():
    arr = [3, 4, 1, 1, 6]
    s = 8
    print(smallest_subarray_with_given_sum(arr, s))

if __name__ == '__main__':
    main()
