# Given an array of positive numbers and a positive number 'S', find the length
# of the smallest contiguous subarray whose sum if greater that or equal to 'S'

# update min_length each time the window is increased or decreased

# The outer for loop runs for all elements and the inner while loop processes
# each element only once, therefore the time complexity of the algorithm
# will be O(N + N) which is asymptotically equivalent to O(N).

# O(N) time O(1) space
def smallest_subarray_with_given_sum(numbers, s):
    window_start = 0
    curr_sum = 0
    smallest_target_subarray = float('inf')

    for window_end, num in enumerate(numbers):
        curr_sum += num

        while curr_sum > s:
            smallest_target_subarray = min(smallest_target_subarray, window_end - window_start)
            curr_sum -= numbers[window_start]
            window_start += 1

    if smallest_target_subarray == float('inf'):
        return 0

    return smallest_target_subarray

def main():
    numbers = [3, 4, 1, 1, 6]
    s = 60
    print(smallest_subarray_with_given_sum(numbers, s))

if __name__ == '__main__':
    main()
