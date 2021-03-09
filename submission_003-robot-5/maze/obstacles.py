import random

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

var = []

def get_obstacles():
    num_of_obstacles = random.randint(5, 10)
    obstacles = []
    global var
    for i in range(num_of_obstacles):
        obstacles.append((random.randint(min_x, max_x), random.randint(min_y, max_y)))
    var = obstacles
    return (obstacles)


def is_path_blocked(x1,y1,x2,y2):
    """
    Checks if the path that the robot
    is going to traval in, is blocked
    or not.
    """
    global var
    prev_x, prev_y = 0,0
    val = 5
    
    if (x1 == x2):
        prev_x, prev_y = (x1),(y1)
        for position_blocked in var:
            while (y1 != y2):
                if (y1 < y2):
                    if (check_y(x1, y1, var, val)):
                        return (True)
                    y1 += 1
                elif (y1 > y2):
                    if (check_y(x1, y1, var, val)):
                        return (True)
                    y1 -= 1 
        return(False)       
    elif (y1 == y2):
        prev_x, prev_y = (x1),(y1)
        for position_blocked in var:
            while(x1 != x2):
                if (x1 < x2):
                    if(check_x(x1, y1, var, val)):
                        return (True)
                    x1 += 1
                elif (x1 > x2):
                    if(check_x(x1, y1, var, val)):
                        return (True)
                    x1 -= 1
        return(False)
    return (False)
   

def store_positions():
    global var
    if (var == []):
        var = get_obstacles()
        return (var)
    return (var)


def check_y(x1, y1, var, val):
    for position_blocked in var:
        if (y1 in range(position_blocked[1], position_blocked[1] - val, - 1) and x1 in range(position_blocked[0], position_blocked[0] + val)):
            return (True)    
    

def check_x(x1, y1, var, val):
    for position_blocked in var:
        if (x1 in range(position_blocked[0], position_blocked[0] + val) and y1 in range(position_blocked[1], position_blocked[1] - val, - 1)):
            return (True)

