# minimum window substring (76) [fast-slow]
def minimum_window_substring(S, T):
    char_frequency_table = {}
    for i in T:
        char_frequency_table[i] = char_frequency_table.get(i, 0) + 1

    result = ""
    start_window = 0
    count = len(char_frequency_table)
    minimum_length = float("inf")

    for end_window, char in enumerate(S):
        if char not in char_frequency_table:
            continue

        char_frequency_table[char] -= 1
        if char_frequency_table[char] == 0:
            count -= 1

        while count == 0:
            if (end_window - start_window) < minimum_length:
                result = S[start_window: end_window + 1]
                minimum_length = end_window - start_window

            char_start = S[start_window]
            if char_start in char_frequency_table:
                char_frequency_table[char_start] += 1
                if char_frequency_table[char_start] > 0:
                    count += 1
            start_window += 1

    return result


def main():
    S = input("String: ")
    T = input("Target: ")
    test1 = minimum_window_substring(S, T)
    print("Minimum substring: ", test1)


if __name__ == "__main__":
    main()
