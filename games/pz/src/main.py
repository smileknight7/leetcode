

import pygame
import sys
from pygame.locals import *
from games.pz.src.image import Image
from games.pz.src.const import GAME_SIZE, GRID_SIZE, GRID_COUNT, LEEFT_SIZE, PATH_BACK
from games.pz.src.object_base import Object_Base, ZombieBase, PeaBullet
pygame.init()

zombie_pic = 'games/pz/pic/zombie/0/%d.png'
pea_pic = 'games/pz/pic/other/peabullet.png'




DS = pygame.display.set_mode(GAME_SIZE)
image = Image(PATH_BACK,pathindex=0, pathIndexCount=0, size=GAME_SIZE)
zom = ZombieBase(1, pos=(600, 200))
pb = PeaBullet(0, pos=(0, 200))



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DS.fill((128,0,97))
    image.draw(DS)

    zom.draw(DS)
    #zom.doLeft()
    # zom.draw(DS)
    zom.update()
    zom.draw(DS)
    pb.update()
    pb.draw(DS)
    pygame.display.update()