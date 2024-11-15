from gasp import *          # So that you can draw things

begin_graphics()            # Create a graphics window
finished = False

place_player()

while not finished:
    move_player()

end_graphics()
