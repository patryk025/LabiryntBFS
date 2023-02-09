import numpy as np

def calculateDistance(point, end):
    p_x, p_y = point
    e_x, e_y = end
    return ( (p_x - e_x)**2 + (p_y - e_y)**2 )**0.5

def angle_between(p1, p2):
    ang1 = np.arctan2(*p1[::-1])
    ang2 = np.arctan2(*p2[::-1])
    angle = np.rad2deg((ang1 - ang2) % (2 * np.pi))
    if angle < 180:
        return angle
    else:
        return 360 - angle

def calcAngleAndDist(p1, p2):
    return calculateDistance(p1, p2), angle_between(p1, p2)

def findNeighbours(matrix, dimensions, point, old_point, end = None):
    neighbours = []

    x, y = point.point
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
        tmp = old_point.point
        tmp2 = point.point
        vector = (tmp2[0] - tmp[0], tmp2[1] - tmp[1])
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

    if end is not None:
        tmp_list = []
        for neighbour in neighbours:
            dist, angle = calcAngleAndDist(neighbour, end)
            tmp_list.append([neighbour, dist, angle])
        
        tmp_list = sorted(tmp_list, key = lambda x: (x[1], x[2]))

        try:
            return [tmp_list[0][0]]
        except:
            raise Exception("Brak sąsiadów")
    else:
        return neighbours