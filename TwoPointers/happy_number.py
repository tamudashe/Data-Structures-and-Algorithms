# Any number will be called a happy number if, after repeatedly replacing
# it with a number equal to the sum of the square of all of its digits,
# leads us to number '1'. All other (not-happy) numbers will never reach
# '1'. Instead, they will be stuck in a cycle of numbers which does not
# include '1'
def find_square_num(num):
    total = 0
    while num > 0:
        curr_digit = num % 10
        total += (curr_digit * curr_digit)
        num = num // 10
    return total

def find_happy_number(num):
    slow = num
    fast = num
    while True:
        # move one step
        slow = find_square_num(slow)
        # move two steps
        fast = find_square_num(find_square_num(fast))
        if slow == fast:
            break
    return slow == 1 # see if cycle is stuck on number '1'


def main():
    assert find_happy_number(23) == True
    assert find_happy_number(12) == False
    print("Passed all test cases!")

if __name__ == '__main__':
    main()
