# Given a string 's' with lowercase letters only, if you are allowed to replace 'k' letters with any letter,
# find the length of the longest substring having the same letters after replacement.

# Grow window up to a certain point and slide it.

def length_of_longest_substring(s, k):
    window_start = 0
    char_frequency = {}
    max_repeat_letter_count = float('-inf')
    max_length = float('-inf')

    for window_end, char in enumerate(s):
        char_frequency[char] = char_frequency.get(char, 0) + 1
        # get the current maximum repeating character in the window
        max_repeat_letter_count = max(max_repeat_letter_count, char_frequency[char])

        if (window_end - window_start + 1) - max_repeat_letter_count > k:
            start_char = s[window_start]
            char_frequency[start_char] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    test = "aabccbb"
    k = 2
    print(length_of_longest_substring(test, k))


main()
