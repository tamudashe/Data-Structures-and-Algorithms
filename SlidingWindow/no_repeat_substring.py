# Given a string, find the length of the longest substring which has no repeating characters.

def non_repeat_substring(s):
    window_start = 0
    unique_chars = {}
    longest_substring = float('-inf')

    for window_end, char in enumerate(s):
        unique_chars[char] = unique_chars.get(char, 0) + 1

        while unique_chars[char] > 1:
            start_char = s[window_start]
            unique_chars[start_char] -= 1
            if unique_chars[start_char] == 0:
                del unique_chars[start_char]
            window_start += 1

        longest_substring = max(longest_substring, window_end - window_start + 1)

    return longest_substring


def non_repeat_substring_clean(s):
    window_start = 0
    longest_substring = float('-inf')
    char_position = {}

    for window_end, char in enumerate(s):
        if char in char_position:
            window_start = max(window_start, char_position[char] + 1)
        char_position[char] = window_end
        # if window_start is already ahead of the last occurance of the char at window_end
        longest_substring = max(longest_substring, window_end - window_start + 1)

    return longest_substring


def main():
    s = "abccde"
    print(non_repeat_substring(s))
    print(non_repeat_substring_clean(s))


main()
