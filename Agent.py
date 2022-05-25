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
    def __init__(self, position, board, id):
        self._board = board
        self._next_move = Vector(0, 0)
        self.id = id
        self.position = position
        self.direction = 0
        self.scanners = []

        for i in range(0, 8):
            self.scanners.append(Scanner(self, i * 45))


    def scan(self):
        for scanner in self.scanners:
            scanner.scan()


    def calculate_next_move(self):
        self.scan()
        # print([scanner.reading for scanner in self.scanners])

        self._next_move = Vector(0, 0)


    def move(self):
        self._board.move_item(self.position, self._next_move)
        self.position.add(self._next_move)


    def __repr__(self) -> str:
        return (f'Agent #{self.id},\n'
            + f'  position: {self.position},\n'
            + f'  readings: '
              + f'{str([scanner.reading for scanner in self.scanners])}')
