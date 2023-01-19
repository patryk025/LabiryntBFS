from util.classes.Queue import Queue
from util.neighboursFinder import findNeighbours

class Graph:
    def __init__(self, matrix, key = None):
        self.graph = {}
        self.node_list = {}
        self.matrix = matrix
        self.point = (None, None)
        self.dimensions = (len(self.matrix), len(self.matrix[0]))
        self.biggest_queue_size = 0
        
        if key is not None:
            self.insert(key)

    def copy(self):
        graph_copy = Graph(self.matrix)
        graph_copy.graph = self.graph.copy()
        graph_copy.node_list = self.node_list.copy()
        graph_copy.point = self.point
        graph_copy.dimensions = self.dimensions
        return graph_copy
            
    def insert(self, key, root = None):
        keyObj = Point(key)
        if key not in self.graph:
            self.graph[key] = []
            self.node_list[key] = keyObj
        else:
            print("Warning: node with key {} already exists" % key)
        
        if root is not None:
            self.graph[root].append()

    def set(self, key, value, distance = None):
        if key not in self.graph:
            self.insert(key)

        for val in value:
            node = Point(val)
            if distance is not None:
                node.setDistance(distance)
            self.graph[key].append(node)

    def get(self, key):
        try:
            key = key.point
        except:
            pass

        if key not in self.graph:
            self.insert(key)

        return self.node_list[key]

    def getNodes(self, key):
        if key not in self.graph:
            self.insert(key)

        return self.graph[key]

    def getNextElementToAnalyze(self, point):
        copy_obj = self.copy()
        copy_obj.point = point
        copy_obj.insert(point)
        return copy_obj
        
    def __str__(self):
        string = ""

        for key in self.graph:
            string = string + str(key) + ": " + str(self.graph[key].point) + "\n"

        return string
    
    def bfs(self, start, end, heuristic = False):
        old_point = self.point[1]
        self.point = (self.point[1], start)
    
        queue = Queue()
        queue.add(self)

        while not queue.is_empty():
            if queue.size() > self.biggest_queue_size:
                self.biggest_queue_size = queue.size()

            graph = queue.remove()
            point = graph.point

            self.point = (old_point, point[1])

            _, point = self.point
            x, y = point.point
            print(point.point)

            if point.point == end:
                print("Znaleziono rozwiązanie")
                print("Dystans", point.getDistance())
                print("Trasa:", point.road)

                return point.road, point.getDistance()

            if heuristic is False:
                neighbours = findNeighbours(self.matrix, self.dimensions, point, old_point)
            else:
                neighbours = findNeighbours(self.matrix, self.dimensions, point, old_point, end)

            self.set(point, neighbours)

            if self.matrix[y][x] == 0:
                self.matrix[y][x] = 4

            for neighbour in neighbours:
                if neighbour not in queue.queue:
                    copy_obj = self.copy()
                    new_road = point.road.copy()
                    new_road.append(point)
                    copy_obj.point = (point, Point(neighbour, new_road))
                    queue.add(copy_obj)
            
            old_point = point

        self.get(start).setDistance(0)

class Point:
    def __init__(self, point, road = None):
        #print("Hitted Point constructor, debug: point => ", point, ", road => ", road)
        self.point = point
        if road is not None:
            self.road = road
        else:
            self.road = []

    def setDistance(self, distance):
        self.distance = distance

    def getDistance(self):
        return len(self.road);

    def setRoad(self, road):
        self.road = road

    def getRoad(self):
        return self.road
