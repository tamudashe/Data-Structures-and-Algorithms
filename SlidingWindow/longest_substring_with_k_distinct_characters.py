# Given a string s, find the length of the longest substring in it with no more than
# k distinct characters

# Only use del dictionary[key] if the key is guaranteed to exist
# else use dictionary.pop(key, None)

from collections import defaultdict

def longest_substring_with_k_distinct_characters(s, k):
    window_start = 0
    char_frequency = defaultdict(int)
    max_length = 0

    for window_end, char in enumerate(s):
        char_frequency[char] += 1

        while len(char_frequency) > k:
            start_char = s[window_start]
            char_frequency[start_char] -= 1
            if char_frequency[start_char] == 0:
                del char_frequency[start_char]
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def main():
    s = "cbbebi"
    k = 3
    print(longest_substring_with_k_distinct_characters(s, k))

if __name__ == "__main__":
    main()
