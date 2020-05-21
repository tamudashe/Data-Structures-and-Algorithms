# Given a string s, find the length of the longest substring in it with no more than
# k distinct characters

# Only use del dictionary[key] if the key is guaranteed to exist
# else use dictionary.pop(key, None)

def longest_substring_with_k_distinct_characters(s, k):
    max_length = 0
    start = 0
    char_frequency = {}

    for end, char in enumerate(s):
        char_frequency[char] = char_frequency.get(char, 0) + 1

        while len(char_frequency) > k:
            start_char = s[start]
            char_frequency[start_char] -= 1
            if char_frequency[start_char] == 0:
                del char_frequency[start_char]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length

def main():
    s = "araaci"
    k = 2
    print(longest_substring_with_k_distinct_characters(s, k))

if __name__ == "__main__":
    main()
