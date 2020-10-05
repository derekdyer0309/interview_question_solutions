a = [[1, 1, 1, 0, 0, 0],[0, 1, 0, 0, 0, 0],[1, 1, 1, 0, 0, 0],[0, 0, 2, 4, 4, 0],[0, 0, 0, 2, 0, 0],[0, 0, 1, 2, 4, 0]]

def hourglassSum(arr):
    # check if our array has 6 arrays inside
    max_total = True
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            total = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if max_total == True:
                max_total = total
            max_total = max(max_total, total)

    return max_total

print(hourglassSum(a))