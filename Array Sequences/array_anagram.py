'''
Anagram Check
Problem

Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"

Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".

Solution
Fill out your solution below:
'''

def anagram(s1, s2):
    #remove spaces since anagrams are not space concious
    s = s1.replace(' ','').lower()
    st = s2.replace(' ','').lower()

    #handle if string contains only one letter
    if len(s) == 1 and len(st) == 1:
        if s == st:
            return True
        else:
            return False
    # make sure they are the same length
    elif len(s) != len(st):
        return False

    else:
        #store both sets of letters in a map
        s_letters = {}
        st_letters = {}
        # add letters with count to the map
        for i in s:
            s_letters[i] = s_letters.get(i, 0) + 1
        for k in st:
            st_letters[k] = st_letters.get(k, 0) + 1
    #if both are equal, we will return True
    return st_letters == s_letters       

print(anagram('go go go','gggooo'))
print(anagram('abc','cba'))
print(anagram('hi man','hi     man'))
print(anagram('aabbcc','aabbc'))
print(anagram('123','1 2'))
print(anagram('a','b'))
print(anagram('aa','bb'))
print(anagram('aacc','ccac'))
print(anagram('dgo','God'))
print(anagram('clint eastwood','old west action'))



# class AnagramTest(object):
    
#     def test(self,sol):
#         assert_equal(sol('go go go','gggooo'),True)
#         assert_equal(sol('abc','cba'),True)
#         assert_equal(sol('hi man','hi     man'),True)
#         assert_equal(sol('aabbcc','aabbc'),False)
#         assert_equal(sol('123','1 2'),False)
#         print('ALL TEST CASES PASSED')

# # Run Tests
# t = AnagramTest()
# t.test(anagram)

