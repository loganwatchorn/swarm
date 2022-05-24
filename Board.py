from Vector import Vector


class Board:
    def __init__(self, width, height):
        self._grid = []
        for x in range(0, width):
            self._grid.append([])
            for y in range(0, height):
                self._grid[x].append(None)


    def height(self):
        return len(self._grid[0])


    def width(self):
        return len(self._grid)


    def point_is_within_bounds(self, x, y):
        x_in_bounds = 0 <= x and x < self.width()
        y_in_bounds = 0 <= y and y < self.height()

        return x_in_bounds and y_in_bounds


    def point_is_occupied(self, x, y):
        return self.point_is_within_bounds(x, y) and self._grid[x][y] is not None


    def read_point(self, x, y):
        if self.point_is_within_bounds(x, y) and self.point_is_occupied(x, y):
            return self._grid[x][y]
        else:
            return None


    def place_on_point(self, item, x, y):
        if not self.point_is_occupied(x, y):
            self._grid[x][y] = item


    def remove_from_point(self, x, y):
        self._grid[x][y] = None


    def scan(self, step, from_x, from_y):
        point = Vector(from_x, from_y)
        point.add(step)

        distance = 0

        while True:
            if (not self.point_is_within_bounds(point.x, point.y)
                or self.point_is_occupied(point.x, point.y)):
                return distance

            point.add(step)
            distance += 1


    def draw(self):
        border = "@"

        print(border * (2 + self.width()))

        for y in range(self.height() - 1, -1, -1):
            line = border

            for x in range(0, self.width()):
                if self.point_is_occupied(x, y):
                    line += str(self.read_point(x, y).id)
                else:
                    line += " "

            line += border

            print(line)

        print(border * (2 + self.width()))


        def debug(self):
            for x in range(0, self.width()):
                for y in range(0, self.height()):
                    point = self.read_point(x, y)
                    id = "" if point is None else point.id
                    print(f'({x}, {y}): {id}')
