# Given an array of distinct positive integers representing  coin denominations and a single non-negative integer n
# representing the target amount of money, write a function that returns the number of ways to make change for that
# amount using the given coin denominations. Note → an unlimited amount of coins is at your disposal.

def num_ways_to_make_change(coins, change):
    ways = [0 for i in range(change + 1)]
    # base case: there is only one way to make change of $0 which is not using any coins
    ways[0] = 1

    for coin in coins:
        for amount in range(1, change+1):
            if coin <= amount:
                ways[amount] += ways[amount - coin]

    return ways[change]


def main():
    coins = [1, 5, 10, 25]
    n = 10
    print(num_ways_to_make_change(coins, n))  # num_ways = 4: (1*10), (2*5), (1*5 + 5*1), (10*1)


if __name__ == '__main__':
    main()
