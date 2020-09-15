# Given two integer arrays to represent weightd and profits of 'N'
# items, we need to find a subset of these items which will give
# us maximum profit such that their cumulative weight is not more
# than a given number 'C'. Each item can only be selected once,
# which means either we put an item in the knapsack or we skip it.

def max_profit(weights, profits, knapsack_capacity):
    pass


def main():
    weights = {2, 3, 1, 4}
    profits = {4, 5, 3, 7}
    knapsack_capacity = 5
    print(max_profit(weights, profits, knapsack_capacity))


if __name__ == '__main__':
    main()
