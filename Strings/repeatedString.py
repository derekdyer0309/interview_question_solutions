import math

def repeatedString(s, n):
    #Edge case: string contains only 1 character
    if len(s) == 1:
        #if there are no 'a's
        if 'a' not in s:
            return 0
        #if n == 0
        if n == 0:
            return 0
        return n
    #minimun constraint for s and n
    min_n = 1
    #maximum constraint for string
    maxs = 100
    #maximum constraint for n
    max_n = math.pow(10, 12)
    #string length
    str_len = len(s)
    #lower all characters and store each string char in list

    if type(s) == str and str_len >= min_n and str_len <= maxs and n == int(n) and n >= min_n and n <= max_n:
        return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")


print(repeatedString("kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm"
, 736778906400))