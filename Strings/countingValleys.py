import math

def countingValleys(steps, path):

    #Make sure steps and len(path) are == or greater than zero
    if steps == 0:
        return 0
    if len(path) == 0:
        return 0
    if steps != len(path):
        return 0
    #keep track of steps down, up, and valleys
    sea_level = 0
    steps = 0
    valleys = 0
    #split the string into a list of strings
    types = list(path.upper())
    # check set if a value from ar already exists in our set, if it does we can increase pairs by one and remove the value from the set
    for val in types:
        # if the value is D we increment  sdown
        if val == "D":
            steps -= 1
            continue
        # if value is U we increment up
        elif val == "U":
            steps += 1
        #check if down is == up and add to valleys if true
        if steps == sea_level:
            valleys += 1
    #else we add to our set 
    return valleys

print(countingValleys(8, "UDDDUDUU"))