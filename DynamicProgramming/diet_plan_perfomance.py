# A dieter consumes calories[i] calories on the i-th day.
# For every consecutive sequence of k days, they look at T, the total calories
# consumed during that sequence of k days.

# If T < lower, they performed poorly on their diet and lose 1 point;
# If T > upper, they performed well on their diet and gain 1 point
# Otherwise, they performed normally and there is no change in points.

# Return the total number of points the dieter has after all calories.length days

# Note that: The total points could be negative

def diet_plan_performance(calories, k, lower, upper):
    points = 0
    T = 0
    for i, num in enumerate(calories):
        T += num
        if i < k - 1:
            continue
        if i >= k:
            T -= calories[i - k]

        if T < lower:
            points -= 1
        elif T > upper:
            points += 1
    return points

def main():
    # test 1
    calories1 = [1, 2, 3, 4, 5]
    k1 = 1
    lower1 = 3
    upper1 = 3
    assert diet_plan_performance(calories1, k1, lower1, upper1) == 0

    # test 2
    calories2 = [3,2]
    k2 = 2
    lower2 = 0
    upper2 = 1
    assert diet_plan_performance(calories2, k2, lower2, upper2) == 1

    # test 3
    calories3 = [6, 5, 0, 0]
    k3 = 2
    lower3 = 1
    upper3 = 5
    assert diet_plan_performance(calories3, k3, lower3, upper3) == 0

    print("Passed all test cases!")

if __name__ == '__main__':
    main()
