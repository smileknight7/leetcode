
from games.pz.src import image
import time
from games.pz.src.const import data


class Object_Base(image.Image):
    def __init__(self, id, pos=(0, 0)):
        self.id = id
        self.preIndexTime = 0
        self.prePosTime = 0

        super().__init__(  self.getData()['PATH']
                         , self.getData()['SIZE'],
                           pos, 0,
                           self.getData()['IMAGE_INDEX_MAX'])
        self.preIndexTime = 0
        self.prePosTime = 0

    def getData(self):
        return data[self.id]

    def getPositionCD(self):
        return self.getData()['POSITION_CD']

    def getImagedIndexCD(self):
        return self.getData()['IMAGE_INDEX_CD']
    
    def update(self):
        self.checkImageIndex()
        self.checkPosition()
    
    def checkImageIndex(self):                  # 帧动画
        if time.time() - self.preIndexTime <= self.getImagedIndexCD():      # 引入延时
            return
        self.preIndexTime = time.time()

        idx = self.pathindex + 1
        if idx >= self.pathIndexCount:
            idx = 0
        self.updateIndex(idx)                   # 调用基类函数

    def checkPosition(self):                      # 平移动画
        if time.time() - self.prePosTime <= self.getPositionCD():          # 引入延时
            return False
        self.prePosTime = time.time()
        return True
    
        # pass




class ZombieBase(Object_Base):
    def __init__(self, id, pos):
        super().__init__(id, pos)


    def checkPosition(self):                                # 调用到父类的update函数的时候，他会先调用到子类这个checkposition函数
        b = super(ZombieBase, self).checkPosition()                 # 子类调用父类的检测函数
        if b:                                                       # 主要是实现共有方法在基类中，但是独有的实现在子类中
            self.pos[0] -= 3
        else: b



class PeaBullet(Object_Base):
    def __init__(self, id, pos):
        super().__init__(id, pos)


    
    def checkPosition(self):                                # 调用到父类的update函数的时候，他会先调用到子类这个checkposition函数
        b = super(PeaBullet, self).checkPosition()                 # 子类调用父类的检测函数
        if b:                                                       # 主要是实现共有方法在基类中，但是独有的实现在子类中
            self.pos[0] += 20
        else: b