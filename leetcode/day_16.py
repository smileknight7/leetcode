'''
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。
请使用原地算法。

输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]
'''

# 必须分两趟：先侦察（只记录要清的行列），再执行
# 边遍历边清零会让写进去的 0 被当成"原本的 0"，引发连锁清零
# 空间 O(m+n) 版本：用两个 set 记录
matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
def set_zeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    rows, cols = set(), set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in rows:                      # 只碰要清的行列，不用全量扫描判断
        for j in range(n):
            matrix[i][j] = 0
    for j in cols:
        for i in range(m):
            matrix[i][j] = 0
    return matrix

print(set_zeroes(matrix1))


# 空间 O(1) 版本：征用第一行第一列当标记位
# matrix[i][0]=0 表示第 i 行要清，matrix[0][j]=0 表示第 j 列要清
def set_zeroes_inplace(matrix):
    m, n = len(matrix), len(matrix[0])
    first_row = any(matrix[0][j] == 0 for j in range(n))    # 先记下，马上要被征用
    first_col = any(matrix[i][0] == 0 for i in range(m))
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if first_row:                       # 必须放最后，提前清会冲掉标记
        for j in range(n):
            matrix[0][j] = 0
    if first_col:
        for i in range(m):
            matrix[i][0] = 0
    return matrix

