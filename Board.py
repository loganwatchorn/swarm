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


    def scan(self, position, direction):
        step = Vector(deg = direction)
        position.add(step)

        distance = step.get_magnitude()

        while True:
            if (not self.point_is_within_bounds(position.x, position.y)
                or self.point_is_occupied(position.x, position.y)):
                return distance

            position.add(step)
            distance += step.get_magnitude()


    def draw_simple(self):
        border = "@"

        print(border * (2 + self.width()))

        for y in range(self.height() - 1, -1, -1):
            line = border

            for x in range(0, self.width()):
                if self.point_is_occupied(x, y):
                    line += str(self.read_point(x, y).to_str())
                else:
                    line += " "

            line += border

            print(line)

        print(border * (2 + self.width()))


    def draw_detailed(self):
        l_border = "@ "
        r_border = " @"
        cell_divider = " @ "
        cell_width = 16
        cell_height = 7

        board_width = (len(l_border)
            + len(r_border)
            + self.width() * cell_width
            + (self.width() - 1) * len(cell_divider))

        horizontal_divider = "@"
        while len(horizontal_divider) + len(r_border) <= board_width:
            horizontal_divider += r_border

        for y in range(self.height() - 1, -1, -1):
            print(horizontal_divider)
            lines = []
            for i in range(0, cell_height):
                lines.append(l_border)

            for x in range(0, self.width()):
                if x > 0:
                    for i in range(0, len(lines)):
                        lines[i] += cell_divider

                if not self.point_is_occupied(x, y):
                    for i in range(0, len(lines)):
                        lines[i] += " " * cell_width
                else:
                    agent = self.read_point(x, y)
                    agent_strings = agent.to_str(detailed=True)
                    for i in range(0, len(lines)):
                        lines[i] += agent_strings[i]

            for l in lines:
                print(l + r_border)

        print(horizontal_divider)


    def draw(self, detailed=True):
        if detailed:
            self.draw_detailed()
        else:
            self.draw_simple()















    def debug(self):
        for x in range(0, self.width()):
            for y in range(0, self.height()):
                point = self.read_point(x, y)
                id = "" if point is None else point.id
                print(f'({x}, {y}): {id}')
