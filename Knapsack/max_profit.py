"""
Given two integer arrays to represent weights and profits of 'N' items, we need to find a subset of these items which
will give us maximum profit such that their cumulative weight is not more than a given number 'C'. Each item can only
be selected once, which means either we put an item in the knapsack or we skip it.
"""


# Top-down approach
def solve_knapsack(weights, profits, capacity):
    # Create a two dimentional array for Memoization, each element is initialized to '-1'
    cache = [[-1 for i in range(capacity+1)] for j in range(len(profits))]
    return max_profit(cache, weights, profits, capacity, 0)


def max_profit(cache, weights, profits, capacity, curr_index):
    # Base cases
    if capacity <= 0 or curr_index >= len(profits):
        return 0

    # If we have already solved a similar problem, return the result from memory
    if cache[curr_index][capacity] != -1:
        return cache[curr_index][capacity]

    # Recursive call after choosing the element at the current index. If the weight of the element at the current
    # index exceeds the capacity, we shouldn't process it.
    profit_a = 0
    if weights[curr_index] <= capacity:
        profit_a = profits[curr_index] + max_profit(cache, weights, profits, capacity - weights[curr_index], curr_index + 1)

    # Recursive call after excluding the element at current index
    profit_b = max_profit(cache, weights, profits, capacity, curr_index + 1)

    cache[curr_index][capacity] = max(profit_a, profit_b)
    return cache[curr_index][capacity]


def print_selected_items(cache, weights, profits, capacity):
    print("The selected items are: ", end='')
    n = len(weights)
    total_profit = cache[n - 1][capacity]

    for i in range(n-1, 0, -1):
        if total_profit != cache[i - 1][capacity]:
            print(str(weights[i]) + " ", end='')
            capacity -= weights[i]
            total_profit -= profits[i]

    if total_profit != 0:
        print(str(weights[0]) + " ", end='')

    print()


# Bottom-up approach: Time complexity O(n*c)
def get_max_profit(weights, profits, capacity):
    # Basic checks
    n = len(profits)
    if capacity <= 0 or not profits or len(weights) != n:
        return 0

    cache = [[0 for i in range(capacity + 1)] for j in range(n)]

    # Populate the capacity = 0 columns: with '0' capacity we have '0' profit
    for i in range(0, n):
        cache[i][0] = 0

    # If we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity+1):
        if weights[0] <= c:
            cache[0][c] = profits[0]

    # Process all subarrays for all capacities
    for i in range(1, n):
        for c in range(1, capacity+1):
            profit_a = 0

            # Include the item if it is not more than the capacity
            if weights[i] <= c:
                profit_a = profits[i] + cache[i - 1][c - weights[i]]

            # Exclude the item
            profit_b = cache[i - 1][c]

            # Take maximum
            cache[i][c] = max(profit_a, profit_b)

    print_selected_items(cache, weights, profits, capacity)

    # The maximum profit will be at the bottom right corner
    return cache[n - 1][capacity]


def main():
    weights = [1, 2, 3, 5]
    profits = [1, 6, 10, 16]
    knapsack_capacity = 7
    # print(solve_knapsack(weights, profits, knapsack_capacity))  # 22
    print(get_max_profit(weights, profits, knapsack_capacity))  # 22


if __name__ == '__main__':
    main()
