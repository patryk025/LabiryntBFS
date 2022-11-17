import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import json
from util.classes.Queue import Queue
from util.neighboursFinder import findNeighbours
from util.matrixToGraph import convertToGraph

# załaduj pliki
myfile = open('datasety/labirynt5x5.txt', 'r')
data = myfile.read().strip()
mazeMatrix = json.loads(data)

# wyznacz parametry labiryntu
height = len(mazeMatrix)
width = len(mazeMatrix[0])
dimensions = (height, width)

"""
0 - nieodwiedzone, puste
1 - ściana
2 - punkt startowy
3 - punkt końcowy
4 - odwiedzony, pusty
"""

# znalezienie punktu wejścia i wyjścia
def findStartParams(matrix):
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

"""
def bfs(matrix, start):
    old_point = None

    queue = Queue()

    #main loop
    queue.add(start)

    while not queue.is_empty():
        point = queue.remove()
        x, y = point

        print("Current point:", point)
        neighbours = findNeighbours(matrix, dimensions, point, old_point)
        print("Neighbours:", neighbours)
        for neighbour in neighbours:
            if neighbour not in queue.queue:
                queue.add(neighbour)
        
        if matrix[y][x] == 0:
            matrix[y][x] = 4
        print("Queue:", queue.queue)
        print()
        old_point = point
"""

# przeszukiwanie wszerz
def bfs(graph, start, end):
    queue = Queue()
    queue.add(start)

    while not queue.is_empty():
        point = graph.get(queue.remove())
        if point.point == end:
            return point.getDistance()

        nodes = graph.get(point)
        for node in nodes:
            if node not in queue.queue:
                queue.add(node)
                node.setDistance(point.getDistance() + 1)

    pass

# zapisz parametry
starting_point, exit_point = findStartParams(mazeMatrix)
    
print("Starting point: ", starting_point)
print("Exit point: ", exit_point)

# ustal punkt startowy
current_point = starting_point

# przetłumacz plik na postać grafu
graf = convertToGraph(mazeMatrix, dimensions, starting_point)
#print(graf)

bfs(graf, current_point, exit_point)

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
line_style = "ro--"
plt.plot([2, 2, 3, 3], [4, 3, 3, 0], line_style, linewidth=2, markersize=12)
plt.show()
