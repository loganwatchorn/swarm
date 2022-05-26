from copy import copy

from .Grid import Grid
from .GridVector import GridVector


class GridSpace(Grid):
    def __init__(self, width, height):
        super().__init__(width, height)


    def point_occupied(self, position):
        return self._read(position) is not None


    def place_item(self, position, item, debug=False):
        if not self.point_occupied(position):
            self._write(position, item)


    def move_item(self, position, step):
        new_position = position + step

        if not self.point_occupied(new_position):
            self._write(new_position, self._read(position))
            self._write(position, None)


    def scan(self, position, direction):
        p = copy(position)
        step = GridVector(angles = [direction])
        p += step

        distance = step.magnitude()

        while (self.contains_point(p) and not self.point_occupied(p)):
            p += step
            distance += step.magnitude()

        return distance
