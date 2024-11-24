from gasp import *
from random import randint

begin_graphics()            
finished = False
robots = []
numbots = 5

class Player: 
    pass

class Robot:
    pass

def place_player():
    global player
    player = Player()
    player.x = randint(0, 63)
    player.y = randint(0, 47)

def place_robots(numbots):
    global robots
    robots = []
    for i in range(numbots):
        robot = Robot()
        robot.x = randint(0, 63)
        robot.y = randint(0, 47)
        robot.shape = Box((10 * robot.x, 10 * robot.y), 10, 10, filled=True)
        robots.append(robot)

def move_player():
    global player
   
    while True: 
        key = update_when('key_pressed') 

        while key == '5':  
            remove_from_screen(player.shape) 
            safely_place_player() 
            key = update_when('key_pressed') 
        if key == '6' and player.x < 63:
            player.x += 1
        elif key == '3':
            if player.x < 63:
                player.x += 1
            if player.y > 0:
                player.y -= 1
        elif key == '7':
            if player.x > 0:
                player.x -= 1
            if player.y < 47:
                player.y += 1
        elif key == '9':
            if player.x < 63:
                player.x += 1
            if player.y < 47:
                player.y += 1
        elif key == '1':
            if player.x > 0:
                player.x -= 1
            if player.y > 0:
                player.y -= 1
        elif key == '4' and player.x > 0:
            player.x -= 1
        elif key == '2' and player.y > 0:
            player.y -= 1
        elif key == '8' and player.y < 47:
            player.y += 1
        elif key == 5:
            pass
        move_to(player.shape, (10 * player.x + 5, 10 * player.y+5))
        break

def move_robot(robot):
    if robot.x < player.x:
        robot.x += 1
    elif robot.x > player.x:
        robot.x -= 1
    if robot.y < player.y:
        robot.y += 1
    elif robot.y > player.y:
        robot.y -= 1
    move_to(robot.shape, (10 * robot.x, 10 * robot.y))

def collided_with_robots(robots):
    return player.x == robot.x and player.y == robot.y

def collided():
    for robot in robots:
        if player.x == robot.x and player.y == robot.y:
            return True
    return False

def safely_place_player():
    global player
    place_player()
    
    while collided():
        place_player()

    player.shape = Circle((10 * player.x + 5 ,10 * player.y + 5) , 5, filled=True)


def check_collisions():
    global finished
    for robot in robots:
        if collided_with_robots(robot): 
            finished = True
            final_text =Text( "You've been caught!", (320, 220), size = 45)
            sleep(3)


#test here 
place_robots(numbots)
safely_place_player()

while not finished:
    move_player()
    for robot in robots:
        move_robot(robot)
    check_collisions()

end_graphics()   
