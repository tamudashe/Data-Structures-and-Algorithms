import random


def generate_random_name():
    list_name = ["Sam", "Smith", "Mathew", "Adele", "Homer", "Simposon", "Marge", "Thompson", "Liam", "Nielson"]
    first_name = random.choice(list_name)
    last_name = random.choice(list_name)

    return "{} {}".format(first_name, last_name)


def generate_burgers():
    return random.randint(1, 200)


def main():
    queue = []
    customer_data = {}

    # add customers to our queue
    for i in range(100):
        queue.append(generate_random_name())

    # assign each customer a random number of burgers
    for customer in queue:
        customer_data[customer] = customer_data.get(customer, 0) + generate_burgers()

    # sort the customers according to the number of burgers eaten
    customer_data_sorted = sorted(customer_data.items(), key=lambda x: x[1], reverse=True)

    for customer in customer_data_sorted:
        name, burgers = customer
        print("{} {}".format(name.ljust(19), burgers))


if __name__ == '__main__':
    main()
