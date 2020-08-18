'''
Array Pair Sum
Problem
Given an integer array, output all the unique pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)

would return 2 pairs:

 (1,3)
 (2,2)

Worry first about returning the number of pairs

'''

def pair_sum(arr, n):
    
    # Handle if array has less than two indices
    if len(arr) < 2:
        return None

    # Cache for repeated operations
    count = {}
    
    i = 0
    k = 1
    # Keep track of what sum of pairs equal n
    seen = set()
    for i in arr:
        for k in arr:
            digits = tuple([i, k])
            # Add digits to dictionary and seen
            if i + k == n and digits[::-1] not in seen:
                count[digits] = 1
                seen.add(digits)

    return count
    

# print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1], 10))

# class TestPair(object):
    
#     def test(self,sol):
#         assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
#         assert_equal(sol([1,2,3,1],3),1)
#         assert_equal(sol([1,3,2,2],4),2)
#         print('ALL TEST CASES PASSED')
        
# #Run tests
# t = TestPair()
# t.test(pair_sum)

arr = [1, 1, 0, -1, -1]

def plusMinus(arr):

    el_count = len(arr)

    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i == 0:
            zero += 1
        elif i > 0:
            pos += 1
        else: 
            neg += 1

    p_ratio = pos / el_count
    neg_ratio = neg / el_count
    zero_ratio = zero / el_count

    return format(p_ratio, '.6f') + format(neg_ratio, '.6f') + format(zero_ratio, '.6f')


print(plusMinus(arr))
