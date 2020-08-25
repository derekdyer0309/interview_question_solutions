"""
Given a string of opening and closing parentheses, 
check whether it’s balanced. We have 3 types of parentheses: 
round brackets: (), square brackets: [], and curly brackets: {}. 
Assume that the string doesn’t contain any other character than 
these, no spaces words or numbers. As a reminder, balanced parentheses 
require every opening parenthesis to be closed in the reverse order 
opened. For example ‘([])’ is balanced but ‘([)]’ is not.

You can assume the input string has no spaces.
"""

def balanced_parenthesis(string):
    #Declare our stack
    stack = []
    #Set what we expect our opening brackets to be
    opening = ("(", "{", "[")
    #Set what we expect our closing brackets to be
    closing = (")", "}", "]")
    #Create a dictionary to compare opening to closing
    #and append the closing bracket for each opening bracket
    parenthesis = {"(": ")", "[": "]", "{": "}"}
    #for each character
    for char in string:
        #if in opening append the complementary closing bracket
        if char in opening:
            stack.append(parenthesis[char])
        # if its a closing bracket, to remain balanced
        # it has to be equal to the last closing bracket encountered
        elif char in closing:
            if char != stack.pop():
                return False 
    # if our stack is empty at the end
    return len(stack) == 0



print(balanced_parenthesis("({[]})"))
print(balanced_parenthesis("[](){([[[]]])}"))
print(balanced_parenthesis("()(){]}"))