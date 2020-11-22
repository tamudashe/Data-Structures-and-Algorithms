# Given a string s, find the length of the longest substring in it with no more than k distinct characters

def longest_substring_with_k_distinct_characters(s, k):
    longest_substring = float('-inf')
    window_start = 0
    char_count = {}

    for window_end, char in enumerate(s):
        char_count[char] = char_count.get(char, 0) + 1

        while len(char_count) > k:
            start_char = s[window_start]
            char_count[start_char] -= 1

            if char_count[start_char] == 0:
                del char_count[start_char]

            window_start += 1

        longest_substring = max(longest_substring, window_end - window_start + 1)

    return longest_substring


def main():
    s = "araaci"
    k = 2
    print(longest_substring_with_k_distinct_characters(s, k))


main()
