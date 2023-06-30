def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    row_start, row_end = 0, n - 1
    col_start, col_end = 0, n - 1

    while num <= n * n:
        for j in range(col_start, col_end + 1):
            matrix[row_start][j] = num
            num += 1
        row_start += 1

        for i in range(row_start, row_end + 1):
            matrix[i][col_end] = num
            num += 1
        col_end -= 1

        for j in range(col_end, col_start - 1, -1):
            matrix[row_end][j] = num
            num += 1
        row_end -= 1

        for i in range(row_end, row_start - 1, -1):
            matrix[i][col_start] = num
            num += 1
        col_start += 1

    return matrix

print(generateMatrix(4))