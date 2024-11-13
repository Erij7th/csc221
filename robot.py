from gasp import *
from random import randint

begin_graphics()            
finished = False

def place_player(player_x = randint(0,63), player_y = randint(0,47)):
    global player_circle
    player_circle = Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)

def move_player():
    print('moving')
    global player_x, player_y, player_circle
    key = update_when('key_pressed')
    if key == 'w' and player_y < 63:
        player_y += 1
        move_to(player_circle, (10 * player_x, 10 * player_y))
    elif key == 's' and player_y > 0:
        player_y -= 1
        move_to(player_circle, (10 * player_x, 10 * player_y))
    elif key == 'd' and player_x < 47:
        player_x += 1
        move_to(player_circle, (10 * player_x, 10 * player_y))
    elif key == 'a' and player_x > 0:
        player_x -= 1
        move_to(player_circle, (10 * player_x, 10 * player_y))

place_player()

while not finished:
    move_player()

end_graphics()   
