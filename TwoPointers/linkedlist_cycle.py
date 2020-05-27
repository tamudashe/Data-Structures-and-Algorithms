# Given the head of a singly linkedlist, write a function to determine if
# the linkedlist has a cycle in it or not

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def has_cycle(head):
    if not head or not head.next:
        return None

    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print(has_cycle(head))

    head.next.next.next.next = head.next.next
    print(has_cycle(head))

if __name__ == '__main__':
    main()
