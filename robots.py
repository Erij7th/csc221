def place_player(player_x, player_y):
    print(circle((player_x, player), 10))

def move_player():
    print("I'm moving...")
    update_when('key_pressed')
from gasp import *          # So that you can draw things

begin_graphics()            # Create a graphics window
finished = False

place_player(300, 200)

while not finished:
    move_player()

end_graphics()


