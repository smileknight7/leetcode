
from games.pz.src import image
import time
from games.pz.src.const import data


class Object_Base(image.Image):
    def __init__(self, id, pos=(0, 0)):
        self.id = id
        self.preIndexTime = 0
        self.prePosTime = 0
        self.preSummonTime = 0                                      # 上次召唤时间

        super().__init__(  self.getData()['PATH']
                         , self.getData()['SIZE'],
                           pos, 0,
                           self.getData()['IMAGE_INDEX_MAX'])
        self.preIndexTime = 0
        self.prePosTime = 0

    def getData(self):
        return data[self.id]
    
    def getSpeed(self):
        return self.getData()['SPEED']

    def getPositionCD(self):
        return self.getData()['POSITION_CD']

    def getImagedIndexCD(self):
        return self.getData()['IMAGE_INDEX_CD']
    
    def getSummonCD(self): 
        return self.getData()['SUMMON_CD']

    def update(self):
        self.checkSummon()
        self.checkImageIndex()
        self.checkPosition()
    
    def checkImageIndex(self):                    # 帧动画
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
        speed = self.getSpeed()
        self.pos = (self.pos[0] + speed[0], self.pos[1] + speed[1])
        return True
    
    def checkSummon(self):
        if time.time() - self.preSummonTime <= self.getSummonCD():
            return
        self.preSummonTime = time.time()
        self.preSummon()

    def preSummon(self):                           # 子类实现具体内容
        pass

    def hasSummon(self):
        pass

    def doSummon(self): 
        pass


class ZombieBase(Object_Base):
    def __init__(self, id, pos):
        super().__init__(id, pos)

    pass


class PeaBullet(Object_Base):
    def __init__(self, id, pos):
        super().__init__(id, pos)

    pass


class SunLight(Object_Base):
    def __init__(self, id, pos):
        super().__init__(id, pos)

    pass


# 这里是把speed抽提到基类中去了

# class SunLight(Object_Base):
#     def __init__(self, id, pos):
#         super().__init__(id, pos)

#     def checkPosition(self):                                # 调用到父类的update函数的时候，他会先调用到子类这个checkposition函数
#         speed = self.getSpeed()
#         b = super(SunLight, self).checkPosition()                 # 子类调用父类的检测函数
#         if b:                                                       # 主要是实现共有方法在基类中，但是独有的实现在子类中
#             self.pos = (self.pos[0] + speed[0], self.pos[1] + speed[1])
#         else: b





# 生命周期管理
# class SunFlower(Object_Base):
#     def __init__(self, id, pos):
#         super().__init__(id, pos)
    
#     def preSummon(self):
#         sl = SunLight(2, pos=(self.pos[0] + 20, self.pos[1] - 10))          # 阳光产生位置和向日葵位置接近
#         self.sunLights.append(sl)
        
#     def update(self):
#         super(SunFlower, self).update()
#         for sunLight in self.sunLights:
#             sunLight.update()

#     def draw(self, ds):
#         super(SunFlower, self).draw(ds)
#         for sunLight in self.sunLights:
#             sunLight.draw(ds)


class SunFlower(Object_Base):
    def __init__(self, id, pos):
        super().__init__(id, pos)
        self.hasSunlight = False

    def hasSummon(self):
        return self.hasSunlight

    def preSummon(self):
        self.hasSunlight = True

    def doSummon(self):
        if self.hasSummon():
            self.hasSunlight = False
            sl = SunLight(2, pos=(self.pos[0] + 20, self.pos[1] - 10))          # 阳光产生位置和向日葵位置接近
            return sl



