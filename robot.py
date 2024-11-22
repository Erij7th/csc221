from gasp import *
from random import randint

begin_graphics()            
finished = False

def place_robot():
    global robot_x, robot_y, robot_shape
    robot_x = randint(0, 63)
    robot_y = randint(0, 47)
    robot_shape = Box((10 * robot_x, 10 * robot_y), 10, 10, filled=False)
def place_player():
    global player_x, player_y, player_shape
    player_x = randint(0, 63)
    player_y = randint(0, 47)
    player_shape = Circle((10 * player_x + 5 ,10 * player_y + 5) , 5, filled=True)

ball = Circle((5, 5), 5)
ball_x = 5
ball_y = 5
while ball_x < 635:
    ball_x += 4
    ball_y += 3
    move_to(ball, (ball_x, ball_y))
    sleep(0.02)
remove_from_screen(ball)

def move_player():
    global player_x, player_y, player_shape
    key = update_when('key_pressed')
    if key == '6' and player_x < 63:
        player_x += 1
    elif key == '3':
        if player_x < 63:
            player_x += 1
        if player_y > 0:
            player_y -= 1
    elif key == '7':
        if player_x > 0:
            player_x -= 1
        if player_y < 47:
            player_y += 1
    elif key == '9':
        if player_x < 63:
            player_x += 1
        if player_y < 47:
            player_y += 1
    elif key == '1':
        if player_x > 0:
            player_x -= 1
        if player_y > 0:
            player_y -= 1
    elif key == '4' and player_x > 0:
        player_x -= 1
    elif key == '2' and player_y > 0:
        player_y -= 1
    elif key == '8' and player_y < 47:
        player_y += 1
    elif key == 5:
        pass
        player_x += 3
    move_to(player_shape, (10 * player_x + 5, 10 * player_y+5))

def move_robot():
    global robot_x, robot_y, robot_shape
    if robot_x < player_x:
        robot_x += 1
    elif robot_x > player_x:
        robot_x -= 1
    if robot_y < player_y:
        robot_y += 1
    elif robot_y > player_y:
        robot_y -= 1
    move_to(robot_shape, (10 * robot_x, 10 * robot_y))
#test here       
place_player()
place_robot()
c = Circle((320, 200), 5)
move_to(c, (300, 220))
while not finished:
    move_player()
    move_robot()
end_graphics()   
