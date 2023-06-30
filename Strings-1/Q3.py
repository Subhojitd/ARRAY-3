def validMountainArray(arr):
    n = len(arr)
    i = 0

    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1

    if i == 0 or i == n - 1:
        return False

    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1

    return i == n - 1

arr = [1,2,3,4,3,2,1]
print(validMountainArray(arr))