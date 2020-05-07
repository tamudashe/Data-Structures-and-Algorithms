# find the longest substring with k distinct characters
def longest_substring(arr, k):
    char_frequency_table = {}
    max_length = 0
    window_start = 0

    for window_end, char in enumerate(arr):
        char_frequency_table[char] = char_frequency_table.get(char, 0) + 1

        while len(char_frequency_table) > k:
            start_char = arr[window_start]
            char_frequency_table[start_char] -= 1
            if char_frequency_table[start_char] == 0:
                char_frequency_table.pop(start_char)
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length



def main():
    arr = ['A', 'A', 'A', 'H', 'H', 'I', 'B', 'C']
    k = 2
    print(longest_substring(arr, k))


if __name__ == "__main__":
    main()
