from itertools import permutations


class ModelData(object):

    def __init__(self, panel, parts):
        self.sheet_length = panel.side_one
        self.sheet_width = panel.side_two
        self.sheet_height = panel.side_three

        self.rect_size = []
        self.valid_shapes = []
        for part in parts:
            indices = set()
            part_permutations = list(permutations([part.side_one, part.side_two, part.side_three]))
            for permutation in part_permutations:
                permutation_as_list = list(permutation)
                if permutation_as_list not in self.rect_size:
                    self.rect_size.append(list(permutation_as_list))
                indices.add(self.rect_size.index(permutation_as_list) + 1)
            self.valid_shapes.append(indices)

        self.rect_offset = []
        for _ in self.rect_size:
            self.rect_offset.append([0, 0, 0])

        self.shape = []
        for i in range(0, len(self.rect_size)):
            self.shape.append({i + 1})

        self.n_objects = len(parts)
        self.n_rectangles = len(self.rect_size)
        self.n_shapes = len(self.shape)

    def copy_data_to(self, instance):
        for key, value in instance.input.items():
            instance[key] = getattr(self, key)
        return instance
