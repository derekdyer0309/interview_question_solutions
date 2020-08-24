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
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


s = Stack()

print(s.size())
print(s.isEmpty())

s.push('s')
s.push('t')
s.push('a')
s.push('c')
s.push('k')

print(s.size())
print(s.isEmpty())
print(s.peek())
print(s.pop())

print(s.size())