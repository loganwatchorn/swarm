from Vector import Vector

class Scanner:
    def __init__(self, holder)

class Agent:
    def __init__(self, x, y, board, id):
        self.x = x
        self.y = y
        self.board = board
        self.id = id
        self.direction = Vector(1, 0)
        self.scanners


    def calculate_step(self):
        return [self.x, self.y]


    def move_to(self, position):
        x = position[0]
        y = position[1]

        self.board.remove_from_point(self.x, self.y)

        self.x = x
        self.y = y
        self.board.place_on_point(self, x, y)
