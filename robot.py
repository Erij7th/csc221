from gasp import *
from random import randint

begin_graphics()            
finished = False

def place_player():
    global player_circle
    player_circle = Circle((randint(0,630), randint(0, 470)), 5, filled=True) 
ball = Circle((5, 5), 5)

ball_x = 5
ball_y = 5

while ball_x < 635:
    ball_x += 4
    ball_y += 3

    move_to(ball, (ball_x, ball_y))

    sleep(0.02)
remove_from_screen(ball)

key_text = Text("a", (320, 240), size=48)

while True:
    key = update_when('key_pressed')
    remove_from_screen(key_text)
    key_text = Text(key, (320, 240), size=48)
    if key == 'q':
        break
        #def move_player():
  #  print('moving')    
   # key = update_when('key_pressed')
 #   if key == 'w' and player_y < 63:
   #     player_y += 1
    #    move_to(player_circle, (10 * player_x, 10 * player_y))
  #  elif key == 's' and player_y > 0:
     #   player_y -= 1
      #  move_to(player_circle, (10 * player_x, 10 * player_y))
  #  elif key == 'd' and player_x < 47:
     #   player_x += 1
     #   move_to(player_circle, (10 * player_x, 10 * player_y))
   # elif key == 'a' and player_x > 0:
     #   player_x -= 1
      #  move_to(player_circle, (10 * player_x, 10 * player_y))

place_player()
c = Circle((320, 200), 5)
move_to(c, (300, 220))
#while not finished:
  #  move_player()
end_graphics()   
