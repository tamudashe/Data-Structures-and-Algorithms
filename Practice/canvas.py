# python dictionaries
from collections import defaultdict


def python_dictionaries():
    name = "tamudashe"
    chars = defaultdict(lambda: 0)
    for char in name:
        chars[char] += 1
    print(dict(chars))
    return chars


def main():
    python_dictionaries()


if __name__ == '__main__':
    main()
