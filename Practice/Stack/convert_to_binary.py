from stack import Stack


def convert_to_binary(num):
    bin_stack = Stack()
    bin_num = 0

    while num > 0:
        bin_stack.push(num % 2)
        num = num // 2

    while not bin_stack.is_empty():
        bin_num = bin_num * 10
        bin_num += bin_stack.pop()

    return bin_num


def main():
    num = 242
    print(convert_to_binary(num))


if __name__ == '__main__':
    main()
