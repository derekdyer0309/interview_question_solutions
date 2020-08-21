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
    

print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1], 10))

# class TestPair(object):
    
#     def test(self,sol):
#         assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
#         assert_equal(sol([1,2,3,1],3),1)
#         assert_equal(sol([1,3,2,2],4),2)
#         print('ALL TEST CASES PASSED')
        
# #Run tests
# t = TestPair()
# t.test(pair_sum)
