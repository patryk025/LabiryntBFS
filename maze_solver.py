import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import json
from util.classes.Graph import Node
from util.classes.Queue import Queue
from util.neighboursFinder import findNeighbours
from util.matrixToGraph import convertToGraph

# załaduj pliki
myfile = open('datasety/labirynt1000x1000.txt', 'r')
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

def drawGraph(graph):
    queue = Queue()

    start = list(graph.graph.keys())[0]

    queue.add(graph.get(start))

    point_list = []

    while not queue.is_empty():
        point = queue.remove()

        point_list.append(point)

        nodes = graph.getNodes(point.point)
        for node in nodes:
            if node not in queue.queue:
                queue.add(node)
                plt.plot([point.point[0], node.point[0]], [point.point[1], node.point[1]], color="black")

    for node in point_list:
        obj = node
        plt.plot(obj.point[0], obj.point[1], 'o', color="white", markersize=40, markeredgewidth=1.5, markeredgecolor="black")
        plt.text(obj.point[0], obj.point[1], str(obj.point)+"\ndist:"+str(obj.getDistance()), horizontalalignment='center', verticalalignment='center')

    plt.xlim(-1, width-1)
    plt.ylim(-1, height-1)
    plt.gca().invert_yaxis()
    plt.show()

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

solved_path = []

# przeszukiwanie wszerz
def bfs(graph, start, end):
    queue = Queue()
    queue.add(graph.get(start))

    while not queue.is_empty():
        point = queue.remove()
        if point.point == end:
            print("Znaleziono rozwiązanie")
            print("Dystans", point.getDistance())
            
            # odtwórz trasę
            solved_path.append(end)
            ancestor = graph.getAncestor(point.point)
            while ancestor is not start:
                solved_path.append(ancestor)
                ancestor = graph.getAncestor(ancestor)
            solved_path.append(start)
            solved_path.reverse()
            print("Trasa:", solved_path)

            return point.getDistance()

        nodes = graph.getNodes(point.point)
        for node in nodes:
            if node not in queue.queue:
                queue.add(node)
                node.setDistance(point.getDistance() + 1)

    print("Brak rozwiązania :(")

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
    x_coords.append(pos[0])
    y_coords.append(pos[1])
line_style = "ro--"
plt.plot(x_coords, y_coords, line_style, linewidth=2, markersize=5)
plt.show()
