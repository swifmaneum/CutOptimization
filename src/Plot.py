import random

import matplotlib.pyplot as plt


class Plot(object):

    def __init__(self, max_x, max_y, max_z):
        fig1 = plt.figure()
        self.ax1 = fig1.add_subplot(111, projection='3d')
        self.ax1.set(xlim=[0, max_x], ylim=[0, max_y], zlim=[0, max_z])

    def add_rectangles(self, rectangles):
        for rectangle in rectangles:
            random_color = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
            self.ax1.bar3d(rectangle.xyz[0], rectangle.xyz[1], rectangle.xyz[2], rectangle.dx, rectangle.dy,
                           rectangle.dz, shade=True, color=random_color)
        return self

    def show(self):
        plt.show()
