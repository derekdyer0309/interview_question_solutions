"""
Problem
Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:

5 is the missing number
"""

def finder(arr1, arr2):
    #if one array has no elements or
    #if both arrays have only one element 
    #in this case they should be considered equal
    if len(arr1) == len(arr2):
        return f"No elements are missing"

    if len(arr2) != len(arr1)-1:
        return f"Too many missing elements"
    
    #Initialize a variable we can return
    missing = 0
    #map values for both arrays and keep track of their count
    #keys = elements, values = count
    seen = dict()
    for i in arr2:
        if i not in seen:
            seen[i] = 1
    for i in arr1:
        if i not in seen:
            missing = i

    return f"{missing} is the missing number"
    

print(finder([1,2,3,4,5,6,7],[1, 2, 3, 4, 5, 6]))
