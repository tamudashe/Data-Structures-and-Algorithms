# Given a string,
# find the length of the longest substring without repeating characters.
# store an index of when to start when we reach a certain point
def length_of_longest_substring(s):
    left_window = 0
    longest_substring = 0
    table = {}

    for right_window, char in enumerate(s):
        if char in table:
            left_window = max(left_window, table[char] + 1)
        table[char] = right_window
        longest_substring = max(longest_substring, right_window - left_window + 1)

    return longest_substring


def main():
    s = "pwwkew"
    print(length_of_longest_substring(s))


if __name__ == "__main__":
    main()
