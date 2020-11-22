# Given a string and a pattern, find out if the string contains any permutation of the pattern.
# Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following
# six permutations: abc, acb, bac, bca, cab, cba

def contains_permutation(text, pattern):
    window_start = 0
    match = 0

    pattern_map = {}
    for char in pattern:
        pattern_map[char] = pattern_map.get(char, 0) + 1

    for window_end, char in enumerate(text):
        if char in pattern_map:
            pattern_map[char] -= 1
            if pattern_map[char] == 0:
                match += 1

        if match == len(pattern_map):
            return True

        if window_end >= len(pattern) - 1:
            start_char = text[window_start]
            if start_char in pattern_map:
                pattern_map[start_char] += 1
                if pattern_map[start_char] == 0:
                    match -= 1
            window_start += 1

    return False


def main():
    text = "oidbcaf"
    pattern = "abc"
    print(contains_permutation(text, pattern))


main()
