import sys
import time

import world.text.world as module
if (len(sys.argv) > 1):
    if sys.argv[1] == 'turtle':
        import world.turtle.world as module
    elif sys.argv[1] == 'text':
        import world.text.world as module

positions = module.positions
from collections import deque

direction = None

# setup lists
walls = []
path = []
visited = set()
frontier = deque()
solution = {}                          # solution dictionary

def get_direction(command_arg):
    global direction
    valid_directions = ['top', 'bottom', 'left', 'right']
    if (command_arg == ''):
        direction = ''
        return (True)
    elif (command_arg in valid_directions):
        direction = command_arg
        return (True)
    return (False)


def top_end():
    end = []
    y_start = 200
    x_start = -100
    while(x_start != 100):
        if ((x_start, y_start) not in positions):
            end.append((x_start, y_start))
        x_start += 10
    return (end[0])


def bottom_end():
    end = []
    y_start = -190
    x_start = -100
    while(x_start != 90):
        if ((x_start, y_start) not in positions):
            end.append((x_start, y_start))
        x_start += 10
    return (end[0])


def left_end():
    end = []
    y_start = 200
    x_start = -100
    while(y_start != -190):
        if ((x_start, y_start) not in positions and x_start == -100):
            end.append((x_start, y_start))
        y_start -= 10
    return (end[0])


def right_end():
    end = []
    y_start = 200
    while(y_start != -200):
        x_start = -100
        while(x_start != 100):
            if ((x_start, y_start) not in positions and x_start == 90):
                end.append((x_start, y_start))
            x_start += 10
        y_start -= 10
    return (end[0])


def get_end_position():
    if (direction == "top" or direction == ""):
        position = top_end()
    elif (direction == "bottom"):
        position = bottom_end()
    elif (direction == "left"):
        position = left_end()
    elif (direction == "right"):
        position = right_end()
    return (position)


def find_path(start_x, start_y, end_x, end_y, obstacles):
    route = []
    route.append((start_x, start_y))
    solution = {}
    solution[start_x, start_y] = (start_x, start_y)
    visited = []
    n = 10

    while (True):
        if (len(route) == 0):
            break

        current = route[0]
        (x, y) = current
        path = []

        if ((x - n, y) not in obstacles and (x - n, y) not in visited and (x - n) >= -100):
            #check the left hand side
            route.append((x - n, y))
            solution[x - n, y] = (x, y)
            visited.append((x - n, y))
        if ((x + n, y) not in obstacles and (x + n, y) not in visited and (x + n) <= 100):
            #check the right hand side
            route.append((x + n, y))
            solution[x + n, y] = (x, y)
            visited.append((x + n, y))
        if ((x, y - n) not in obstacles and (x, y - n) not in visited and (y - n) >= -200):
            #check bottom
            route.append((x, y - n))
            solution[x, y - n] = (x, y)
            visited.append((x, y - n))
        if ((x, y + n) not in obstacles and (x, y + n) not in visited and (y + n) <= 200):
            #check top
            route.append((x, y + n))
            solution[x, y + n] = (x, y)
            visited.append((x, y + n))
        route.pop(0)
    #print(solution)
    while (True):
        path.append((end_x, end_y))
        if (start_x, start_y) == (end_x, end_y):
            break
        (end_x, end_y) = solution[end_x, end_y]
    path.reverse()
    return (path)


def mazerunner(robot_name, command_arg):
    (start_x, start_y) = (0, 0)
    module.current_position = (start_x, start_y)
    end_point = get_end_position()
    obs = module.positions
    path = find_path(start_x, start_y, end_point[0], end_point[1], obs)

    return (path)
