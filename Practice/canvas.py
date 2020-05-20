def accum(s):
    result = []
    for i, char in enumerate(s):
        temp = [char.upper()]
        for _ in range(i):
            temp.append(char.lower())
        result.append("".join(temp))
    return "-".join(result)


def main():
    print("Result: ", accum(input("Enter a string: ")))


if __name__ == '__main__':
    main()
