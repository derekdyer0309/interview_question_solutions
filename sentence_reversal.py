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


###NOTE: DO NOT USE .reverse()###

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


print(string_reversal('    space before')) #'before space'
print(string_reversal('space after     ')) #'after space'
print(string_reversal('   Hello John    how are you   ')) # 'you are how John Hello'
print(string_reversal('1')) #1

# from nose import nose.tools
# class ReversalTest(object):
    
#     def test(self,sol):
#         assert_equal(sol('    space before'),'before space')
#         assert_equal(sol('space after     '),'after space')
#         assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
#         assert_equal(sol('1'),'1')
#         print("ALL TEST CASES PASSED")
        
# # Run and test
# t = ReversalTest()
# t.test(string_reversal)