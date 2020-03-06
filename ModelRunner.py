import random

from minizinc import Instance, Model, Solver
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from Part import Part

model = Model("./cutting_min_xy.mzn")
solver = Solver.lookup("chuffed")
instance = Instance(solver, model)

panel = Part(2000, 2000)
# parts = [Part(2000, 4000), Part(2000, 2000), Part(1000, 2000), Part(500, 2000), Part(2000, 500)]
parts = [Part(538, 474), Part(538, 474), Part(541, 70), Part(541, 70), Part(596, 144), Part(596, 144),
         Part(596, 144), Part(596, 144), #Part(596, 144), Part(596, 144),
         Part(562, 80), Part(562, 80), Part(562, 560), Part(562, 560), Part(1800, 100), Part(1800, 100),
         Part(1800, 100), Part(1800, 100), ]
# parts = [Part(1800, 100), Part(1800, 100), Part(762, 574), Part(762, 574), Part(762, 574), Part(762, 574)]
#parts = [Part(1800, 100), Part(1800, 100), Part(1800, 100), Part(1800, 100)]

instance["nParts"] = len(parts)

instance["length"] = list(map(lambda part: part.side_one, parts))
instance["width"] = list(map(lambda part: part.side_two, parts))

instance["plateLength"] = panel.side_one
instance["plateWidth"] = panel.side_two

result = instance.solve()

if result.solution is not None:
    print(result["x"])
    print(result["y"])
    print(result["dx"])
    print(result["dy"])
else:
    print("No solution found")

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
