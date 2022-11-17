import random
import time
from colorama import init
from colorama import Fore, Back, Style

import matplotlib.pyplot as plt

# zainicjowanie zmiennych
wall_ = 'w'
cell = 'c'
start = 's'
exit_ = 'x'
unvisited = 'u'
height = 100
width = 100

# narysowanie labiryntu
def printMaze(maze):
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == unvisited):
                print(Fore.WHITE + str(maze[i][j]), end=" ")
            elif (maze[i][j] == cell):
                print(Fore.GREEN + str(maze[i][j]), end=" ")
            elif (maze[i][j] == start):
                print(Fore.YELLOW + str(maze[i][j]), end=" ")
            elif (maze[i][j] == exit_):
                print(Fore.BLUE + str(maze[i][j]), end=" ")
            else:
                print(Fore.RED + str(maze[i][j]), end=" ")

        print('\n')

# inicjalizacja kolorków
init()

# Randomize starting point and set it a cell
starting_height = int(random.random() * height)
starting_width = int(random.random() * width)
if (starting_height == 0):
    starting_height += 1
if (starting_height == height - 1):
    starting_height -= 1
if (starting_width == 0):
    starting_width += 1
if (starting_width == width - 1):
    starting_width -= 1

def generateMaze(starting_height, starting_width):
    maze = []

    # znalezienie sąsiednich komórek
    def surroundingCells(rand_wall):
        s_cells = 0
        if (maze[rand_wall[0] - 1][rand_wall[1]] == cell):
            s_cells += 1
        if (maze[rand_wall[0] + 1][rand_wall[1]] == cell):
            s_cells += 1
        if (maze[rand_wall[0]][rand_wall[1] - 1] == cell):
            s_cells += 1
        if (maze[rand_wall[0]][rand_wall[1] + 1] == cell):
            s_cells += 1

        return s_cells

    # Denote all cells as unvisited
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append(unvisited)
        maze.append(line)

    # Mark it as cell and add surrounding walls to the list
    maze[starting_height][starting_width] = cell
    walls = []
    walls.append([starting_height - 1, starting_width])
    walls.append([starting_height, starting_width - 1])
    walls.append([starting_height, starting_width + 1])
    walls.append([starting_height + 1, starting_width])

    # Denote walls in maze
    maze[starting_height - 1][starting_width] = wall_
    maze[starting_height][starting_width - 1] = wall_
    maze[starting_height][starting_width + 1] = wall_
    maze[starting_height + 1][starting_width] = wall_

    while (walls):
        # Pick a random wall
        rand_wall = walls[int(random.random() * len(walls)) - 1]

        # Check if it is a left wall
        if (rand_wall[1] != 0):
            if (maze[rand_wall[0]][rand_wall[1] - 1] == unvisited and maze[rand_wall[0]][rand_wall[1] + 1] == cell):
                # Find the number of surrounding cells
                s_cells = surroundingCells(rand_wall)

                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = cell

                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0] - 1][rand_wall[1]] != cell):
                            maze[rand_wall[0] - 1][rand_wall[1]] = wall_
                        if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                    # Bottom cell
                    if (rand_wall[0] != height - 1):
                        if (maze[rand_wall[0] + 1][rand_wall[1]] != cell):
                            maze[rand_wall[0] + 1][rand_wall[1]] = wall_
                        if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] + 1, rand_wall[1]])

                    # Leftmost cell
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1] - 1] != cell):
                            maze[rand_wall[0]][rand_wall[1] - 1] = wall_
                        if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] - 1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Check if it is an upper wall
        if (rand_wall[0] != 0):
            if (maze[rand_wall[0] - 1][rand_wall[1]] == unvisited and maze[rand_wall[0] + 1][rand_wall[1]] == cell):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = cell

                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0] - 1][rand_wall[1]] != cell):
                            maze[rand_wall[0] - 1][rand_wall[1]] = wall_
                        if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                    # Leftmost cell
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1] - 1] != cell):
                            maze[rand_wall[0]][rand_wall[1] - 1] = wall_
                        if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] - 1])

                    # Rightmost cell
                    if (rand_wall[1] != width - 1):
                        if (maze[rand_wall[0]][rand_wall[1] + 1] != cell):
                            maze[rand_wall[0]][rand_wall[1] + 1] = wall_
                        if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] + 1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Check the bottom wall
        if (rand_wall[0] != height - 1):
            if (maze[rand_wall[0] + 1][rand_wall[1]] == unvisited and maze[rand_wall[0] - 1][rand_wall[1]] == cell):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = cell

                    # Mark the new walls
                    if (rand_wall[0] != height - 1):
                        if (maze[rand_wall[0] + 1][rand_wall[1]] != cell):
                            maze[rand_wall[0] + 1][rand_wall[1]] = wall_
                        if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] + 1, rand_wall[1]])
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1] - 1] != cell):
                            maze[rand_wall[0]][rand_wall[1] - 1] = wall_
                        if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] - 1])
                    if (rand_wall[1] != width - 1):
                        if (maze[rand_wall[0]][rand_wall[1] + 1] != cell):
                            maze[rand_wall[0]][rand_wall[1] + 1] = wall_
                        if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] + 1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Check the right wall
        if (rand_wall[1] != width - 1):
            if (maze[rand_wall[0]][rand_wall[1] + 1] == unvisited and maze[rand_wall[0]][rand_wall[1] - 1] == cell):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = cell

                    # Mark the new walls
                    if (rand_wall[1] != width - 1):
                        if (maze[rand_wall[0]][rand_wall[1] + 1] != cell):
                            maze[rand_wall[0]][rand_wall[1] + 1] = wall_
                        if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] + 1])
                    if (rand_wall[0] != height - 1):
                        if (maze[rand_wall[0] + 1][rand_wall[1]] != cell):
                            maze[rand_wall[0] + 1][rand_wall[1]] = wall_
                        if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] + 1, rand_wall[1]])
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0] - 1][rand_wall[1]] != cell):
                            maze[rand_wall[0] - 1][rand_wall[1]] = wall_
                        if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Delete the wall from the list anyway
        for wall in walls:
            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                walls.remove(wall)

    # Mark the remaining unvisited cells as walls
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == unvisited):
                maze[i][j] = wall_

    # Set entrance and exit
    # for i in range(0, width):
    #     if (maze[1][i] == cell):
    #         maze[0][i] = start
    #         break

    # for i in range(width - 1, 0, -1):
    #     if (maze[height - 2][i] == cell):
    #         maze[height - 1][i] = start
    #         break
    
    return maze

