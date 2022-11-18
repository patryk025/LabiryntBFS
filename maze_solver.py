import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import json
from util.classes.Queue import Queue
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
