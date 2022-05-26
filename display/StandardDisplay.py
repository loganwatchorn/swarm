class StandardDisplay:
    def draw(self, space):
        border = "@"

        print(border * (2 + space.width()))

        for y in range(space.height() - 1, -1, -1):
            line = border

            for x in range(0, space.width()):
                if space.point_occupied(Vector([x, y])):
                    line += "+"
                else:
                    line += " "

            line += border

            print(line)

        print(border * (2 + space.width()))
