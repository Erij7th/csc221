from gasp import *
from random import randint

high_score = 0


class Player: 
    pass

class Robot:
    def __init__(self, lives=1):
        self.lives = lives

def place_player():
    global player
    player = Player()
    player.x = randint(0, 63)
    player.y = randint(0, 47)

def safely_place_player():
    global player
    place_player()
    
    while collided(player, robots):
        place_player()

    player.shape = Circle((10 * player.x + 5 ,10 * player.y + 5) , 5, filled=True)

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

def place_robots(numbots):
    global robots

    robots = []

    while len(robots) < numbots:
        robot = Robot(lives=randint(1, 3))
        robot.x = randint(0, 63)
        robot.y = randint(0, 47)
        if not collided(robot, robots):
            if robot.lives > 1:
                robot.shape = Box((10 * robot.x, 10 * robot.y), 10, 10, filled=True, color = 'red')
            else: 
                robot.shape = Box((10 * robot.x, 10 * robot.y), 10, 10, color='green')
            robots.append(robot)


def move_robots():
    global junk
    for robot in robots:
        if robot.x < player.x:
            robot.x += 1
        elif robot.x > player.x:
            robot.x -= 1
        if robot.y < player.y:
            robot.y += 1
        elif robot.y > player.y:
            robot.y -= 1

        move_to(robot.shape, (10 * robot.x, 10 * robot.y))

        crashed_robot = robot_crashed(robot)
        if crashed_robot:
            crashed_robot.lives -= 1
            if crashed_robot.lives == 0:
                remove_from_screen(crashed_robot.shape)
                robots.remove(crashed_robot)
                crashed_robot.shape = Box((10 * crashed_robot.x, 10 * crashed_robot.y), 10, 10, filled = True, color = 'gray')
                junk.append(crashed_robot)
                
def collided(thing1, list_of_things):
    for thing2 in list_of_things:
        if thing1.x == thing2.x and thing1.y == thing2.y:
            return True
    return False

def robot_crashed(the_bot):
    for a_bot in robots:
        if a_bot == the_bot:
            return False
        if a_bot.x == the_bot.x and a_bot.y == the_bot.y:
            return a_bot
    return False

def check_collisions():
    global finished, robots, junk, score

    if collided(player, robots + junk): 
            finished = True
            final_text =Text( "You've been caught!", (320, 220), size = 45)
            sleep(3)
            return

    surviving_robots = []

    for robot in robots:
        if collided(robot, junk):
            continue

        jbot = robot_crashed(robot) 
        if jbot:
            jbot.lives -= 1
            if jbot.lives == 0:
                remove_from_screen(jbot.shape)
                jbot.shape = Box((10 * jbot.x, 10 * jbot.y), 10, 10, filled=True)
                junk.append(jbot)
                score += 1
                print(f"Score: {score}")
        else:
            surviving_robots.append(robot)

    robots = []
    for robot in surviving_robots:
        if not collided(robot, junk):
            robots.append(robot)

    if not robots:
        finished = True
        Text("YOU WIN!", (120, 240), size=36)
        sleep(3)
        return


#test here
while True:
    level = 1 
    numbots = 10 
    score = 0
    print(f"High Score: {high_score}")

    while True:
        finished = False
        robots = []
        junk = []

        begin_graphics()

        place_robots(numbots)
        safely_place_player()

        while not finished:
            move_player()
            move_robots()
            check_collisions()

        end_graphics()

        if not robots:
            level += 1
            numbots += 5
        else: 
            break 

    if score > high_score:
        high_score = score
    print(f"Final Score: {score}")
    print(f"High Score: {high_score}")

    answer = input("Would you like another game? (yes or no): ")
    if answer.lower() != 'yes':
        break 
