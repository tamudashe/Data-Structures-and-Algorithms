# Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal
# is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type
# of fruit. Write a function to return the maximum number of fruits in both the baskets O(N + N) -> O(N)

def maximum_fruits(fruits):
    window_start = 0
    baskets = {}
    max_fruits = float('-inf')

    for window_end, fruit in enumerate(fruits):
        baskets[fruit] = baskets.get(fruit, 0) + 1

        while len(baskets) > 2:
            start_char = fruits[window_start]
            baskets[start_char] -= 1
            if baskets[start_char] == 0:
                del baskets[start_char]
            window_start += 1

        max_fruits = max(max_fruits, window_end - window_start + 1)

    return max_fruits


def main():
    fruits = ['A', 'B', 'C', 'A', 'C']
    print(maximum_fruits(fruits))


main()

# Similar problem: Longest substring with at most 2 distinct characters Given a string, find the length of the
# longest substring in it with at most two distinct characters
