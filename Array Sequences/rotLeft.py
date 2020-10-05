
a = [33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60, 87, 97]


def rotLeft(a, d):
    # counter to be less than d
    i = 0
    #stores a in our own list
    rot_a = [i for i in a]
    #while our counter is less than the number of rotations to be performed
    while i < d:
        #we insert our 0th element to the end of our list
        rot_a.insert(len(a), rot_a.pop(0))
        #increment our counter
        i += 1 
    #return our rotated list
    return rot_a


print(rotLeft(a, 13))