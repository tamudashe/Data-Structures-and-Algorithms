# Given a string,
# find the length of the longest substring without repeating characters.
def length_of_longest_substring(s):
    start_window = 0
    longest_sub_len = 0
    table = {}

    for end_window, char in enumerate(s):
        if char in table:
            start_window = max(start_window, table[char] + 1)
        table[char] = end_window
        longest_sub_len = max(longest_sub_len, end_window - start_window + 1)

    return longest_sub_len


def main():
    s = "pwwkew"
    print(length_of_longest_substring(s))


if __name__ == "__main__":
    main()
