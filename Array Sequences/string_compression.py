"""
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely 

"compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this 
technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
"""

def compress(string):
    #declare a dictionary to store
    #key value pairs where key = character 
    # and value = count
    letters = dict()
    #we can use a list to append key, value pairs later
    result = []
    #for each character in the string entered
    for char in string:
        # If its not already in our dictionary
        # we will add the character as key and set count to 1
        if char not in letters:
            letters[char] = 1
        # If char is in dictionary we will add 1 to the count
        else:
            letters[char] +=1
    #Each key and value is appended to our result
    for k, v in letters.items():
        result.append(k + str(v))
    #We join our list to a string and return
    return "".join(result)



print(compress('AAAAABBBBCCCC')) #A5B4C4
print(compress('AABBCC')) #A2B2C2
print(compress('AAABCCDDDDD')) #A3B1C2D5
print(compress('AaBbCcDdCc')) #A1a1B1b1C2c2D1d1