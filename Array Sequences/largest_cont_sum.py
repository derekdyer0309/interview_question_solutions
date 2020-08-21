"""
Problem
Given an array of integers (positive and negative) find the 
largest continuous sum.
"""

def largest_sum(arr):
    
    #if array has 0 elements we can't get a sum
    if len(arr) == 0:
        return
    #start with our max sum being the first value in arr
    #as our anchor point
    max_sum = sum = arr[0]
    # add every num in arr to first num
    for num in arr[1:]:
    #Total running sum
        sum = max(sum+num, num)
    #Capture max of total running and compare as it changes
        max_sum = max(sum, max_sum)
    return max_sum

print(largest_sum([1,2,-1,3,4,10,10,-10,-1]))