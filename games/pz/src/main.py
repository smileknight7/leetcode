

import pygame
import sys
from pygame.locals import *
from games.pz.src.image import Image
from games.pz.src.const import GAME_SIZE, GRID_SIZE, GRID_COUNT, LEFT_TOP, PATH_BACK

pygame.init()

zombie_pic = 'games/pz/pic/zombie/0/%d.png'
pea_pic = 'games/pz/pic/other/peabullet.png'


from games.pz.src.game import Game  

DS = pygame.display.set_mode(GAME_SIZE)

game = Game(DS)




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DS.fill((128,0,98))

    game.draw()
    game.update()
    pygame.display.update()