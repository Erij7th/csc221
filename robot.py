from gasp import *
from random import randint

begin_graphics()            
finished = False

player_x = 0
player_y = 0
player_shape = 0

def place_player():
    global player_x, player_y, player_shape
    player_x = 55
    player_y = randint(0, 470)
    player_shape = Circle((player_x ,player_y) , 5, filled=True)

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
    key = update_when('key_pressed')
    if key == '6' and player_x < 63:
        player_x += 1
    elif key == '3':
        if player_x < 63:
            player_x += 1
        if player_y > 0:
            player_y -= 1
    move_to(player_shape, (10 * player_x + 5, 10 * player+5))

#Ftext = Text("hello", (320, 240), size=48)
#while True:
  #  text = update_when('key_pressed')
   # remove_from_screen(Ftext)
   # text = Text(text, (320, 240), size=48)
   # if text  == 'exit':
      #  break

#test here       
place_player()
c = Circle((320, 200), 5)
move_to(c, (300, 220))
move_player()
#while not finished:
  #  move_player()
end_graphics()   
