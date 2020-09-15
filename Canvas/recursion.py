# Recursion occurs when a function calls itself firectly or
# indirectly

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def main():
    print(factorial(5))


if __name__ == '__main__':
    main()
