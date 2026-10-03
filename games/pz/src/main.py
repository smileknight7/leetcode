

import pygame
import sys
from pygame.locals import *
from games.pz.src.image import Image


pygame.init()

path = 'games/pz/pic/other/back.png'
path1 = 'games/pz/pic/zombie/0/%d.png'
position = ''




DS = pygame.display.set_mode((800, 600))
image = Image(path,pathindex=0, pathIndexCount=0, size=(800, 600))
image1 = Image(path1, pathindex=0, pathIndexCount=15, size=(100, 128), pos = (800, 200))




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DS.fill((128,0,97))
    image.draw(DS)

    image1.draw(DS)
    image1.doLeft()
    image1.draw(DS)
    image1.updateIndex((image1.pathindex + 1) % image1.pathIndexCount)
    pygame.display.update()