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
        [x, y] = [position[0], position[1]]
        x_in_bounds = 0 <= x and x < self.width()
        y_in_bounds = 0 <= y and y < self.height()
        return x_in_bounds and y_in_bounds


    def _read(self, position):
        if self.contains_point(position):
            return self._cols[position[0]][position[1]]
        else:
            return None


    def _write(self, position, value):
        if self.contains_point(position):
            self._cols[position[0]][position[1]] = value

        contents = self._read(position)
