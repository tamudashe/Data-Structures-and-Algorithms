class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.elements:
            return self.elements.pop()

    def peek(self):
        if self.elements:
            return self.elements[-1]

    def get_stack(self):
        return self.elements

    def is_empty(self):
        if not self.elements:
            return True
        return False
