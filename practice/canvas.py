def area(length, width):
    return length * width


def fac(n):
    if n == 0 or n == 1:
        return 1
    return n * fac(n - 1)


def main():
    length = int(input("Enter the rectangle length: "))
    width = int(input("Enter the rectangle width: "))
    print("The area is {}".format(area(length, width)))

    n = int(input("Enter a non-negative integer: "))
    print("{}! = ".format(n), fac(n))


if __name__ == '__main__':
    main()
