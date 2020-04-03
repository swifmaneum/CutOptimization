from minizinc import Instance, Model, Solver

from ModelData import ModelData
from Part import Part
from Plot import Plot
from RectangleToDraw import RectangleToDraw

model = Model("./cutting_geost.mzn")
solver = Solver.lookup("chuffed")
instance = Instance(solver, model)

panel = Part(2000, 2000)

#parts = [Part(538, 474), Part(538, 474), Part(538, 474), Part(538, 474),
#      Part(538, 474), Part(538, 474), Part(538, 474), Part(538, 474),
#      Part(538, 474),Part(538, 474), Part(538, 474), Part(538, 474), ]
# parts = [Part(2000, 3000), Part(2000, 2000), Part(1000, 2000), Part(1000, 4000)]
parts = [Part(538, 474), Part(538, 474), Part(538, 474), Part(538, 474), Part(538, 474), Part(538, 474),
         Part(538, 474), Part(538, 474), Part(538, 474), Part(596, 144), Part(596, 144), Part(596, 144),
         Part(596, 144), Part(1800, 100), Part(1800, 100)]

#parts = [Part(538, 474), Part(538, 474), Part(538, 474), Part(538, 474), Part(538, 474), Part(538, 474),
#         Part(538, 474), Part(538, 474), Part(538, 474), Part(596, 144), Part(596, 144), Part(596, 144),
#         Part(596, 144), Part(538, 100), Part(538, 100), Part(1800, 100), Part(1800, 100)]

data = ModelData(panel, parts)
data.copy_data_to(instance)
print("Solving ...")
result = instance.solve()

if result.solution is not None:
    print("Solved in: " + str(result.statistics["time"]))
    print(str(result.statistics))
    print("Objective: " + str(result.statistics["objective"]))
    print(result["x"])
    print(result["kind"])

    rectangles_to_draw = []
    for i in range(len(result["x"])):
        xy = (result["x"][i][0], result["x"][i][1])
        dx = data.rect_size[result["kind"][i] - 1][0]
        dy = data.rect_size[result["kind"][i] - 1][1]

        rectangles_to_draw.append(RectangleToDraw(xy, dx, dy))

    Plot(panel.side_one, panel.side_two).add_rectangles(rectangles_to_draw).show()
else:
    print("No solution found")
