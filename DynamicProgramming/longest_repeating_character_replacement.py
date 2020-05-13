# Given a string s that consists of only uppercase English letters,
# you can perform at most k operations on that string.
# In one operation, you can choose any character of the string and change it
# to any other uppercase English character. Find the length of the longest
# sub-string containing all repeating letters you can get after performing
# the above operations.

# Notes
# in every window, get the character that is occuring the most

def characterReplacement(s, k):
    longest_substring = 0
    start_window = 0
    max_count = 0
    table = {}

    # keep moving start_window while # of replacements < k
    for end_window, char in enumerate(s):
        table[char] = table.get(char, 0) + 1
        max_count = max(max_count, table[char])
        # shrink the window until replacements < k
        while (end_window - start_window + 1) - max_count > k:
           table[s[start_window]] -= 1
           start_window += 1

        longest_substring = max(longest_substring, end_window - start_window + 1)

    return longest_substring


def main():
    s = "BAAAB"
    k = 2
    print(characterReplacement(s, k))  # 5


if __name__ == "__main__":
    main()
