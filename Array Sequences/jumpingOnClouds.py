def jumpingOnClouds(c):
    #c is our integer array
    #if our array length == 0 we return zero
    if len(c) == 0:
        return 0
    #if our array length == 1 we can't make a jump
    if len(c) == 1:
        return 1
    #if our array length == 2 we can only make one jump
    if len(c) == 2:
        return 1
    end = len(c) - 1
    #keep track of our index
    index = 0
    #keep track of our jumps
    jumps = 0
    #while our index is less than the length of our array
    while index < end:
        # if we can make a jump of 2
        if index + 2 <= end and c[index + 2] == 0:
            index += 2
            jumps += 1
        elif index + 1 <= end:
            index += 1
            jumps += 1

        # else if we can't make a jump of 2 and can only make a jump of one

    
    return jumps

print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))