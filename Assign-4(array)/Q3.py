def transpose(mat):
    r = len(mat)
    c = len(mat[0])
    transposed = [[0] * r for _ in range(c)]

    for i in range(r):
        for j in range(c):
            transposed[j][i] = mat[i][j]

    return transposed

mat1 = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(mat1))    