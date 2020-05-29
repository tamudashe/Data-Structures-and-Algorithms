# Given the head of a singly linkedlist, write a method to return the
# middle node of the linkedlist
# If the total number of nodes in the linkedlist is even, return the second
# middle node

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def get_linkedlist_min(head):
    slow = head
    fast = head
    while  fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    assert get_linkedlist_min(head) == 4
    print("Passed all test cases!")

if __name__ == '__main__':
    main()
