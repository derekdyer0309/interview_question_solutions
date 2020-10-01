import math

def repeatedString(s, n):
    #Edge case: string contains only 1 character
    if len(s) == 1:
        if 'a' not in s:
            return 0
        return n
    #string needs to be at least one character and n needs to be at least one character
    min_n = 1
    #string must be <= 100 characters
    maxs = 100
    #max number is 10 ^^ 12
    max_n = math.pow(10, 12)
    #length for if statement logic comparison of the above
    str_len = len(s)
    #a list of each character in lowercase  as long as we don't exceed the max string length
    seq = [c.lower() for c  in s * n if len(s) < maxs and len(s) > min_n and n < max_n]
    #counts the number of times 'a' appears in our string
    seq_len = seq[:n].count('a')
    #if the constraints are met
    if type(s) == str and str_len >= min_n and str_len <= maxs and n == int(n) and n >= min_n and n <= max_n:
        #return the remainder of our sequence length and n
        return seq_len % n 


print(repeatedString("AbA", 10))