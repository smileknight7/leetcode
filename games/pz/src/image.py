import pygame



# 封装
class Image(pygame.sprite.Sprite):
    def __init__(self, pathFmt, size, pos=(0, 0), pathindex=0, pathIndexCount=0):
        self.pathFmt = pathFmt
        self.pathindex = pathindex
        self.pathIndexCount = pathIndexCount
        self.size = size
        self.pos = list(pos)
        self.updateImage()

    def updateImage(self):
        path = self.pathFmt
        if self.pathIndexCount !=0:                             # 则例哦按段是否使用帧动画
            path = self.pathFmt % self.pathindex
        self.image = pygame.image.load(path)
        if self.size:
            self.image = pygame.transform.scale(self.image, self.size)

    def updateSize(self, size):
        self.size = size
        self.updateImage()

    def updateIndex(self, pathindex):       # 通过updateindex来实现动画
        self.pathindex = pathindex
        self.updateImage()

    def getRect(self):
        rect = self.image.get_rect()                # 这样pos就可以修改图片矩形的位置了
        rect.x, rect.y = self.pos
        return rect

    def doLeft(self):
        self.pos[0] -= 0.1

    def draw(self, ds):
        ds.blit(self.image, self.getRect())



