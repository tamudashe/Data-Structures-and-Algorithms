"""
Given a string and a pattern, find all anagrams of the pattern in the given string.

Anagram is actually a permutation of a string. For example,
“abc” has the following six anagrams: abc acb bac bca cab cba.
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.
"""


def find_string_anagrams(text, pattern):
    window_start = 0
    matches = 0
    anagrams = []

    frequency = {}
    for char in pattern:
        frequency[char] = frequency.get(char, 0) + 1

    for window_end, char in enumerate(text):
        if char in frequency:
            frequency[char] -= 1
            if frequency[char] == 0:
                matches += 1

        if matches == len(frequency):
            anagrams.append(window_start)

        if window_end >= len(pattern) - 1:
            start_char = text[window_start]
            if start_char in frequency:
                frequency[start_char] += 1
                if frequency[start_char] == 0:
                    matches -= 1
            window_start += 1

        return anagrams


def main():
    text = "ppqp"
    pattern = "pq"
    print(find_string_anagrams(text, pattern))


if __name__ == '__main__':
    main()
