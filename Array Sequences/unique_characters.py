"""
Given a string,determine if it is compreised of all unique characters.
For example, the string 'abcde' has all unique characters and should 
return True. The string 'aabcde' contains duplicate characters and 
should return false.
"""

def unique_char(string):
    #set all our chars in string to list
    chars = [i for i in string]
    #get all of our unique characters into set
    unique_chars = [i for i in chars if chars.count(i)<2]
    #for each character in chars
    for i in chars:
        #if the character is not in unique characters
        if i not in unique_chars:
            return False
    #return true by default if loop does not return false
    return True


print(unique_char('AaBbCcDd'))