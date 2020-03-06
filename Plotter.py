import random

import matplotlib.pyplot as plt
import matplotlib.patches as patches

from Part import Part

panel = Part(2000, 2000)

result = {"x": [1, 2, 0, 1, 0, 1],
          "y": [140, 240, 340, 814, 0, 70],
          "dx": [1800, 1800, 538, 538, 541, 541],
          "dy": [100, 100, 474, 474, 70, 70]}

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
xlim = (0, panel.side_one)
ylim = (0, panel.side_two)

for i in range(len(result["x"])):  # no need to draw the last two rectangles as they are placeholders
    xy = (result["x"][i], result["y"][i])
    dx = result["dx"][i]
    dy = result["dy"][i]

    random_color = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
    ax1.add_patch(
        patches.Rectangle(xy, dx, dy, color=random_color))

plt.ylim(ylim)
plt.xlim(xlim)
plt.show()
