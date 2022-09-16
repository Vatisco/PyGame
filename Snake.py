import os, sys, pygame as pg
from random import randint
pg.init()

#Text
my_font = pg.font.SysFont('Comic Sans MS', 48)


#snake
snake = [[352,288]] #[[x_pos, y_pos],[x_pos, y_pos], etc.]
snake_color = (109,242,27)
snakeLength = 3
fruit_pos = [0,0]
fruitmade = False

#Basic Variables
max_width = 736 # 23 wide
max_height = 608 # 19 height
size = width, height = max_width, max_height

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

#Movement
Direction = ""  # from button press
oldDirection = "" # old button press
Movement = "" # Direction that the Snake moves

#Game Control
screen = pg.display.set_mode(size)
clock = pg.time.Clock()

#Loading Images
#alien = pg.image.load('images/alien.jpg')

objectWidth = 32
x_pos = 352
y_pos = 288
On = False
Start = False
Dead = False
Won = False


# def checkBoundaries(x_pos, y_pos):
#     if x_pos < 0:   x_pos = 0
#     if y_pos < 0:   y_pos = 0
#     if x_pos > max_width - objectWidth:     x_pos = max_width - objectWidth
#     if y_pos > max_height - objectWidth:    y_pos = max_height - objectWidth

def MakeFruit():
    x_pos = randint(0, max_width/objectWidth - 1)
    y_pos = randint(0, max_height/objectWidth - 1)
    if[x_pos, y_pos] in snake:
        [x_pos, y_pos] = MakeFruit()
    
    # print(x_pos, y_pos)
    return [x_pos * objectWidth, y_pos * objectWidth]

text = my_font.render('Move to start', True, (255, 255, 255))
text_rect = text.get_rect(center=(max_width/2, max_height/2))
screen.blit(text, text_rect)
pg.display.flip()


while not On:
    while Dead == False:
        #basic loop
        clock.tick(60)    
        screen.fill(black)

        #Exiting if user quits
        for event in pg.event.get(): # User did something
            if event.type == pg.QUIT:
                On = True

        #Checking for game start
        while Start == False:
            pg.time.delay(100)
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    Start = True


        #Movement of the snake
        keys = pg.key.get_pressed()
        if keys[pg.K_DOWN] or keys[pg.K_s]: Direction = "S" #y_pos += velocity
        if keys[pg.K_UP] or keys[pg.K_w]:   Direction = "N" #y_pos -= velocity
        if keys[pg.K_LEFT] or keys[pg.K_a]:     Direction = "W" #x_pos -= velocity
        if keys[pg.K_RIGHT] or keys[pg.K_d]:    Direction = "E" #x_pos += velocity
        
        #Enforcing a boundary for the screen

        #pg.Surface.blit(screen, alien, (x_pos, y_pos))
        pg.time.delay(125)
        if Direction == "N" and oldDirection != "S": Movement = Direction; oldDirection = Direction
        if Direction == "S" and oldDirection != "N": Movement = Direction; oldDirection = Direction
        if Direction == "W" and oldDirection != "E": Movement = Direction; oldDirection = Direction
        if Direction == "E" and oldDirection != "W": Movement = Direction; oldDirection = Direction
        if Movement == "N": y_pos -= objectWidth
        if Movement == "S": y_pos += objectWidth
        if Movement == "W": x_pos -= objectWidth
        if Movement == "E": x_pos += objectWidth

        if x_pos < 0:   x_pos = 0; Dead = True
        if y_pos < 0:   y_pos = 0; Dead = True
        if x_pos > max_width - objectWidth:     x_pos = max_width - objectWidth; Dead = True
        if y_pos > max_height - objectWidth:    y_pos = max_height - objectWidth; Dead = True

        if fruitmade == False:
            fruit_pos = MakeFruit()
            fruitmade = True

        if fruit_pos in snake:
            snakeLength += 1
            fruitmade = False

        if snakeLength == (max_width/objectWidth - 1)*(max_height/objectWidth - 1):
            Won = True
            break


        index = 0
        for x in snake:
            pg.draw.rect(screen, snake_color, pg.Rect(snake[index][0] + 4, snake[index][1] + 4,objectWidth - 8,objectWidth - 8))
            if index > 0:
                #adding Green inbetween gaps
                #X axis
                if snake[index][0] > snake[index-1][0]: pg.draw.rect(screen, snake_color, pg.Rect(snake[index-1][0] + 28, snake[index][1] + 4, 8, objectWidth - 8 ))
                if snake[index][0] < snake[index-1][0]: pg.draw.rect(screen, snake_color, pg.Rect(snake[index][0] + 28, snake[index-1][1] + 4, 8, objectWidth - 8 ))
                #Y axis
                if snake[index][1] > snake[index-1][1]: pg.draw.rect(screen, snake_color, pg.Rect(snake[index][0] + 4 , snake[index-1][1] + 28, objectWidth - 8, 8 ))
                if snake[index][1] < snake[index-1][1]: pg.draw.rect(screen, snake_color, pg.Rect(snake[index-1][0] + 4 , snake[index][1] + 28, objectWidth - 8, 8 ))
            index += 1
        
        #Drawing eyes
        if(Movement == "N" or Movement == "W"): # Top left
            pg.draw.rect(screen, black, pg.Rect(snake[len(snake) - 1][0] + 7, snake[len(snake) - 1][1] + 7, 5, 5))
        if(Movement == "N" or Movement == "E"): # Top right
            pg.draw.rect(screen, black, pg.Rect(snake[len(snake) - 1][0] + 20, snake[len(snake) - 1][1] + 7, 5, 5))
        if(Movement == "S" or Movement == "W"): # Bottom left
            pg.draw.rect(screen, black, pg.Rect(snake[len(snake) - 1][0] + 7, snake[len(snake) - 1][1] + 20, 5, 5))
        if(Movement == "S" or Movement == "E"): # Bottom right
            pg.draw.rect(screen, black, pg.Rect(snake[len(snake) - 1][0] + 20, snake[len(snake) - 1][1] + 20, 5, 5))

        if fruitmade:
            pg.draw.rect(screen, red, pg.Rect(fruit_pos[0], fruit_pos[1], objectWidth, objectWidth))

        if[x_pos, y_pos] in snake:
            Dead = True

        snake.append([x_pos, y_pos])

        #correcting Snake length
        if len(snake) > snakeLength: snake.pop(0)
        pg.display.flip()
    
    if Dead:
        text = my_font.render('You lose', True, (255, 255, 255))
        text_rect = text.get_rect(center=(max_width/2, max_height/2))
        screen.blit(text, text_rect)
    
    if Won:
        text = my_font.render('You Win!', True, (255, 255, 255))
        text_rect = text.get_rect(center=(max_width/2, max_height/2))
        screen.blit(text, text_rect)
    
    pg.display.flip()
    pg.time.delay(2000)
    On = True

    

pg.quit()
sys.exit()