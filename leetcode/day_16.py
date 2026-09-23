'''

base problem 1



1275. 找出井字棋的获胜者
简单
相关标签
premium lock icon
相关企业
提示
井字棋 是由两个玩家 A 和 B 在 3 x 3 的棋盘上进行的游戏。井字棋游戏的规则如下：

玩家轮流将棋子放在空方格 (' ') 上。
第一个玩家 A 总是用 'X' 作为棋子，而第二个玩家 B 总是用 'O' 作为棋子。
'X' 和 'O' 只能放在空方格中，而不能放在已经被占用的方格上。
只要有 3 个相同的（非空）棋子排成一条直线（行、列、对角线）时，游戏结束。
如果所有方块都放满棋子（不为空），游戏也会结束。
游戏结束后，棋子无法再进行任何移动。
给你一个数组 moves，其中 moves[i] = [rowi, coli] 表示第 i 次移动在 grid[rowi][coli]。如果游戏存在获胜者（A 或 B），就返回该游戏的获胜者；如果游戏以平局结束，则返回 "Draw"；如果仍会有行动（游戏未结束），则返回 "Pending"。

你可以假设 moves 都 有效（遵循 井字棋 规则），网格最初是空的，A 将先行动

输入：moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
输出："A"
解释："A" 获胜，他总是先走

base problem 2

给你一个 m x n 的整数网格 accounts ，其中 accounts[i][j] 是第 i​​​​​​​​​​​​ 位客户在第 j 家银行托管的资产数量。返回最富有客户所拥有的 资产总量 。

客户的 资产总量 就是他们在各家银行托管的资产数量之和。最富有客户就是 资产总量 最大的客户。

 

示例 1：

输入：accounts = [[1,2,3],[3,2,1]]
输出：6
解释：
第 1 位客户的资产总量 = 1 + 2 + 3 = 6
第 2 位客户的资产总量 = 3 + 2 + 1 = 6
两位客户都是最富有的，资产总量都是 6 ，所以返回 6 

'''

moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]

# 按照move来区分奇数偶数判断A&B
# 胜利条件只有8种类
# 必须先判断赢家再判断平局
def tictactoe(moves):

    # 先构建一个3X3的棋盘
    grid = [['']*3 for _ in range(3)]
    for i, (r, c) in enumerate(moves):      # i 就是步数 ，r，c是坐标
        grid[r][c] = 'X' if i % 2 == 0 else 'O'

    # 收集的条目胜利的路线
    lines = []
    for i in range(3):
        lines.append((grid[i][0], grid[i][1], grid[i][2]))  # 行
        lines.append((grid[0][i], grid[1][i], grid[2][i]))  # 列
    lines.append((grid[0][0], grid[1][1], grid[2][2]))  # 主对角线
    lines.append((grid[0][2], grid[1][1], grid[2][0]))  # 副对角线
    
    # 判断赢家
    for a, b , c in lines:     # 这里代表棋盘上的数值
        if a == b == c and a != '':
            return 'A' if a == 'X' else 'B'
        
    # 判断平局或者未结束
    return 'Draw' if len(moves) == 9 else 'Pending'



accounts = [[1,2,3],[3,2,1]]
def maximumWealth(accounts):
    import numpy as np
    accounts = np.array(accounts)
    max_wealth = np.max(np.sum(accounts, axis=1))
    return max_wealth
max_wealth = maximumWealth(accounts)
print(max_wealth)