from sys import argv, stdin

from agents import Agent
from space import Vector
from space.GridSpace import GridSpace, GridVector
from display import Display, DisplayVariant


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
space = GridSpace(width, height)
agents = [None] * num_agents
for i in range(0, num_agents):
    position = GridVector([i % width, i // width])
    agents[i] = Agent(position, space, i)
    space.place_item(position, agents[i])


display.draw(space)
for line in stdin:
    for i in range(0, num_agents):
        agents[i].calculate_next_move()
    for i in range(0, num_agents):
        agents[i].move()
    display.draw(space)
