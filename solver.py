import sys
from PIL import Image
from Graph import Graph
import math


# try's to open the image if IOException is raised prints an error
def open_image(imgPath):
    try:
        img = Image.open(imgPath)
        return img
    except IOError:
        print("Unable to open the image")


# finds all the nodes in the graph by looking for junctions in the image
def get_nodes(img, graph):
    width, height = img.size
    # Finds the finish node from the image and adds it to the graph in position 0
    for x in range(1, width - 1):
        if img.getpixel((x, height - 1)) == 1:
            graph.add_node((x, height - 1), 0)

    # finds the start node, calculates its distance and adds it to the graph in position 0
    for x in range(1, width - 1):
        if img.getpixel((x, 0)) == 1:
            value = get_value(graph, (x, 0))
            graph.add_node((x, 0), value)

    # loops through each line on the image, if a pixel is a node adds it to the graph
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            if img.getpixel((x, y)) == 1:
                if is_node(img, (x, y)):
                    value = get_value(graph, (x, y))
                    graph.add_node((x, y), value)


# takes (x, y) of node and finds the euclidean distance between the node and
# the finish node
def get_value(graph, node):
    finish = graph.get_nodes_names()[0]
    x1, y1 = node
    x2, y2 = finish

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# takes a pixel and if 2 adjacent pixels surrounding the pixel are white, return true
def is_node(img, pixel):
    x, y = pixel

    if img.getpixel((x, y - 1)) == 1 and img.getpixel((x + 1, y)) == 1:
        return True
    elif img.getpixel((x + 1, y)) == 1 and img.getpixel((x, y + 1)) == 1:
        return True
    elif img.getpixel((x, y + 1)) == 1 and img.getpixel((x - 1, y)) == 1:
        return True
    elif img.getpixel((x - 1, y)) == 1 and img.getpixel((x, y - 1)) == 1:
        return True
    else:
        return False


# loops through all nodes in the graph and finds their neighbours from the image
def get_neighbours(img, graph):
    width, height = img.size
    for x, y in graph.get_nodes_names():
        if y == 0:
            graph.add_neighbour((x, y), (x, y + 1), 1)
        elif y == (height - 1):
            graph.add_neighbour((x, y), (x, y - 1), 1)
        else:
            for direction in find_directions(img, (x, y)):
                traverse(img, graph, (x, y), direction)


# takes a node and finds which directions can be travelled based on the surrounding pixels
def find_directions(img, node):
    x, y = node
    directions = []

    if img.getpixel((x, y - 1)) == 1:
        directions.append(0)
    if img.getpixel((x + 1, y)) == 1:
        directions.append(1)
    if img.getpixel((x, y + 1)) == 1:
        directions.append(2)
    if img.getpixel((x - 1, y)) == 1:
        directions.append(3)

    return directions


# given a node and direction will traverse the image along the path until it finds a node
# or hits a wall, if a node is found it will add the node as a neighbour
def traverse(img, graph, node, direction):
    x, y = node
    counter = 0
    while img.getpixel((x, y)) == 1:
        if (x, y) in graph.get_nodes_names() and (x, y) != node:
            graph.add_neighbour(node, (x, y), counter)
            break

        counter += 1

        # 0 = up, 1 = right, 2 = down, 3 = left
        if direction == 0:
            y -= 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y += 1
        elif direction == 3:
            x -= 1
        else:
            break


def test(img, nodes):
    red = (255, 0, 0)
    img = img.convert('RGB')
    px = img.load()

    for node in nodes:
        x, y = node
        px[x, y] = red

    img.save("test.png")


def main(imgPath):
    img = open_image(imgPath)
    graph = Graph()

    get_nodes(img, graph)
    get_neighbours(img, graph)

    # test(img, graph.get_nodes_names())

    graph.print_nodes()


if __name__ == "__main__":
    # get path name from the command line
    imgPath = sys.argv[1]
    main(imgPath)