print(set_zeroes_inplace([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))


'''
给你一个 m x n 的矩阵 matrix ，请按照顺时针螺旋顺序，返回矩阵中的所有元素。

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
'''

# 撞墙转向法：方向数组 + % 4
# 先试探下一步，出界或已访问过就右转
# 循环 m*n 次，不用判断条件，数够次数就行
matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
def spiral_order(matrix):
    if not matrix or not matrix[0]:
        return []
    m, n = len(matrix), len(matrix[0])
    DIRS = [(0,1),(1,0),(0,-1),(-1,0)]      # 右 下 左 上，row 往下增长所以"下"是 (1,0)
    seen = [[False]*n for _ in range(m)]
    r = c = d = 0
    res = []
    for _ in range(m*n):
        res.append(matrix[r][c])
        seen[r][c] = True
        nr, nc = r + DIRS[d][0], c + DIRS[d][1]
        if not (0 <= nr < m and 0 <= nc < n and not seen[nr][nc]):
            d = (d+1) % 4                   # 撞墙，右转
            nr, nc = r + DIRS[d][0], c + DIRS[d][1]
        r, c = nr, nc
    return res

print(spiral_order(matrix2))


# 边界剥皮法：O(1) 空间，四条边界层层往里收
# 那两个 if 是命门：剩单行或单列时不判会重复遍历（3x3 方阵恰好不出错，长方形才暴露）
def spiral_order_peel(matrix):
    if not matrix or not matrix[0]:
        return []
    top, bottom = 0, len(matrix)-1
    left, right = 0, len(matrix[0])-1
    res = []
    while top <= bottom and left <= right:
        for c in range(left, right+1):          # 上边
            res.append(matrix[top][c])
        top += 1
        for r in range(top, bottom+1):          # 右边
            res.append(matrix[r][right])
        right -= 1
        if top <= bottom:                       # 下边
            for c in range(right, left-1, -1):
                res.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:                       # 左边
            for r in range(bottom, top-1, -1):
                res.append(matrix[r][left])
            left += 1
    return res

print(spiral_order_peel([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))


'''
给定一个 n x n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在原地旋转图像。

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]
'''

# 坐标映射 (i,j) -> (j, n-1-i)
# 把它分解成两个简单操作：转置 + 每行反转
# 转置时 j 从 i+1 开始（只走上三角），否则每对元素换两次等于没换
matrix3 = [[1,2,3],[4,5,6],[7,8,9]]
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()                   # 原地反转，写 row = row[::-1] 无效
    return matrix

print(rotate(matrix3))


# 四元素环形交换：一趟完成
# (i,j) -> (j,n-1-i) -> (n-1-i,n-1-j) -> (n-1-j,i) -> 回到起点，四个位置构成一个环
def rotate_cycle(matrix):
    n = len(matrix)
    for i in range(n//2):                   # 圈数
        for j in range(i, n-1-i):           # 每圈只走上边一段，多一格就把转好的又转回去
            tmp = matrix[i][j]
            matrix[i][j]         = matrix[n-1-j][i]
            matrix[n-1-j][i]     = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-1-i]     = tmp
    return matrix

print(rotate_cycle([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))


'''
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。
该矩阵具有以下特性：每行的元素从左到右升序排列，每列的元素从上到下升序排列。

输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22]], target = 5
输出：True
'''

# 从右上角走楼梯：O(m+n)，不是 O(m*n)
# 右上角的元素同时是"这一行最大"和"这一列最小"，所以比较结果能唯一决定排除方向
# 左上角不行（两个方向都变大，有歧义），右下角同理
matrix4 = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    r, c = 0, n-1                       # 右上角出发
    while r < m and c >= 0:
        v = matrix[r][c]
        if v == target:
            return True
        elif v > target:
            c -= 1                      # 这一列全 >= v > target，整列排除
        else:
            r += 1                      # 这一行全 <= v < target，整行排除
    return False

print(search_matrix(matrix4, 5), search_matrix(matrix4, 20))


'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

输入：grid = [["1","1","1","1","0"],["1","1","0","1","0"],
              ["1","1","0","0","0"],["0","0","0","0","0"]]
输出：1
'''

from collections import deque

# 连通块计数的通用骨架：
#   外层双层循环负责"找新岛的起点"，BFS 负责"把整座岛淹光"
#   淹光（'1' 改 '0'）让外层后面遇到同一座岛时自动跳过，否则会按格子数重复计数
# 用 deque 而不是 list：popleft() 是 O(1)，list.pop(0) 是 O(n)
grid1 = [["1","1","1","1","0"],["1","1","0","1","0"],
         ["1","1","0","0","0"],["0","0","0","0","0"]]
def num_islands(grid):
    if not (grid and grid[0]):          # 只用一个 not，比 "not grid or not grid[0]" 不容易漏
        return 0
    m, n = len(grid), len(grid[0])
    DIRS = [(0,1),(1,0),(0,-1),(-1,0)]
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                grid[i][j] = '0'
                q = deque([(i,j)])
                while q:
                    r, c = q.popleft()
                    for dr, dc in DIRS:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                            grid[nr][nc] = '0'      # 必须入队时标记，出队才标记会重复入队
                            q.append((nr, nc))
    return count

print(num_islands([row[:] for row in grid1]))
print(num_islands([["1","1","0","0","0"],["1","1","0","0","0"],
                   ["0","0","1","0","0"],["0","0","0","1","1"]]))


# DFS 递归版：代码更短，但网格大时会爆栈
# 100x100 全陆地递归深度就超过 Python 默认上限 1000 了
def num_islands_dfs(grid):
    if not (grid and grid[0]):
        return 0
    m, n = len(grid), len(grid[0])

    def sink(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
            return                      # 出界和非陆地在入口一起挡掉
        grid[r][c] = '0'
        sink(r+1, c); sink(r-1, c)
        sink(r, c+1); sink(r, c-1)

    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                sink(i, j)
    return count

print(num_islands_dfs([row[:] for row in grid1]))


'''
给定一个不含重复数字的数组 nums ，返回其所有可能的全排列。你可以按任意顺序返回答案。

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''

# 回溯三要素：路径（已选的数）、选择列表（未用过的数）、结束条件（路径长度 == n）
# 核心动作是 "做选择 -> 递归深入 -> 撤销选择"，三步严格配对
# append 和 pop 次数必然相等，pop 的触发条件是"递归返回了"而不是"走不下去"
nums = [1,2,3]
def permute(nums):
    n = len(nums)
    res = []
    path = []
    used = [False] * n

    def backtrack():
        if len(path) == n:
            res.append(path[:])         # 必须拷贝：path 全程只有一个对象，会被反复修改
            return
        for i in range(n):              # 每层递归有自己独立的 i，但 path/used 是所有层共享的
            if used[i]:
                continue
            path.append(nums[i])        # 做选择
            used[i] = True
            backtrack()                 # 深入
            path.pop()                  # 撤销，让状态精确还原成进入前的样子
            used[i] = False

    backtrack()
    return res

print(permute(nums))


# 交换法：不需要 used 数组
# nums[0:start] 是已确定的前缀，把选中的数交换到 start 位置
def permute_swap(nums):
    res = []
    n = len(nums)

    def backtrack(start):
        if start == n:
            res.append(nums[:])
            return
        for i in range(start, n):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]      # 换回来
    backtrack(0)
    return res

print(permute_swap([1,2,3]))
