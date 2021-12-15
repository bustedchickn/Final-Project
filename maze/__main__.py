import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 

def main(screen):

    # create the cast {key: tag, value: list}
    cast = {}

    marquee = Actor()
    marquee.set_tag("marquee")
    marquee.set_text("")
    marquee.set_position(Point(1, 0))
    cast["marquee"] = [marquee]

    x = 25
    y = 18
    position = Point(x, y)
    robot = Actor()
    robot.set_tag("robot")
    
    robot.set_text("#")
    robot.set_position(position)
    cast["robot"] = [robot]

    artifacts = []
    for x in range(49):
        
        if x <= 5:
            drawing = True
        elif x>=19 and x <= 28:
            drawing = True
        elif x>=30 and x<=36:
            drawing = True
        elif x==38:
            drawing = True
        elif (x>=40 and x<=49):
            drawing = True
        
        
        
        if drawing:
            text = "l"
            #chr(random.randint(33, 34))
            description = constants.MESSAGES[x]
            # x = random.randint(1, constants.MAX_X - 1)
            y = 1
            position = Point(x, y)
            artifact = Actor()
            artifact.set_tag("artifact")
            artifact.set_description(description)
            artifact.set_color(2)
            artifact.set_bg(2)
            artifact.set_text(text)
            artifact.set_position(position)
            artifacts.append(artifact)
            drawing = False
    for x in range(49):
        
        if x < 6 :
            drawing = True
        elif x>=7 and x <= 17:
            drawing = True
        elif x==19:
            drawing = True
        elif x==23:
            drawing = True
        elif x>=30 and x<=36:
            drawing = True
        elif x==38:
            drawing = True
        elif (x>=40 and x<=49):
            drawing = True
        if drawing:
            text = "l"
            #chr(random.randint(33, 34))
            description = constants.MESSAGES[x]
            # x = random.randint(1, constants.MAX_X - 1)
            y = 2
            position = Point(x, y)
            artifact = Actor()
            artifact.set_tag("artifact")
            artifact.set_description(description)
            artifact.set_color(2)
            artifact.set_bg(2)
            artifact.set_text(text)
            artifact.set_position(position)
            artifacts.append(artifact)
            drawing = False
    for x in range(49):
        
        if x == 5:
            drawing = True
        elif x==7:
            drawing = True
        elif x==17:
            drawing = True
        elif x==19:
            drawing = True
        elif x>=21 and x<=23:
            drawing = True
        elif x>=34 and x<=44:
            drawing = True
        
        
        
        if drawing:
            text = "l"
            #chr(random.randint(33, 34))
            description = constants.MESSAGES[x]
            # x = random.randint(1, constants.MAX_X - 1)
            y = 3
            position = Point(x, y)
            artifact = Actor()
            artifact.set_tag("artifact")
            artifact.set_description(description)
            artifact.set_color(2)
            artifact.set_bg(2)
            artifact.set_text(text)
            artifact.set_position(position)
            artifacts.append(artifact)
            drawing = False
    for x in range(49):
        
        if x < 4 :
            drawing = True
        elif x == 5 :
            drawing = True
        elif x>=7 and x <= 17:
            drawing = True
        elif x==19:
            drawing = True
        elif x==21:
            drawing = True
            
        elif x>=23 and x<=27:
            drawing = True
        elif x>=29 and x<=32:
            drawing = True
        
        elif x==35:
            drawing = True
        elif (x>=37 and x<=39):
            drawing = True
        elif (x>=41 and x<=44):
            drawing = True
        elif x>=46 and x<=47:
            drawing = True
        elif x==49:
            drawing = True
        if drawing:
            text = "l"
            #chr(random.randint(33, 34))
            description = constants.MESSAGES[x]
            # x = random.randint(1, constants.MAX_X - 1)
            y = 4
            position = Point(x, y)
            artifact = Actor()
            artifact.set_tag("artifact")
            artifact.set_description(description)
            artifact.set_color(2)
            artifact.set_bg(2)
            artifact.set_text(text)
            artifact.set_position(position)
            artifacts.append(artifact)
            drawing = False
    for x in range(49):
        
        if x ==1:
            drawing = True
        elif x == 3 :
            drawing = True
        elif x == 5 :
            drawing = True
        elif x==19:
            drawing = True
        elif x==21:
            drawing = True
        elif x==25:
            drawing = True
        elif x==27:
            drawing = True
        elif x==29:
            drawing = True
        elif (x>=31 and x<=33):
            drawing = True
        elif x == 36 :
            drawing = True
        elif x>=40 and x<=44:
            drawing = True
        elif x==46:
            drawing = True
        elif x>=48 and x<=49:
            drawing = True
        if drawing:
            text = "l"
            #chr(random.randint(33, 34))
            description = constants.MESSAGES[x]
            # x = random.randint(1, constants.MAX_X - 1)
            y = 5
            position = Point(x, y)
            artifact = Actor()
            artifact.set_tag("artifact")
            artifact.set_description(description)
            artifact.set_color(2)
            artifact.set_bg(2)
            artifact.set_text(text)
            artifact.set_position(position)
            artifacts.append(artifact)
            drawing = False
