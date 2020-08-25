"""
Given a singly linked list, write a function which takes in the 
first node in a singly linked list and returns a boolean indicating 
if the linked list contains a "cycle".

A cycle is when a node's next point actually points back to a 
previous node in the list. This is also sometimes known as a circularly 
linked list.

You've been given the Linked List Node class code:
"""

class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None


def cycle_check(node):

    pointer_one = node
    pointer_two = node

    while pointer_two != None and pointer_two.next_node != None:
        pointer_one = pointer_one.next_node
        pointer_two = pointer_two.next_node.next_node

        if pointer_two == pointer_one:
            return True
    
    return False
        
a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c
c.next_node = a # Cycle Here!

print(cycle_check(a))

x = Node(1)
y = Node(2)
z = Node(3)

x.next_node = y
y.next_node = z

print(cycle_check(y))