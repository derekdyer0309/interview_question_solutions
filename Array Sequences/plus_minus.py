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