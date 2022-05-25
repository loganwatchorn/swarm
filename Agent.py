from Vector import Vector

class Scanner:
    def __init__(self, owner, relative_direction):
        self.owner = owner
        self.relative_direction = relative_direction
        self.reading = None


    def get_direction(self):
        return (self.owner.direction + self.relative_direction) % 360


    def scan(self):
        self.reading = self.owner._board.scan(self.owner.position, self.get_direction())



class Agent:
    def __init__(self, x, y, board, id):
        self._board = board
        self.id = id
        self.position = Vector(x, y)
        self.direction = 0
        self.scanners = []

        for i in range(0, 8):
            self.scanners.append(Scanner(self, i * 45))


    def scan(self):
        for scanner in self.scanners:
            scanner.scan()


    def calculate_step(self):
        self.scan()

        return self.position


    def move_to(self, position):
        x = position[0]
        y = position[1]

        self._board.remove_from_point(self.x, self.y)

        self.x = x
        self.y = y
        self._board.place_on_point(self, x, y)


    def to_str(self, detailed=False):
        if not detailed:
            return "+"

        num_lines = 7
        lines = [""] * num_lines

        for i in [0, 2, 4, 6]:
            lines[i] = "+----+----+----+"

        def format_reading(r):
            s = "  " if r is None else str(r)
            return " " + s if len(s) == 1 else s

        for i in [1, 3, 5]:
            if i == 1:
                readings = [self.scanners[j].reading for j in [3, 2, 1]]
            elif i == 3:
                readings = [self.scanners[4].reading, self.id, self.scanners[0].reading]
            elif i == 5:
                readings = [self.scanners[j].reading for j in [5, 6, 7]]

            lines[i] += ("| "
                + format_reading(readings[0])
                + " | "
                + format_reading(readings[1])
                + " | "
                + format_reading(readings[2])
                + " |")

        return lines
