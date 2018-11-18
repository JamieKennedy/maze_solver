from Node import Node


class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, name, value):
        self.nodes.append(Node(name, value))

    def get_nodes_names(self):
        return [node.get_name() for node in self.nodes]

    def get_nodes(self):
        nodes = []
        for node in self.nodes:
            x, y = node.get_name()
            value = node.get_value()
            neighbours = node.get_neighbours()
            nodes.append(((x, y), value, neighbours))

        return nodes

    def print_nodes_names(self):
        print([node.get_name() for node in self.nodes])

    def print_nodes(self):
        nodes = []
        for node in self.nodes:
            x, y = node.get_name()
            value = node.get_value()
            neighbours = node.get_neighbours()
            nodes.append(((x, y), value, neighbours))

        print(nodes)

    def add_neighbour(self, name, neighbour, distance):
        for node in self.nodes:
            if node.get_name == neighbour:
                neighbour = node

        for node in self.nodes:
            if node.get_name() == name:
                node.add_neighbour(neighbour, distance)

    def get_neighbours(self, node):
        for i in self.nodes:
            if i.get_name() == node:
                return i.get_neighbours()

    def get_value(self, node):
        for i in self.nodes:
            if i.get_name() == node:
                return i.get_value()

