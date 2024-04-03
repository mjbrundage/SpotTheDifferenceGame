# Matt Brundage II
# 4/2/24
# SpotDifferenceGame.py

import pygame
from pygame.locals import *
from time import sleep
from random import randrange

# initialisation
pygame.init()
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h

# screen
screen = pygame.display.set_mode((width, height))
pygame.display.update()

# game
difference = pygame.image.load("images/spot_the_diff.png")
difference = pygame.transform.scale(difference, (width, height))
screen.blit(difference, (0, 0))
pygame.display.update()

zombie = pygame.image.load("images/scary_face.png")
zombie = pygame. transform.scale(zombie, (width, height))
scream = pygame.mixer.Sound("sounds/scream.wav")
sleep(randrange(5, 15))
scream.play()
screen.blit(zombie, (0, 0))
pygame.display.update()

sleep(3)
scream.stop()

# quit game
pygame.quit()