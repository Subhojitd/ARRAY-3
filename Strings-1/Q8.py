def multiply(mat1, mat2):
    m = len(mat1)
    k = len(mat1[0])
    n = len(mat2[0])

    result = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(k):
            if mat1[i][j] != 0:
                for k in range(n):
                    if mat2[j][k] != 0:
                        result[i][k] += mat1[i][j] * mat2[j][k]

    return result

mat1 = [[1,0,0],[-1,0,3]]
mat2 = [[7,0,0],[0,0,0],[0,0,1]]
print(multiply(mat1,mat2))