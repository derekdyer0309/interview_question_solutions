"""
Implement a Dequeue class

It should be able to do the following:

Check if its empty
Add to both front and rear
Remove from Front and Rear
Check the Size
"""

class Dequeue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


d = Dequeue()

print(d.isEmpty())

d.addFront(0)
d.addRear(1)
d.addRear(2)

print(d.isEmpty())

print(d.removeRear())

d.addRear(2)

print(d.removeFront())
print(d.removeFront())
print(d.removeFront())

print(d.isEmpty())

d.addFront(0)
d.addRear(1)
d.addRear(2)

print(d.isEmpty())

print(d.removeRear())
print(d.removeRear())
print(d.removeRear())

print(d.size())