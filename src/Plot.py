import random

import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Plot(object):

    def __init__(self, max_x, max_y):
        fig1 = plt.figure()
        self.ax1 = fig1.add_subplot(111)
        plt.xlim(0, max_x)
        plt.ylim(0, max_y)
        plt.gca().set_aspect('equal', adjustable='box')

    def add_rectangles(self, rectangles):
        for rectangle in rectangles:
            random_color = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
            self.ax1.add_patch(
                patches.Rectangle(rectangle.xy, rectangle.dx, rectangle.dy, color=random_color))
        return self

    def show(self):
        plt.show()