maze1 = generateMaze(starting_height, starting_width)
maze2 = generateMaze(starting_height, starting_width)

#merge two mazes
rowNo = 0
maze = []
for (row1,row2) in zip(maze1,maze2):
    colNo = 0
    maze.append([])
    for (column1, column2) in zip(row1, row2):
        maze[rowNo].append(cell if column2 == cell else column1)
        colNo = colNo + 1
    rowNo = rowNo + 1

checkWalls = True
checkTryLimit = 3
tries = 0

while checkWalls and tries < checkTryLimit: #check if can put start and end
    # set entrance and exit
    wall1 = int(random.random() * 4) # 0 - n, 1 - e, 2 - s, 3 - w
    wall2 = wall1
    while wall2 == wall1:
        wall2 = int(random.random() * 4)

    #select candidates to enter
    wall1_entrances = []
    if wall1 in [0, 2]:
        for x in range (1, width - 1):
            # if maze[1 if wall1 == 0 else height - 1][x] == cell:
            #     wall1_entrances.append([0 if wall1 == 0 else height,x])
            if wall1 == 0: 
                if maze[1][x] == cell: wall1_entrances.append([0,x])
            else:
                if maze[height-2][x] == cell: wall1_entrances.append([height-1,x])
    if wall1 in [1, 3]:
        for x in range (1, height - 1):
            # if maze[x][1 if wall1 == 3 else width - 1] == cell:
            #     wall1_entrances.append([x, 0 if wall1 == 3 else width])
            if wall1 == 1: 
                if maze[x][1] == cell: wall1_entrances.append([x,0])
            else:
                if maze[x][height-2] == cell: wall1_entrances.append([x,height-1])

    wall2_entrances = []
    if wall2 in [0, 2]:
        for x in range (1, width - 1):
            # if maze[1 if wall2 == 0 else height - 2][x] == cell:
            #     wall2_entrances.append([0 if wall2 == 0 else height-1,x])
            if wall2 == 0: 
                if maze[1][x] == cell: wall2_entrances.append([0,x])
            else:
                if maze[height-2][x] == cell: wall2_entrances.append([height-1,x])
    if wall2 in [1, 3]:
        for x in range (1, height - 1):
            # if maze[x][1 if wall2 == 3 else width - 1] == cell:
            #     wall2_entrances.append([x, 0 if wall2 == 3 else width])
            if wall2 == 1: 
                if maze[x][1] == cell: wall2_entrances.append([x,0])
            else:
                if maze[x][height-2] == cell: wall2_entrances.append([x,height-1])

    if len(wall1_entrances) > 0 and len(wall2_entrances) > 0:
        #choose entrance and exit
        starting_point = random.choice(wall1_entrances)
        exit_point = random.choice(wall2_entrances)
        checkWalls = False
    
    tries = tries + 1

if checkWalls and tries == checkTryLimit:
    print("Cannot find two unique walls for entrance and exit")
    exit(0)

tmp_x, tmp_y = starting_point[0], starting_point[1]
maze[tmp_x][tmp_y] = start

tmp_x, tmp_y = exit_point[0], exit_point[1]
maze[tmp_x][tmp_y] = exit_

# Print final maze
printMaze(maze)

mazeMatrix = []

rowNo = 0

for row in maze:
    mazeMatrix.append([])
    for column in row:
        mazeMatrix[rowNo].append(1 if column == wall_ else 2 if column == start else 3 if column == exit_ else 0)
    rowNo = rowNo + 1

#print(mazeMatrix)
plt.imshow(mazeMatrix)
plt.show()

f = open('labirynt'+str(width)+'x'+str(height)+'.txt','w')
f.write(str(mazeMatrix))
f.close()