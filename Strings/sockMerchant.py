# Alex works at a clothing store. There is a large pile of socks that must be paired by color for sale. 
# Given an array of integers representing the color of each sock, determine how many pairs of socks with 
# matching colors there are.

# Function Description

# sockMerchant has the following parameter(s):

# n: the number of socks in the pile
# ar: the colors of each sock
# Input Format

# The first line contains an integer , the number of socks represented in .
# The second line contains  space-separated integers describing the colors  of the socks in the pile.
 
# Output Format

# Return the total number of matching pairs of socks that Alex can sell.

# Sample Input

# 9
# 10 20 20 10 10 30 50 10 20

# Sample Output

# 3

def sockMerchant(n, ar):
    
    #Make sure n and len(ar) are not 0
    if n == 0:
        return 0
    if len(ar) == 0:
        return 0

    seen = set()
    pairs = 0
    types = list(ar.split(' '))

    # check set if a value from ar already exists in our set, if it does we can increase pairs by one and remove the value from the set
    for val in types:
        if val in seen:
            seen.remove(val)
            pairs += 1
    #else we add to our set
        else:
            seen.add(val)
    
    return pairs

print(sockMerchant(10, "1 1 3 1 2 1 3 3 3 3"))


