# Given an array of integers of size 'n'. Our aim is to calculate the maximum
# sum posible for 'k' consecutive elements in the array.
def max_k_possible_sum(arr, k):
    max_sum = 0
    window_sum = 0
    for i, num in enumerate(arr):
        if i < k:
            window_sum += num
            continue
        window_sum += num - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum


def main():
    arr = [100, 200, 300, 400]
    k = 2
    maxPossibleSum =  max_k_possible_sum(arr, k)
    print(maxPossibleSum)


if __name__ == '__main__':
    main()
