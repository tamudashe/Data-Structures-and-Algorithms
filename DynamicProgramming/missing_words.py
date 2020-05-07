# given two strings, s and t, where t is a subsequence of s, report the words
# of s, missing in t (case sensitive), in the order they are missing
def missing_words(s, t):
    missing_words_array = []
    t_list =  t.split()
    pointer = 0

    for word in s.split():
        if pointer < len(t_list) and word == t_list[pointer]:
            pointer += 1
        else:
            missing_words_array.append(word)
    return missing_words_array


def main():
    s = input("s: ")
    t = input("t: ")
    print(missing_words(s, t))


if __name__ == "__main__":
    main()
