def checkStraightLine(coordinates):
    n = len(coordinates)
    if n < 3:
        return True

    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    slope = (y2 - y1) / (x2 - x1)

    for i in range(2, n):
        x, y = coordinates[i]
        new_slope = (y - y1) / (x - x1)
        if new_slope != slope:
            return False

    return True


coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
print(checkStraightLine(coordinates))
