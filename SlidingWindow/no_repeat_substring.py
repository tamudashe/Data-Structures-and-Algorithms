# Given a string s, find the length of the longest substring which has no
# repeating charaters

def longest_unique(s):
    max_length = 0
    start = 0
    char_count = {}

    for end, char in enumerate(s):
        char_count[char] = char_count.get(char, 0) + 1

        while char_count[char] > 1:
            start_char = s[start]
            char_count[start_char] -= 1
            start += 1
        max_length = max(max_length, end - start + 1)

    return max_length

# Note: get the max bextwean the table[char]+1 and start
# if start is already ahead of the last index of end, we'll use start
# start indicates where we can start and there is no repeating character
# table[char] will show the last occurance of the current character
# array can also be used here instead of hashmap

def longest_unique_clean(s):
    max_length = 0
    start = 0
    table = {}

    for end, char in enumerate(s):
        if char in table:
            start = max(start, table[char] + 1)

        table[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length

def main():
    test1 = "aabccbb"
    test2 = "abbbb"
    test3 = ""
    test4 = "michaelscott"

    assert longest_unique_clean(test1) == 3
    assert longest_unique_clean(test2) == 2
    assert longest_unique_clean(test3) == 0
    assert longest_unique_clean(test4) == 8

    print("Passed all text cases!")

if __name__ == '__main__':
    main()
