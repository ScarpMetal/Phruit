import sys, time
import pygame
from TouchSensor import TouchSensor
from GameSprite import GameSprite

from pygame.locals import *

# set up pygame
pygame.init()

#Set up the window
windowSurface = pygame.display.set_mode((900, 700), 0 , 32)
pygame.display.set_caption('Pick Up the Phone!')

img = pygame.image.load('images/bphone.png')

# SET COLORS
WHITE = (255,255,255)
PEACH = (246,176,146)

# set up fonts
basicFont = pygame.font.SysFont(None, 48)

#Set up the text
text = basicFont.render('Pick Up the Phone!', True, WHITE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = 70

# draw the white background onto the surface
windowSurface.fill(PEACH)

#Load in bananaphone image
windowSurface.blit(img, (windowSurface.get_rect().centerx-180,170))

# draw the text onto the surface
windowSurface.blit(text, textRect)

# draw the window onto the screen
pygame.display.update()

# initialize Touch Sensor
ts = TouchSensor()

# run the game loop
while True:
    ts.update()


    if ts.status(3) == ts.TOUCHED:
        print("WOOOO")
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and ts.DEBUG:
            if event.key == K_0:
                print("Key 0 was pressed")
            elif event.key == K_1:
                print("Key 1 was pressed")
            elif event.key == K_2:
                print("Key 2 was pressed")
            elif event.key == K_3:
                print("Key 3 was pressed")
            elif event.key == K_4:
                print("Key 4 was pressed")
            elif event.key == K_5:
                print("Key 5 was pressed")
            elif event.key == K_6:
                print("Key 6 was pressed")
            elif event.key == K_7:
                print("Key 7 was pressed")
            elif event.key == K_8:
                print("Key 8 was pressed")
            elif event.key == K_9:
                print("Key 9 was pressed")
            
    time.sleep(0.1)
