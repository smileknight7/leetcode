
GAME_SIZE = (800, 600)
GRID_SIZE = (76,96)
GRID_COUNT = (9, 5)
LEFT_TOP = (128, 65)
PATH_BACK = 'games/pz/pic/other/back.png'



# 这个是数据表




# 数据表可以体现多态性
data = {
    0: {
        'PATH': 'games/pz/pic/other/peabullet.png',
        'IMAGE_INDEX_MAX':0,
        'IMAGE_INDEX_CD': 0.1,
        'POSITION_CD': 0.1,
        'SUMMON_CD': 10000,                                        # 召唤物
        'SIZE': (32, 32),
        'SPEED': (20, 0)
        }, 
    1: {'PATH': 'games/pz/pic/zombie/0/%d.png',
        'IMAGE_INDEX_MAX': 15, 
        'IMAGE_INDEX_CD': 0.2,
        'POSITION_CD': 0.2,
        'SUMMON_CD': 10000,   
        'SIZE': (100, 128),
        'SPEED': (-3, 0),
    },

    2: {'PATH': 'games/pz/pic/other/sunlight/%d.png',
        'IMAGE_INDEX_MAX': 30, 
        'IMAGE_INDEX_CD': 0.1,
        'POSITION_CD': 0.1,
        'SUMMON_CD': 10000,                                    # 设置非法值
        'SIZE': (80, 80),
        'SPEED': (0, 3),
    },
    3: {'PATH': 'games/pz/pic/plant/sunflower/%d.png',  
        'IMAGE_INDEX_MAX': 19, 
        'IMAGE_INDEX_CD': 0.1,
        'POSITION_CD': 0.1,
        'SUMMON_CD': 2,                                      # 负责召唤物  
        'SIZE': (138, 128),
        'SPEED': (0, 0),
    },
}
