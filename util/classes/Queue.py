class Queue:
    def __init__(self):
        self.queue = []

    def add(self, elem):
        self.queue.append(elem)

    def remove(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)