class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def get_stack(self):
        return self.items

"""
mystack=Stack()
mystack.push("A")
mystack.push("B")
print(mystack.get_stack())
mystack.push("C")
print(mystack.get_stack())
mystack.pop()
print(mystack.get_stack())
"""
