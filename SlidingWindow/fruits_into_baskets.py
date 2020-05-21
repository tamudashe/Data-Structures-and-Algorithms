# Given an array of characters where each character represents a fruit tree, you
# are given two baskets and your goal is to put maximum number of fruits in each
# in each basket. The only restriction is that each basket can have only one type
# of fruit.

# Write a function to return the maximum number of fruits in both the baskets
# O(N + N) -> O(N)

def maximum_fruits(fruits):
    total = 0
    start = 0
    frequency = {}

    for end, f_type in enumerate(fruits):
        frequency[f_type] = frequency.get(f_type, 0) + 1
        while len(frequency) > 2:
            start_fruit = fruits[start]
            frequency[start_fruit] -= 1
            if frequency[start_fruit] == 0:
                del frequency[start_fruit]
            start += 1
        total = max(total, end - start + 1)
    return total

def main():
    test1 = ['A', 'B', 'C', 'A', 'C']
    test2 = ['A', 'B', 'C', 'B', 'B', 'C']
    assert maximum_fruits(test1) == 3
    assert maximum_fruits(test2) == 5
    print("Passed all test cases!")

if __name__ == '__main__':
    main()

# Similar problem:
# Longest substring with at most 2 distinct characters
# Given a string, find the length of the longest substring in it with at most two
# distinct characters
