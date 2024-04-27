import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Node():
    def __init__(self, x0, y0, w, h, points):
        self.x0 = x0
        self.y0 = y0
        self.width = w
        self.height = h
        self.points = points
        self.children = []

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_points(self):
        return self.points

def recursive_subdivide(node, k):
    if len(node.points) <= k:
        return
    
    w_ = float(node.width / 2)
    h_ = float(node.height / 2)

    p = contains(node.x0, node.y0, w_, h_, node.points)
    x1 = Node(node.x0, node.y0, w_, h_, p)
    recursive_subdivide(x1, k)

    p = contains(node.x0, node.y0 + h_, w_, h_, node.points)
    x2 = Node(node.x0, node.y0 + h_, w_, h_, p)
    recursive_subdivide(x2, k)

    p = contains(node.x0 + w_, node.y0, w_, h_, node.points)
    x3 = Node(node.x0 + w_, node.y0, w_, h_, p)
    recursive_subdivide(x3, k)

    p = contains(node.x0 + w_, node.y0 + h_, w_, h_, node.points)
    x4 = Node(node.x0 + w_, node.y0 + h_, w_, h_, p)
    recursive_subdivide(x4, k)

    node.children = [x1, x2, x3, x4]
   
def contains(x, y, w, h, points):
    pts = []
    for point in points:
        if point.x >= x and point.x <= x + w and point.y >= y and point.y <= y + h:
            pts.append(point)
    return pts

def find_children(node):
    if not node.children:
        return [node]
    else:
        children = []
        for child in node.children:
            children += (find_children(child))
    return children

class QTree():
    def __init__(self, k, n):
        self.threshold = k
        self.points = []
        self.root = Node(0, 0, 16, 16, self.points)

    def add_point(self, x, y):
        self.points.append(Point(x, y))
    
    def get_points(self):
        return self.points
    
    def subdivide(self):
        recursive_subdivide(self.root, self.threshold)
    
    def graph(self):
        fig = plt.figure(figsize=(12, 8))
        plt.title("Quadtree")
        c = find_children(self.root)
        print("Number of segments: %d" %len(c))
        areas = set()
        for el in c:
            areas.add(el.width * el.height)
        print("Minimum segment area: %.3f units" %min(areas))
        for n in c:
            plt.gcf().gca().add_patch(patches.Rectangle((n.x0, n.y0), n.width, n.height, fill=False))
        x = [point.x for point in self.points]
        y = [point.y for point in self.points]
        plt.plot(x, y, 'ro') # plots the points as red dots
        plt.xlim(0, 16)
        plt.ylim(0, 16)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()
        return

# Create a quadtree with a threshold value of 2
quadtree = QTree(4, 10)

# Manually add 10 points replace (2,11), (4,10),(1,9),(5,12)
points = [(8, 7), (11, 1), (14, 6), (12, 2), (1, 15),(2,11), (4,10),(1,9),(5,12) ]
for point in points:
    quadtree.add_point(point[0], point[1])

# Subdivide the quadtree
quadtree.subdivide()

# Graph the quadtree
quadtree.graph()
