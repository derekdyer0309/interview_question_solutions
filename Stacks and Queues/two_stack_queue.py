"""
Given the class below, implement a Queue class 
using two stacks. 

Use a Python list data structure as your Stack
"""

class Queue2Stacks(object):
    
    def __init__(self):
        #Two stacks
        self.in_stack = []
        self.out_stack = []
     
    def enqueue(self, element):
        #Add elements to instack
        self.in_stack.append(element)
    
    def dequeue(self):
        #if outstack is empty
        if not self.out_stack:
            #while there is an instack
            while self.in_stack:
                #append the instack elements to our outstack and reverse
                self.out_stack.append(self.in_stack.pop())
                #pop the item off the stack
        return self.out_stack.pop()


q = Queue2Stacks()

q.enqueue(1)
q.enqueue(2)
q.enqueue("Hello")
q.enqueue("World")

print(q.dequeue()) #1
print(q.dequeue()) #2

q.enqueue(True)
q.enqueue(70)
q.enqueue('2')
q.enqueue("string")

print(q.dequeue()) #Hello
print(q.dequeue()) #World
print(q.dequeue()) #True

