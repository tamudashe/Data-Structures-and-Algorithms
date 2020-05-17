# Leetcode 1052

# minutes = len(customers)
# customers enter every minute and all leave leave after the end of that minute
# grumpy[i] = 1 -> customers of that minute are not satisfied
# secret technique -> not grumpy for x minutes straight (can only be used once)

# return maximum number of customers that can be satisfied throughout the day.
# customers = [1,0,1,2,1,1,7,5],
# grumpy    = [0,1,0,1,0,1,0,1],
# output = 16
def maxSatisfied(customers, grumpy, X):
    satisfied = 0
    technique_satisfied  = 0
    curr_sum = 0

    for i, shoppers in enumerate(customers):
        if not grumpy[i] == 0:
            satisfied += shoppers
        else:
            curr_sum += shoppers
        if i >= X and grumpy[i - X] == 1:
            curr_sum -= customers[i - X]
        technique_satisfied = max(technique_satisfied, curr_sum)

    satisfied += technique_satisfied
    return satisfied

def main():
    customers = [1,0,1,2,1,1,7,5]
    grumpy = [0,1,0,1,0,1,0,1]
    x = 3
    print(maxSatisfied(customers, grumpy, x))

if __name__ == '__main__':
    main()

