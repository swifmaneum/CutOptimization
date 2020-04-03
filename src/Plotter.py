import random

import matplotlib.pyplot as plt
import matplotlib.patches as patches

from src.Part import Part

panel = Part(2000, 2000)

result = {"x": [820, 195, 819, 0, 474, 1358, 1357, 948, 1422, 224, 51, 224, 224, 96, 96],
          "y": [200, 674, 674, 1148, 1148, 200, 674, 1148, 1148, 242, 552, 386, 530, 0, 100],
          "dx": [538, 538, 538, 474, 474, 538, 538, 474, 474, 596, 144, 596, 596, 1800, 1800],
          "dy": [474, 474, 474, 538, 538, 474, 474, 538, 538, 144, 596, 144, 144, 100, 100]}

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
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
