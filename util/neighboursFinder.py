def findNeighbours(matrix, dimensions, point, old_point):
    neighbours = []

    x, y = point
    height, width = dimensions

    if y - 1 >= 0:
        if matrix[y - 1][x] in [0, 3]:
            neighbours.append((x, y - 1))
        elif matrix[y - 1][x] != 3:
            neighbours.append(None)
    else:
        neighbours.append(None)
    if x + 1 < width:
        if matrix[y][x + 1] in [0, 3]:
            neighbours.append((x + 1, y))
        elif matrix[y][x + 1] != 3:
            neighbours.append(None)
    else:
        neighbours.append(None)
    if y + 1 < height:
        if matrix[y + 1][x] in [0, 3]:
            neighbours.append((x, y + 1))
        elif matrix[y + 1][x] != 3:
            neighbours.append(None)
    else:
        neighbours.append(None)
    if x - 1 >= 0:
        if matrix[y][x - 1] in [0, 3]:
            neighbours.append((x - 1, y))
        elif matrix[y][x - 1] != 3:
            neighbours.append(None)
    else:
        neighbours.append(None)

    if old_point is not None:
        vector = (point[0] - old_point[0], point[1] - old_point[1])
    else:
        vector = None

    if vector == (0, -1): # N
        neighbours = [neighbours[3], neighbours[0], neighbours[1], neighbours[2]]
    elif vector == (1, 0): #E
        pass
    elif vector == (0, 1): #S
        neighbours = [neighbours[1], neighbours[2], neighbours[3], neighbours[0]]
    else: #W
        neighbours = [neighbours[2], neighbours[3], neighbours[0], neighbours[1]]

    while None in neighbours:
        neighbours.remove(None)

    return neighbours