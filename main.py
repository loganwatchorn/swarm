from sys import argv, stdin
from Agent import Agent
from Board import Board
from Display import Display, DisplayVariant
from Vector import Vector


def get_flag(flag, default=False):
    for arg in argv:
        flag_str = "-" + flag
        if arg[0:2] == flag_str:
            return arg[2:] if len(arg) > 2 else True

    return default

display_variant = get_flag("d", DisplayVariant.standard)
if display_variant == "scanners":
    display_variant = DisplayVariant.scanners

def variant(standard, scanners):
    if display_variant == DisplayVariant.scanners:
        return scanners
    return standard

debug = get_flag("f")
height = get_flag("h", variant(56, 7))
num_agents = get_flag("n", variant(1000, 14))
width = get_flag("w", variant(211, 11))


display = Display(display_variant, debug)
board = Board(width, height)
agents = [None] * num_agents
for i in range(0, num_agents):
    position = Vector(x = i % width, y = i // width)
    agents[i] = Agent(position, board, i)
    board.place_item(position, agents[i])


display.draw(board)
for line in stdin:
    for i in range(0, num_agents):
        agents[i].calculate_next_move()
    for i in range(0, num_agents):
        agents[i].move()
    display.draw(board)
