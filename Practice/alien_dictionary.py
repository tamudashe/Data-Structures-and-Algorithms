def is_alien_sorted(words, order):
    lex = {}
    for i, char in enumerate(order):
        lex[char] = i

    for i, second in enumerate(words):
        if i == 0:
            continue
        first = words[i - 1]
        i = 1
        for f_char, s_char in zip(first, second):
            if lex[f_char] < lex[s_char]:
                break
            elif lex[f_char] > lex[s_char]:
                return False
            elif i == len(second) and len(first) > len(second):
                return False
            i += 1
    return True

def main():
    words = ["apap", "app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    print(is_alien_sorted(words, order))

if __name__ == '__main__':
    main()
