
# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


var = []

def get_positions():
    """
    Stores the positions of
    all the obstacle in this
    Hard-coded maze
    """
    positions = []
    maze = [
"xxxxxxxxxx xxxxxxxxx",
"x     xxxx xxx    xx",
"x xxx          xx xx",
"x     xx xxxxx xx xx",
"x xxxxxx xx xx     x",
"x     xx xx     xx x",
"x xxx xx xxxxxxxxx x",
"x   x xx         x x",
"x xxx xxxxxxxxxx x x",
"x       xx    xx xxx",
"xxxxxxx x  xx xx xxx",
"xxxxxxx xxx   xx xxx",
"x       x   x x  xxx",
"  x xx xx x x xx xxx",
"x x xx xx x        x",
"x x xx    xxxxxx x x",
"x x xxxxxxxxxxxx x x",
"x xxx         xx   x",
"x xxx xxx  xx xxx xx",
"x   x xxx  xx x     ",
"x x xxxxx  xx xx xxx",
"x xxxxxxxxxxx xx xxx",
"xx            xx   x",
"x x xxxxxx xxxxx x x",
"x x xx      xxxx x x",
"x     xx xx      x x",
"xxxxx xxxxxxxxxx x x",
"x         x xxxx xxx",
"xxxxxxxxxxx        x",
"xx     xxxxxx xxxxxx",
"xx xxx        xxx  x",
"xx xxxxxxxxxxxxxx xx",
"xx           xxx  xx",
"xxxxxxx xxxxxxxx xxx",
"xxxxxxx          xxx",
"x       xxx xxx    x",
"x xx xxxxxx x   xx x",
"x xx        x x xx x",
"x    xxxxx xxxx    x",
"xxxxxxxxxx xxxxxxxxx"]

    x = -100
    y = 200

    for i in maze:
        x = -100
        for j in i:
            if (j == 'x'):
                positions.append((x, y))
            x += 10
        y -= 10
    return (positions)



def get_obstacles():
    """
    calls the function for 
    the positions of obstacles
    """
    obstacles = get_positions()
    return (obstacles)


def store_positions():
    global var
    if (var == []):
        var = get_obstacles()
        return (var)
    return (var)


def is_path_blocked(x1,y1,x2,y2):
    """
    Checks if the path that the robot
    is going to traval in, is blocked
    or not.
    """
    global var
    prev_x, prev_y = 0,0
    val = 10
    
    if (x1 == x2):  #robot going up or down
        prev_x, prev_y = (x1),(y1)
        for position_blocked in var:
            while(y1 != y2):
                if (y1 < y2):
                    if (check_y(x1, y1, var, val)):
                        return (True)
                    y1 += 1
                elif (y1 > y2):
                    if (check_y(x1, y1, var, val)):
                        return (True)
                    y1 -= 1 
        return(False)       
    elif(y1 == y2):
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
   

def check_y(x1, y1, var, val):
    for position_blocked in var:
        if (y1 in range(position_blocked[1], position_blocked[1] - val, - 1) and x1 in range(position_blocked[0], position_blocked[0] + val)):
            return (True)    
    

def check_x(x1, y1, var, val):
    for position_blocked in var:
        if (x1 in range(position_blocked[0], position_blocked[0] + val) and y1 in range(position_blocked[1], position_blocked[1] - val, - 1)):
            return (True)

