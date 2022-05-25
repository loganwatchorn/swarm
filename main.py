from sys import stdin, argv
from Agent import Agent
from Board import Board

detailed = "-d" in argv

width = 11 if detailed else 200
height = 7 if detailed else 55

board = Board(width, height)

num_agents = 14 if detailed else 1000

agents = [None] * num_agents
for i in range(0, num_agents):
    x = i % width
    y = i // width

    agents[i] = Agent(x, y, board, i)

    board.place_on_point(agents[i], x, y)

board.draw(detailed=detailed)

simulation_time = 60

steps_complete = 0
step_time = 1

# while (steps_complete + 1) * step_time < simulation_time:
for line in stdin:
    new_board = board
    for agent in agents:
        next_position = agent.calculate_step()
        agent.board = new_board
        # agent.move_to(next_position)

    board = new_board
    board.draw(detailed=detailed)
    steps_complete += 1
