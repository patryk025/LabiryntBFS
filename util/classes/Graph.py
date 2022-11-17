class Graph:
    def __init__(self, key = None):
        self.graph = {}
        
        if key is not None:
            self.insert(key)
            
    def insert(self, key, root = None):
        if key not in self.graph:
            self.graph[key] = []
        else:
            print("Warning: node with key {} already exists" % key)
        
        if root is not None:
            self.graph[root].append(Node(key))

    def set(self, key, value, distance = None):
        if key not in self.graph:
            self.insert(key)

        for val in value:
            node = Node(val)
            if distance is not None:
                node.setDistance(distance)
            self.graph[key].append(node)

    def get(self, key):
        if key not in self.graph:
            self.insert(key)

        return self.graph[key]
        
    def __str__(self):
        string = ""

        for key in self.graph:
            string = string + str(key) + ": " + str(self.graph[key].point) + "\n"

        return string

class Node:
    def __init__(self, point):
        self.point = point
        self.distance = None

    def setDistance(self, distance):
        self.distance = distance

    def getDistance(self):
        return self.distance
