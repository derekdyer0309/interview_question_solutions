"""
Write a function to reverse a Linked List in place. 
The function will take in the head of the list as input and return 
the new head of the list.

You are given the example Linked List Node class:
"""

class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None

# Iterative Approach

def reverse(head):
    
    prev = None
    current = head
    nxt = None

    while current != None:
        nxt = current.next_node
        current.next_node = prev

        prev = current

        current = nxt

    return prev.value


# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.next_node = b
b.next_node = c
c.next_node = d

print(reverse(a))

print (d.next_node.value)
print (c.next_node.value)
print (b.next_node.value)


# Recursive approach

def recursive_reverse(head):

    if head.next_node == None:
        return head
    
    reversed_list_head = recursive_reverse(head.next_node)

    head.next_node.next_node = head

    head.next_node = None

    return reversed_list_head

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.next_node = b
b.next_node = c
c.next_node = d

print(recursive_reverse(a))
print(d.value)
print (d.next_node.value)
print (c.next_node.value)
print (b.next_node.value)