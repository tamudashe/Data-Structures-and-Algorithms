# Given a string 's' with lowercase letters only, if you are allowed to replace
# 'k' letters with any letter, find the length of the longest substring having the
# same letters after replacement

# end - start + 1 -> length of current window
# at each index: what is the maximum repeating, check if we have used up k

def length_of_longest_substring(s, k):
    max_length = 0
    max_repeating = 0
    start = 0
    table = {}

    for end, char in enumerate(s):
        table[char] = table.get(char, 0) + 1
        max_repeating = max(max_repeating, table[char])

        if (end - start + 1 - max_repeating) > k:
            start_char = s[start]
            table[start_char] -= 1
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length

def main():
    s1 = "aabccbb"
    k1 = 2

    s2 = "abbcb"
    k2 = 1

    s3 = "abccde"
    k3 = 1

    assert length_of_longest_substring(s1, k1) == 5
    assert length_of_longest_substring(s2, k2) == 4
    assert length_of_longest_substring(s3, k3) == 3

    print("Passed all test cases")

if __name__ == '__main__':
    main()
