from util.classes.Graph import Graph
from util.classes.Queue import Queue
from util.neighboursFinder import findNeighbours


def convertToGraph(matrix, dimensions, start):
    old_point = None
    
    graph = Graph(start)
    queueue = Queue()

    #main loop
    queueue.add(start)

    while not queueue.is_empty():
        point = queueue.remove()
        x, y = point

        neighbours = findNeighbours(matrix, dimensions, point, old_point)

        for neighbour in neighbours:
            queueue.add(neighbour)
        
        graph.set(point, neighbours)

        if matrix[y][x] == 0:
            matrix[y][x] = 4
        old_point = point

    graph.get(start).setDistance(0)
    return graph