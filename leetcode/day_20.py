'''

hot problem 1



给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1：

输入：grid = [
  ['1','1','1','1','0'],
  ['1','1','0','1','0'],
  ['1','1','0','0','0'],
  ['0','0','0','0','0']
]
输出：1

'''

# 图论
# BFS入门
'''
找到一个岛屿之后要将整个岛屿淹没，把 '1' 改成 '0' 当访问标记

# BFS 经典流程！！！！！！！！！！

q = deque([起点])
标记起点已访问                      # ← 起点也要标记

while q:
    当前 = q.popleft()              # 从头部取
    for 每个方向:
        邻居 = 当前 + 方向
        if 邻居在界内 and 邻居未访问:
            标记邻居已访问           # ← 在这里标记，不是出队时
            q.append(邻居)          # 加到尾部


'''
grid = [
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0']
]


# 动作淹没陆地
# 需求：网络本身， 计数器
# 怎么扩散：向四个方向扩散 DIRS = [(0,1),(1,0),(0,-1),(-1,0)] 
# 停止时间：遍历全部四个方向

from collections import deque                       # deque是双端对列--->
def numIslands(grid):
    if not grid or grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    DIRS = [(0,1),(1,0),(0,-1),(-1,0)]
    count = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                grid[i][j] = '0'
                # BFS淹没陆地
                q = deque([(i,j)])
                while q:
                    r, c = q.popleft()
                    for dr, dc in DIRS:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                            grid[nr][nc] = '0'  # 淹没陆地
                            q.append((nr, nc))
    return count

# 这个是手写深度优先搜索的方式
# class Solution:
#     def dfs(self, grid, r, c):
#         grid[r][c] = 0
#         nr, nc = len(grid), len(grid[0])
#         for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
#             if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
#                 self.dfs(grid, x, y)

#     def numIslands(self, grid: List[List[str]]) -> int:
#         nr = len(grid)
#         if nr == 0:
#             return 0
#         nc = len(grid[0])

#         num_islands = 0
#         for r in range(nr):
#             for c in range(nc):
#                 if grid[r][c] == "1":
#                     num_islands += 1
#                     self.dfs(grid, r, c)
        
#         return num_islands




# 回溯

# 回溯三个要素
# 1 路径
# 2 选择列表
# 3 结束条件


# 要将这个问题相成做选择的事情，第一个选什么，第二个选什么，第三个选什么
'''

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]





回溯的通用流程！！！！！！

def backtrack(路径, 选择列表):
    if 满足结束条件:
        收集结果（记得拷贝！）
        return

    for 选择 in 选择列表:
        做选择
        backtrack(新路径, 新选择列表)
        撤销选择
'''

nums = [1,2,3]
def permute(nums):
    n = len(nums)
    res = []
    path = []
    used = [False] * n

    def backtrack():            # 这里实际上构建了一个递归！！！！！！
        if len(path) == n:
            res.append(path[:])         # 记得拷贝
            return
        for i in range(n):              # 先走这行，每层具有独享 i,所有层共享 path, used, res
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            backtrack()
            path.pop()
            used[i] = False
    backtrack()
    return res
print(permute(nums))

# 链表，二叉树，图论，回溯，二分查找，栈，堆，贪心算法，动态规划，这些我应该先看哪些呢？