from copy import copy

from Vector import Vector


class Grid:
    def __init__(self, width, height):
        self._cols = []
        for x in range(0, width):
            self._cols.append([])
            for y in range(0, height):
                self._cols[x].append(None)


    def height(self):
        return len(self._cols[0])


    def width(self):
        return len(self._cols)


    def contains_point(self, position):
        [x, y] = [position.x, position.y]
        x_in_bounds = 0 <= x and x < self.width()
        y_in_bounds = 0 <= y and y < self.height()
        return x_in_bounds and y_in_bounds


    def _read(self, position):
        if self.contains_point(position):
            return self._cols[position.x][position.y]
        else:
            return None


    def _write(self, position, value):
        if self.contains_point(position):
            self._cols[position.x][position.y] = value

        contents = self._read(position)




class Board(Grid):
    def __init__(self, width, height):
        super().__init__(width, height)


    def contains_item_at(self, position):
        return self._read(position) is not None


    def place_item(self, position, item, debug=False):
        if not self.contains_item_at(position):
            self._write(position, item)


    def move_item(self, position, step):
        new_position = copy(position) + step

        if not self.contains_item_at(new_position):
            self._write(new_position, self._read(position))
            self._write(position, None)


    def scan(self, position, direction):
        p = copy(position)
        step = Vector(deg = direction)
        p += step

        distance = step.get_magnitude()

        while (self.contains_point(p) and not self.contains_item_at(p)):
            p += step
            distance += step.get_magnitude()

        return distance


    def draw_debug(self):
        for x in range(0, self.width()):
            for y in range(0, self.height()):
                point = self._read(Vector(x, y))
                id = "" if point is None else point.id
                print(f'({x}, {y}): {id}')
