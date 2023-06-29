def convert_to_2d_array(original, m, n):
    if len(original) != m * n:
        return []

    result = [[0] * n for _ in range(m)]
    for row in range(m):
        for column in range(n):
            index = row * n + column
            result[row][column] = original[index]

    return result

arr1 = [2,3,4,5]
m = 2
n = 2
print(convert_to_2d_array(arr1,m,n))

