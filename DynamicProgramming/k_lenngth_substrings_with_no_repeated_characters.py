# Suppose we have a string S, we have to find the number of substrings of length K
# where no characters are repeated.
# input: S = 'heyfriendshoareyou'  K = 5
# output: 15
# [heyfr, eyfri, yfrie, frien, riend, iends, endsh, ndsho, dshow, showa, howar,
# oware, warey, areyo, reyou]
def distinct_letter_substrings(S, K):
    total = 0
    unique_chars = 0
    seen_table = {}
    for i, char in enumerate(S):
        seen_table[char] = seen_table.get(char, 0) + 1
        if seen_table[char] == 1:
            unique_chars += 1

        if i >= K:
            start_char = S[i - K]
            seen_table[start_char] -= 1
            if seen_table[start_char] == 0:
                unique_chars -= 1

        if unique_chars == K:
            total += 1
    return total

def main():
    # test 1
    S1 = "heyfriendshowareyou"
    K1 = 5
    print(distinct_letter_substrings(S1, K1))

    # test 2
    S2 = "mynameisariripaulorighoye"
    K2 = 5
    print(distinct_letter_substrings(S2, K2))

if __name__ == '__main__':
    main()
