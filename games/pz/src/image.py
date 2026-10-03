import pygame



# 封装
class Image(pygame.sprite.Sprite):
    def __init__(self, path):
        self.path = path
        self.image = pygame.image.load(path)
        
    def draw(self, ds):
        ds.blit(self.image, self.image.get_rect())



