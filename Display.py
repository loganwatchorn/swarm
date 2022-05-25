from enum import Enum
from Vector import Vector

class DisplayVariant(Enum):
    standard = 'standard'
    scanners = 'scanners'

class Display:
    def __new__(cls, variant, debug):
        if variant == DisplayVariant.scanners:
            display_class = ScannerDisplay
        else:
            display_class = StandardDisplay

        display = super().__new__(display_class)
        display.debug = debug
        return display


class StandardDisplay:
    def draw(self, board):
        border = "@"

        print(border * (2 + board.width()))

        for y in range(board.height() - 1, -1, -1):
            line = border

            for x in range(0, board.width()):
                if board.contains_item_at(Vector(x, y)):
                    line += "+"
                else:
                    line += " "

            line += border

            print(line)

        print(border * (2 + board.width()))


class ScannerDisplay:
    def format_scanner_reading(self, r):
        s = "  " if r is None else str(r)
        return " " + s if len(s) == 1 else s


    def agent_to_strings(self, agent):
        def format_int(i):
            s = "  " if i is None else str(i)
            return " " + s if len(s) == 1 else s

        num_lines = 7
        lines = [""] * num_lines

        for i in [0, 2, 4, 6]:
            lines[i] = "+----+----+----+"

        for i in [1, 3, 5]:
            if i == 1:
                readings = [agent.scanners[j].reading for j in [3, 2, 1]]
            elif i == 3:
                readings = [agent.scanners[4].reading,
                            agent.id,
                            agent.scanners[0].reading]
            elif i == 5:
                readings = [agent.scanners[j].reading for j in [5, 6, 7]]

            lines[i] += ("| "
                + format_int(readings[0])
                + " | "
                + format_int(readings[1])
                + " | "
                + format_int(readings[2])
                + " |")

        return lines


    def draw(self, board):
        l_border = "@ "
        r_border = " @"
        cell_divider = " @ "
        cell_width = 16
        cell_height = 7

        display_width = (len(l_border)
            + len(r_border)
            + board.width() * cell_width
            + (board.width() - 1) * len(cell_divider))

        horizontal_divider = "@"
        while len(horizontal_divider) + len(r_border) <= display_width:
            horizontal_divider += r_border

        for y in range(board.height() - 1, -1, -1):
            print(horizontal_divider)
            lines = []
            for i in range(0, cell_height):
                lines.append(l_border)

            for x in range(0, board.width()):
                if x > 0:
                    for i in range(0, len(lines)):
                        lines[i] += cell_divider

                if not board.contains_item_at(Vector(x, y)):
                    for i in range(0, len(lines)):
                        lines[i] += " " * cell_width
                else:
                    agent = board._read(Vector(x, y))
                    agent_strings = self.agent_to_strings(agent)
                    for i in range(0, len(lines)):
                        lines[i] += agent_strings[i]

            for l in lines:
                print(l + r_border)

        print(horizontal_divider)




# d1 = Display(variant = DisplayVariant.standard, debug=True)
# d1.draw_board()
#
# d2 = Display(DisplayVariant.scanners, False)
# d2.draw_board()
