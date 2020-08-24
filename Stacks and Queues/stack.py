"""
Implement a stack:

It should have the methods:

Check if its empty
Push a new item
Pop an item
Peek at the top item
Return the size
"""

class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def size(self):
        return len(self.items)


s = Stack()

print(s.size())
print(s.isEmpty())

s.push('s')
s.push('k')

print(s.size())
print(s.isEmpty())

s.pop()

print(s.size())