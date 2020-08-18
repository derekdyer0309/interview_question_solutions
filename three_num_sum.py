import random
import time


# Naive approach
def threeNumberSum(arr, target):
    # use three nested loops and check if sum of any three elements == target
    res = []
    for i in range(0, len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == target:
                    res.append([arr[i], arr[j], arr[k]])
    return res

# Map/ Set
def threeSum(arr, target):
    result = []
    # Iterate through array
    for i in range(0, len(arr) - 1):
        # Fix first el
        curr = target - arr[i]
        nums = set()
        # find the other two el using two sum approach 
        for j in range(0, len(arr) - 1):
            if curr - arr[j] in nums:
                result.append([arr[i], arr[j], curr - arr[j]])
            else:
                nums.add(arr[j])

    return result


my_list = list(random.sample(range(-3000, 3000), 500))
little_list = [12, 3, 1, 2, -6, 5, -8, 6]



start = time.perf_counter()
threeNumberSum(little_list, 0)
end = time.perf_counter()
print(f"little_list naive: {end - start}")

start = time.perf_counter()
threeSum(little_list, 0)
end = time.perf_counter()
print(f"little_list map/set: {end - start}")

start = time.perf_counter()
threeNumberSum(my_list, 30)
end = time.perf_counter()
print(f"my_list naive: {end - start}")

start = time.perf_counter()
threeSum(my_list, 30)
end = time.perf_counter()
print(f"my_list map/set: {end - start}")
