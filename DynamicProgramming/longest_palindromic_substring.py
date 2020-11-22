"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

O(n^2)
"""


def expand_from_middle(text, left, right):
    if not text or left >= right:
        return 0

    while left >= 0 and right < len(text) and text[left] == text[right]:
        left -= 1
        right += 1
    return right - left - 1


def longest_palindromic_substring(s):
    if not s:
        return ""

    start = 0
    end = 0

    for i, char in enumerate(s):
        len_a = expand_from_middle(s, i, i)
        len_b = expand_from_middle(s, i, i + 1)
        curr_longest = max(len_a, len_b)

        if curr_longest > (end - start):
            start = i - (curr_longest - 1)//2
            end = i + (curr_longest - 1)//2

    return s[start: end + 1]


def main():
    s = "babad"
    print(longest_palindromic_substring(s))  # bab


if __name__ == '__main__':
    main()
