# user never interfaces with this Node class
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # head node will not be indexable, user cannot interface with this node
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        curr_node = self.head
        new_node.next = curr_node.next
        curr_node.next = new_node

    def insert_after_node(self, data, index):
        new_node = Node(data)
        curr_node = self.head
        curr_index = 0
        while curr_node.next:
            curr_node = curr_node.next
            if curr_index == index:
                new_node.next = curr_node.next
                curr_node.next = new_node
                break
            curr_index += 1

    def delete_node(self, position):
        curr_node = self.head
        curr_index = 0
        while curr_node.next:
            if curr_index == position:
                curr_node.next = curr_node.next.next
                break
            curr_node = curr_node.next
            curr_index += 1

    def swap_nodes(self, key1, key2):
        curr_node1 = self.head
        prev_1 = None
        while curr_node1.next and curr_node1.data != key1:
            prev_1 = curr_node1
            curr_node1 = curr_node1.next

        curr_node2 = self.head
        prev_2 = None
        while curr_node2.next and curr_node2.data != key2:
            prev_2 = curr_node2
            curr_node2 = curr_node2.next

        prev_1.next = curr_node2
        prev_2.next = curr_node1

        curr_node1.next, curr_node2.next = curr_node2.next, curr_node1.next

    def length(self):
        curr_node = self.head
        total_nodes = 0
        while curr_node.next:
            curr_node = curr_node.next
            total_nodes += 1
        return total_nodes

    def length_recursive(self, node):
        if not node:
            return 0
        return 1 + self.length_recursive(node.next)

    def display(self):
        nodes = []
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
            nodes.append(curr_node.data)
        print(nodes)

    def get(self, index):
        if index >= self.length():
            print("List index out of range")
            return None
        curr_node = self.head
        curr_index = 0
        while True:
            curr_node = curr_node.next
            if curr_index == index:
                return curr_node.data
            curr_index += 1


def main():
    test = LinkedList()
    test.display()
    test.append(0)
    test.append(1)
    test.append(2)
    test.append(3)
    test.append(4)
    test.display()
    test.swap_nodes(4, 2)
    test.display()


if __name__ == '__main__':
    main()
