import copy

def min_eating_speed(piles, H):
    def canEatAll(time):
        return sum((p+time-1)//time for p in piles) <= H

    l = 1
    h = max(piles)
    while l<h:
        m = (l+h)//2
        if canEatAll(m):
            h = m
        else:
            l = m+1
    return l




# test cases
piles = [4,9,11,17]
h = 8
print(min_eating_speed(piles, h))
