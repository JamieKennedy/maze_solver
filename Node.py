class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.neighbours = []

    def add_neighbour(self, neighbour, distance):
        self.neighbours.append((neighbour, distance))

    def get_neighbours(self):
        return self.neighbours

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value








