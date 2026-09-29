


# 动态规划

'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？


'''
# 这个和回溯问题很像，问有几种路径----->动态规划
#                   问具体几种路径实现方式---->回溯



# 到第 2 阶，共 2 种走法:
#     1 + 1
#     2

# 到第 3 阶，共 3 种走法:
#     1 + 1 + 1
#     2 + 1
#     1 + 2

# 到第 4 阶，共 5 种走法:
#     1 + 1 + 1 + 1
#     2 + 1 + 1
#     1 + 2 + 1
#     1 + 1 + 2
#     2 + 2
#  把第四阶，以最后一步怎么走的形式拆差分后（发现就是前两步的走法）

# 【最后一步爬 1】共 3 种 —— 说明之前站在第 3 阶
#     1 + 1 + 1 + 1   把最后那个 1 去掉 →  1 + 1 + 1   这是到第3阶的走法
#     2 + 1 + 1   把最后那个 1 去掉 →  2 + 1   这是到第3阶的走法
#     1 + 2 + 1   把最后那个 1 去掉 →  1 + 2   这是到第3阶的走法

n = 5 
def climbStairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2                       # 2节楼梯只有两种方式
    for i in range(3, n + 1):       # 第3到n节楼梯
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]



# 二分查找

'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。


'''
nums = [1,3,5,6]
target = 5
def searchInsert(nums, target):
    left, right = 0, len(nums) - 1          # 闭区间写法
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1          # 这里是排除mid本身
        else:
            right = mid - 1
    return left



# 贪心算法
'''


121. 买卖股票的最佳时机
简单
相关标签
premium lock icon
相关企业
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。


'''

# 这就是把 O(n²) 降到 O(n) 的那一步——用一个变量记住历史信息，代替回头重算。!!!


prices = [7,1,5,3,6,4]


# 如果我今天（第 i 天）卖出，能赚多少
# 找到前面一天的最小值


'''
① 重复什么动作    看今天的价格，算"今天卖出能赚多少"，并更新历史最低价
② 需要什么变量    历史最低价、目前为止的最大利润
③ 一轮后什么变了  这两个变量各自可能被刷新
④ 什么时候停      遍历完所有天

'''
 
def maxProfit(prices):
    if not prices:
        return 0
    min_price = prices[0]   
    best = 0
    for p in prices[1:]:
        best = max(best, p - min_price)
        min_price = min(min_price, p)
    return best


# 图论
'''
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 

输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4
'''

grid = [[2,1,1],[1,1,0],[0,1,1]]



# 这个题也是bfs
def orangesRotting(grid):
    from collections import deque
    m, n = len(grid), len(grid[0])
    DIRS = [(0,1),(1,0),(0,-1),(-1,0)]
    q = deque()
    fresh = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:             # 所有烂橘子一次入对
                q.append((i,j))
            elif grid[i][j] == 1:
                fresh += 1                  # 统计新鲜橘子数量
    
    minutes = 0
    while q and fresh > 0:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr,nc))
        minutes += 1
    return minutes if fresh == 0 else -1