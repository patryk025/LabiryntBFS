import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import json
from util.classes.Queue import Queue
from util.classes.Graph import Graph
from util.classes.Graph import Point

def loadJson(path):
    fileHook = open(path, 'r')
    dataLoaded = fileHook.read().strip()
    loadedData = json.loads(dataLoaded)
    return loadedData

# załaduj pliki
mazeMatrix = loadJson('datasety/labirynt15x15.txt')

# wyznacz parametry labiryntu
height = len(mazeMatrix)
width = len(mazeMatrix[0])

"""
0 - nieodwiedzone, puste
1 - ściana
2 - punkt startowy
3 - punkt końcowy
4 - odwiedzony, pusty
"""

# znalezienie punktu wejścia i wyjścia
def findStartingParams(matrix):
    rowNo = 0
    colNo = 0

    starting_point = None
    exit_point = None

    for row in matrix:
        colNo = 0
        for column in row:
            if matrix[rowNo][colNo] == 2: starting_point = (colNo, rowNo)
            if matrix[rowNo][colNo] == 3: exit_point = (colNo, rowNo)
            colNo = colNo + 1
        rowNo = rowNo + 1
    
    return starting_point, exit_point

solved_path = []

# zapisz parametry
starting_point, exit_point = findStartingParams(mazeMatrix)
    
print("Starting point: ", starting_point)
print("Exit point: ", exit_point)

# ustal punkt startowy
current_point = starting_point

# przetłumacz plik na postać grafu
#graf = convertToGraph(mazeMatrix, dimensions, starting_point)
graf = Graph(mazeMatrix, starting_point)
#print(graf)

# przeszukiwanie wszerz
solved_path, distance = graf.bfs(Point(current_point), exit_point)
#drawGraph(graf)


# przydzielenie kolorków
cvals  = range(5)
colors = ["#440154", "#30678d", "#35b778", "#fde724", "#440154"]

# tworzenie mapy kolorów
norm=plt.Normalize(min(cvals),max(cvals))
tuples = list(zip(map(norm,cvals), colors))
cmap = LinearSegmentedColormap.from_list("", tuples)

# generuj labirynt
plt.imshow(mazeMatrix, cmap=cmap, norm=norm)

# dorysuj wyznaczoną trasę
x_coords = []
y_coords = []
for pos in solved_path:
    point = pos.point
    x_coords.append(point[0])
    y_coords.append(point[1])
x_coords.append(exit_point[0])
y_coords.append(exit_point[1])
line_style = "ro--"
plt.plot(x_coords, y_coords, line_style, linewidth=2, markersize=1)
plt.show()
