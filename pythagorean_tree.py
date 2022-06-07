import matplotlib.pyplot as plt
import numpy
from math import *

class Shape:
    def __init__(self, angle, base_size, x, y):
        self.angle = angle
        self.base_size = base_size
        self.x = x
        self.y = y
        self.unit_x = numpy.array([])
        self.unit_y = numpy.array([])
        self.kinder = None
    def draw(self, tree_plt):
        scaled_x = self.unit_x * self.base_size
        scaled_y = self.unit_y * self.base_size
        xs, ys = transform(scaled_x, scaled_y, self.x, self.y, self.angle)
        tree_plt.plot(xs, ys, color = 'green')



class Square(Shape):
    def __init__(self, angle, base_size, x, y):
        Shape.__init__(self, angle, base_size, x, y)
        self.unit_x = numpy.array([-.5, -.5, .5, .5, -.5])
        self.unit_y = numpy.array([0., 1., 1.,0., 0.])
    def child(self):
        angle = self.angle
        base_size = self.base_size
        x, y = transform(0, self.base_size, self.x, self.y, self.angle)
        return Triangle(angle, base_size, x, y)
    def children(self):
        return [self.child()]


class Triangle(Shape):
    def __init__(self, angle, base_size, x, y):
        Shape.__init__(self, angle, base_size, x, y)
        self.unit_x = numpy.array([0., .5, 0, -.5, 0])
        self.unit_y = numpy.array([0., 0.,.5,0.,0.])
    def child1(self):
        angle = self.angle + 45.
        base_size = self.base_size * sqrt(1./2.)
        x, y = transform(-.25 * self.base_size, .25 * self.base_size, self.x, self.y, self.angle)
        return Square(angle, base_size, x, y)
    def child2(self):
        angle = self.angle - 45.
        base_size = self.base_size * sqrt(1./2.)
        x, y = transform(.25 * self.base_size, .25*self.base_size , self.x, self.y, self.angle)
        return Square(angle, base_size, x, y)
    def children(self):
        return [self.child1(), self.child2()]


class Node:
    def __init__(self):
        self.item = null
        self.type = ""
        self.kinder = []


class P_Tree:
    def __init__(self, base_size, n_levels):
        self.trunk = Square(0., base_size, 0, 0)
        self.n_levels = n_levels
        self.grow_Tree(self.trunk, n_levels)
    def grow_Tree(self, node, n):
        if n > 1:
            node.kinder = node.children()
            for x in node.kinder:
                self.grow_Tree(x, n-1)
    def draw_Tree(self, node, plt):
        node.draw(plt)
        if node.kinder != None:
            for x in node.kinder:
                self.draw_Tree(x, plt)
        

def transform(x, y, x_offset, y_offset, angle):
    x_new = (x * cos(angle * pi/180.)) + (-y * sin(angle * pi/180.))  + x_offset
    y_new = (x * sin(angle * pi/180.)) + (y * cos(angle * pi/180.))  + y_offset
    return x_new, y_new


#TEST CODE:
#tri = Triangle(0., 5., 2., 4.)
#tri.draw(plt)
#squ = Square(45., 5, 2, 4.)
#squ.draw(plt)

#squ = Square(45., 5, 2, 4.)
#squ.draw(plt)
#squ_2 = Square(0, 5, 2, 4.)
#squ_2.draw(plt)
#tri = squ.child()
#tri.draw(plt)
#squ_3 = tri.child1()
#squ_3.draw(plt)
#plt.show()

print("calculating...")
pt = P_Tree(1.,23)
pt.draw_Tree(pt.trunk, plt)
plt.show()
