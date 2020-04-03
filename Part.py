class Part(object):

    def __init__(self, side_one, side_two):
        self.side_one = side_one
        self.side_two = side_two

    def is_symmetric(self):
        return self.side_one == self.side_two
