class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # noot indexable, dummy node to allow us to point to the first node
        self.head = Node()
        
    def append(self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next:
            curr = curr.next 
        curr.next = new_node
    
    def length(self):
        length = 0
        curr = self.head
        while curr.next:
            curr = curr.next
            length += 1
        return length

    def display(self):
        seen = []
        curr = self.head
        while curr.next:
            curr = curr.next
            seen.append(curr.data)
        print(seen)
        
    def delete(self, index):
        if index >= self.length():
            print('List index out of range')
            return -1
        
        curr = self.head 
        i = 0
        while curr.next.next and i < index:
            curr = curr.next
            i += 1
        curr.next = curr.next.next
    
    def get(self, index):
        if index >= self.length():
            print('List index out of range')
            return -1
        curr = self.head 
        i = 0
        while i <= index:
            curr = curr.next
            i += 1
        return curr.data
    
    def insert(self, data, index):
        if index > self.length():
            print('List index out of range')
            return -1
        i = 0
        curr = self.head
        while curr.next and i < index:
            curr = curr.next
            i += 1
        new_node = Node(data)
        new_node.next = curr.next
        curr.next = new_node
            


test_list = LinkedList()
test_list.append(1)
test_list.append(2) 
test_list.append(3)
test_list.append(4) 
test_list.append(5)
test_list.append(6)       
test_list.display()
test_list.delete(0)
test_list.display()
print(test_list.length())
test_list.insert(1, 5)
test_list.display()
    
    
    
    
        
    