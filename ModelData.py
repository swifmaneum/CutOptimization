class ModelData(object):

    def __init__(self, panel, parts):
        self.sheetLength = panel.side_one
        self.sheetWidth = panel.side_two

        self.rect_size = []
        self.valid_shapes = []
        for part in parts:
            if part.is_symmetric():
                if [part.side_one, part.side_two] not in self.rect_size:
                    self.rect_size.append([part.side_one, part.side_two])
                self.valid_shapes.append({self.rect_size.index([part.side_one, part.side_two]) + 1})
            else:
                if [part.side_one, part.side_two] not in self.rect_size:
                    self.rect_size.append([part.side_one, part.side_two])
                    self.rect_size.append([part.side_two, part.side_one])
                self.valid_shapes.append({self.rect_size.index([part.side_one, part.side_two]) + 1,
                                          self.rect_size.index([part.side_two, part.side_one]) + 1})

        self.rect_offset = []
        for _ in self.rect_size:
            self.rect_offset.append([0, 0])

        self.shape = []
        for i in range(0, len(self.rect_size)):
            self.shape.append({i + 1})

        self.nObjects = len(parts)
        self.nRectangles = len(self.rect_size)
        self.nShapes = len(self.shape)

    def copy_data_to(self, instance):
        for key, value in instance.input.items():
            instance[key] = getattr(self, key)
        return instance
