from minizinc import Instance, Model, Solver

from src.ModelData import ModelData
from src.Part import Part
from src.Plot import Plot
from src.RectangleToDraw import RectangleToDraw

model = Model("./models/cutting_geost.mzn")
solver = Solver.lookup("chuffed")
instance = Instance(solver, model)

panel = Part(5, 3, 10)

parts = [Part(3, 3, 3), Part(2, 1, 2), Part(1, 2, 3), Part(3, 2, 3), Part(5, 1, 2), Part(8, 2, 3), Part(3, 2, 3)]

data = ModelData(panel, parts)
data.copy_data_to(instance)

print("Solving ...")
result = instance.solve()

if result.solution is not None:
    print("Solved in: " + str(result.statistics["time"]))
    print("Used area: " + str(result.statistics["objective"]))

    rectangles_to_draw = []
    for i in range(len(result["x"])):
        xyz = (result["x"][i][0], result["x"][i][1], result["x"][i][2])
        dx = data.rect_size[result["kind"][i] - 1][0]
        dy = data.rect_size[result["kind"][i] - 1][1]
        dz = data.rect_size[result["kind"][i] - 1][2]

        rectangles_to_draw.append(RectangleToDraw(xyz, dx, dy, dz))

    Plot(panel.side_one, panel.side_two, panel.side_three).add_rectangles(rectangles_to_draw).show()
else:
    print("No solution found")
