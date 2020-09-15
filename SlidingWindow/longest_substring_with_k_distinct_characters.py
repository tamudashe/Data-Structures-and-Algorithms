# Given a string s, find the length of the longest substring in it
# with no more than k distinct characters

def longest_substring_with_k_distinct_characters(s, k):
    char_counter = {}
    window_start = 0
    longest_substring = float('-inf')

    for window_end, char in enumerate(s):
        char_counter[char] = char_counter.get(char, 0) + 1

        while len(char_counter) > k:
            start_char = s[window_start]
            char_counter[start_char] -= 1
            if char_counter[start_char] == 0:
                del char_counter[start_char]
            window_start += 1

        longest_substring = max(longest_substring, window_end - window_start + 1)

    return longest_substring


def main():
    s = "aaahhibc"
    k = 2
    print(longest_substring_with_k_distinct_characters(s, k))


if __name__ == "__main__":
    main()
