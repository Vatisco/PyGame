import os, sys, pygame as pg
pg.init()

#Basic Variables
max_width = 720
max_height = 640
size = width, height = max_width, max_height

#colors
black = (0, 0, 0)
white = (255, 255, 255)

#Movement
velocity = 5

#Game Control
screen = pg.display.set_mode(size)
clock = pg.time.Clock()

#Loading Images
alien = pg.image.load('images/alien.jpg')

x_pos = 0
y_pos = 0
On = False

while not On:
    #basic loop
    clock.tick(60)    
    screen.fill(black)

    #Exiting if user quits
    for event in pg.event.get(): # User did something
        if event.type == pg.QUIT:
            On = True

    #Movement of the image
    keys = pg.key.get_pressed()
    if keys[pg.K_DOWN]: y_pos += velocity
    if keys[pg.K_UP]:   y_pos -= velocity
    if keys[pg.K_LEFT]:     x_pos -= velocity
    if keys[pg.K_RIGHT]:    x_pos += velocity
    
    #Enforcing a boundary for the screen
    if x_pos < 0:   x_pos = 0
    if y_pos < 0:   y_pos = 0
    if x_pos > max_width - 120:     x_pos = max_width - 120
    if y_pos > max_height - 120:    y_pos = max_height - 120

    pg.Surface.blit(screen, alien, (x_pos, y_pos))

    pg.display.flip()

pg.quit()
sys.exit()