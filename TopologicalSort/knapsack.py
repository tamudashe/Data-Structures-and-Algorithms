def knapsack(profits, weights, capacity):
    return knapsack_recursive(profits, weights, capacity, 0)


def knapsack_recursive(profits, weights, capacity, curr_index):
    # base cases
    if capacity <= 0 or curr_index >= len(profits):
        return 0

    # recursive call after choosong the element at the curr_index
    # if the weight of the element at curr_index exceeds the
    # capacity, we should not process this
    profit1 = 0
    if weights[curr_index] <= capacity:
        profit1 = profits[curr_index] + knapsack_recursive(
                profits,
                weights,
                capacity - weights[curr_index],
                curr_index + 1)

    # recursive call after excluding the element at the curr_index
    profit2 = knapsack_recursive(
            profits,
            weights,
            capacity,
            curr_index + 1)

    return max(profit1, profit2)


def main():
    print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


if __name__ == '__main__':
    main()
