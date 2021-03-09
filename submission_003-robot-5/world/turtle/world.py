import sys
import turtle
import import_helper

obstacles = import_helper.dynamic_import(sys.argv[len(sys.argv) - 1])
if (sys.argv[len(sys.argv) - 1] == "turtle"):
    width = 4
else:
    width = 9


draw = turtle.Turtle()

# variables tracking position and direction
current_position = 0
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0
STEPS = 0
positions = obstacles.store_positions()

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

def print_obstacles():
    """
    does nothing in the graphics-based world
    """
    pass


def reset_variables():
    """
    Restores the variables to their default values
    """
    global position_x, position_y, current_direction_index
    position_x = 0
    position_y = 0
    current_direction_index = 0

    
def move_cusor_to_position():
    """
    Moves cursor to starting position, before
    drawing the boundaries
    """
    draw.color("red")
    draw.up()
    draw.goto(-100, 200)
    draw.down()


def draw_shape():
    """
    Draws the boundaries the limit the
    robot in the Graphics-based world
    """
    for i in range(4):
        if (i % 2 == 0):
            draw.forward(200)
        else:
            draw.forward(400)
        draw.right(90)


def draw_obstacles(item):
    """
    Draws obstacles in the Graphics-based world
    """
    draw.begin_fill()
    draw.up()
    draw.goto(item)
    draw.down()
    draw.goto(item[0] + width, item[1])
    draw.goto(item[0] + width, item[1] - width)
    draw.goto(item[0], item[1] - width)
    draw.goto(item[0], item[1])
    draw.up()
    draw.end_fill()


def go_Home():
    """
    After draw the boundaries, this function
    takes the cursor back to position (0,0)
    """
    draw.up()
    draw.home()
    draw.color("black")
    draw.left(90)


def draw_world():
    """
    Calls all the functions the are responsible
    for creating the graphical world
    """
    move_cusor_to_position()        #at position (-100, 200)
    draw_shape()
    turtle.tracer(n = 0)
    for item in positions:
        draw_obstacles(item)
    turtle.tracer(n = 1)
    go_Home()
    

def show_position(robot_name):
    """
    shows the current position of the robot
    """
    global current_position
    current_position = (position_x, position_y)
    return(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """
    global position_x, position_y, STEPS

    STEPS = steps
    prev_x = position_x
    prev_y = position_y

    
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        if (obstacles.is_path_blocked(prev_x, prev_y, position_x, position_y)):
            position_x = prev_x
            position_y = prev_y
            return ("blocked")
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    val = update_position(steps)
    if (val == True):
        draw.forward(steps)
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    elif (val == False):
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'
    elif (val == "blocked"):
        return True, "" + robot_name + ": Sorry, there is an obstacle in the way."


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    val = update_position(-steps)
    if (val == True):
        draw.back(steps)
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    elif (val == False):
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'
    elif (val == "blocked"):
        return True, "" + robot_name + ": Sorry, there is an obstacle in the way."


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0
    draw.right(90)
    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3
    draw.left(90)
    return True, ' > '+robot_name+' turned left.'


def reset():
    reset_variables()
    draw.seth(90)
    draw.goto(0, 0)