

from games.pz.src.const import GAME_SIZE, GRID_SIZE, GRID_COUNT, LEFT_TOP, PATH_BACK

from games.pz.src.object_base import SunFlower
from games.pz.src.image import Image

class Game():
    def __init__(self, ds):
        self.ds = ds
        self.back = Image(PATH_BACK, pathindex=0, pathIndexCount=0, size=GAME_SIZE)
        self.plants = []
        self.summons = []
        

        for i in range(GRID_COUNT[0]):
            for j in range(GRID_COUNT[1]):
                self.addSunFlower(i, j)
    def draw(self):
        self.back.draw(self.ds)                     # 设置交替绘制更新
        for plant in self.plants:
            plant.draw(self.ds)
        for summon in self.summons:
            summon.draw(self.ds)

    def update(self):
        self.back.update()
        for plant in self.plants:
            plant.update()
            if plant.hasSummon():
                summ = plant.doSummon()
                self.summons.append(summ)
        for summon in self.summons:
            summon.update()


    def addSunFlower(self, x, y):
        pos = (LEFT_TOP[0] + x * GRID_SIZE[0], LEFT_TOP[1] + y * GRID_SIZE[1])
        self.plants.append(SunFlower(3, pos=pos))
