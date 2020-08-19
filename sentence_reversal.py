"""
Given a string of words, reverse all the words. For example:

Given:

'This is the best'

Return:

'best the is This'

As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:

'  space here'  and 'space here      '

both become:

'here space'


###NOTE: DO NOT USE .reverse()

"""

def string_reversal(str):
    #separate words into a list
    #remove whitespace
    sentence = list(str.split(' '))
    #create list to store indices in reverse order
    reversed_str = []
    #iterate string in reverse order
    for word in sentence[::-1]:
        #removes excess whitespace
        if word is not '':
            reversed_str.append(word)
    return " ".join(reversed_str)



print(string_reversal('This is the best'))
print(string_reversal('  space here'))