#NEXT 5-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    for x in range(49):
        
        if x == 1:
            drawing = True
        elif x == 3:
            drawing = True
        elif x>=5 and x <= 6:
            drawing = True
        elif x>=8 and x <= 19:
            drawing = True
        elif x==21:
            drawing = True
        elif x==23:
            drawing = True
        elif x==25:
            drawing = True
        elif x==27:
            drawing = True
        elif x==29:
            drawing = True
        elif x>=33 and x<=34:
            drawing = True
        elif x>=37 and x<=44:
            drawing = True
        elif x==46:
            drawing = True
        elif (x>=48 and x<=49):
            drawing = True
        
        
        
        if drawing:
            text = "l"
            #chr(random.randint(33, 34))
            description = constants.MESSAGES[x]
            # x = random.randint(1, constants.MAX_X - 1)
            y = 6
            position = Point(x, y)
            artifact = Actor()
            artifact.set_tag("artifact")
            artifact.set_description(description)
            artifact.set_color(2)
            artifact.set_bg(2)
            artifact.set_text(text)
            artifact.set_position(position)
            artifacts.append(artifact)
            drawing = False
    for x in range(49):
        
        if x ==1 :
            drawing = True
        elif x>=5 and x <= 6:
            drawing = True
        elif x==21:
            drawing = True
        elif x==23:
            drawing = True
        elif x==25:
            drawing = True
        elif x==27:
            drawing = True
        elif x>=29 and x<=31:
            drawing = True
        elif x>=33 and x<=35:
            drawing = True
        elif x>=38 and x<=44:
            drawing = True
        elif x==46:
            drawing = True
        elif (x>=48 and x<=49):
            drawing = True
        if drawing:
            text = "l"
            #chr(random.randint(33, 34))
            description = constants.MESSAGES[x]
            # x = random.randint(1, constants.MAX_X - 1)
            y = 7
            position = Point(x, y)
            artifact = Actor()
            artifact.set_tag("artifact")
            artifact.set_description(description)
            artifact.set_color(2)
            artifact.set_bg(2)
            artifact.set_text(text)
            artifact.set_position(position)
            artifacts.append(artifact)
            drawing = False
    for x in range(49):
        
        if x == 1:
            drawing = True
        elif x==3:
            drawing = True
        elif x==5:
            drawing = True
        elif x==6:
            drawing = True
        elif x==8:
            drawing = True
        elif x==9:
            drawing = True
        elif x==11:
            drawing = True
        elif x==13:
            drawing = True
        elif x==17:
            drawing = True
        elif x==19:
            drawing = True
        elif x>=21 and x<=23:
            drawing = True
        elif x>=34 and x<=44:
            drawing = True
        
        
        
        if drawing:
            text = "l"
            #chr(random.randint(33, 34))
            description = constants.MESSAGES[x]
            # x = random.randint(1, constants.MAX_X - 1)
            y = 8
            position = Point(x, y)
            artifact = Actor()
            artifact.set_tag("artifact")
            artifact.set_description(description)
            artifact.set_color(2)
            artifact.set_bg(2)
            artifact.set_text(text)
            artifact.set_position(position)
            artifacts.append(artifact)
            drawing = False
    for x in range(49):
        
        if x < 4 :
            drawing = True
        elif x == 5 :
            drawing = True
        elif x>=7 and x <= 17:
            drawing = True
        elif x==19:
            drawing = True
        elif x==21:
            drawing = True
            
        elif x>=23 and x<=27:
            drawing = True
        elif x>=29 and x<=32:
            drawing = True
        
        elif x==36:
            drawing = True
        elif (x>=40 and x<=44):
            drawing = True
        elif x>=46 and x<=47:
            drawing = True
        elif x==49:
            drawing = True
        if drawing:
            text = "l"
            #chr(random.randint(33, 34))
            description = constants.MESSAGES[x]
            # x = random.randint(1, constants.MAX_X - 1)
            y = 9
            position = Point(x, y)
            artifact = Actor()
            artifact.set_tag("artifact")
            artifact.set_description(description)
            artifact.set_color(2)
            artifact.set_bg(2)
            artifact.set_text(text)
            artifact.set_position(position)
            artifacts.append(artifact)
            drawing = False
    for x in range(49):
        
        if x ==1:
            drawing = True
        elif x == 3 :
            drawing = True
        elif x == 5 :
            drawing = True
        elif x==19:
            drawing = True
        elif x==21:
            drawing = True
        elif x==25:
            drawing = True
        elif x==27:
            drawing = True
        elif x==29:
            drawing = True
        elif (x>=31 and x<=33):
            drawing = True
        elif x == 36 :
            drawing = True
        elif x>=40 and x<=44:
            drawing = True
        elif x==46:
            drawing = True
        elif x>=48 and x<=49:
            drawing = True
        if drawing:
            text = "l"
            #chr(random.randint(33, 34))
            description = constants.MESSAGES[x]
            # x = random.randint(1, constants.MAX_X - 1)
            y = 10
            position = Point(x, y)
            artifact = Actor()
            artifact.set_tag("artifact")
            artifact.set_description(description)
            artifact.set_color(2)
            artifact.set_bg(2)
            artifact.set_text(text)
            artifact.set_position(position)
            artifacts.append(artifact)
            drawing = False





    cast["artifact"] = artifacts

    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()

Screen.wrapper(main)