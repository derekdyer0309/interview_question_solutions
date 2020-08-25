"""
Pros:
Cons:
"""

class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next_node = b
b.prev_node = a

b.next_node = c
c.prev_node = b

c.next_node = d
d.prev_node = c


print("Dll in order\n")
print(a.value)
print(a.next_node.value)
print(b.next_node.value)
print(c.next_node.value)
print("\n")
print("b -> d prev in order\n")
print(b.prev_node.value)
print(c.prev_node.value)
print(d.prev_node.value)