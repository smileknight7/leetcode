

import pygame
import sys
from pygame.locals import *
from games.pz.src.image import Image


pygame.init()



DS = pygame.display.set_mode((800, 600))

path = 'games/pz/pic/other/back.png'
# image = pygame.image.load(path)
image = Image(path)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DS.fill((128,0,97))
    image.draw(DS)
    pygame.display.update()