
def balancedBrackets(string):

    # Check if brackets are divisible by 2
    # if len(string) % 2 != 0:
    #     return 0

    # ('(', '{', '[', '|')
    opening = tuple('({[|')
    # (')', '}', ']', '|')
    closing = tuple(')}]|')
    #{'(' : ')', '[' : ']', '{' : '}', '|' : '|'}
    mapping = dict(zip(opening, closing))

    stack = []

    for char in string:
        # If the char is in opening, we append the closing
        if char in opening:
            stack.append(mapping[char])
        # If the char is in closing and not in the stack
        elif char in closing:
            if not stack or char != stack.pop():
                return False
    #We want our stack to be empty so we return the opposite of stack
    return not stack

print(balancedBrackets('I (wa)n{t to buy a on}esie[…] b(u{[t] kno}w it) won’t suit me.'))