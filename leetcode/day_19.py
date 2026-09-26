'''

hot problem 1

以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

 

示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6]




hot problem 2 

给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

 

示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]


hot problem 3


给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]



hot problem 4

编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列


'''



intervals = [[1,3],[2,6],[8,10],[15,18]]




# 先进行排序
# 然后将i+1 元素的做端点和i元素的右端点进行比较
def Solution(intervals):
    intervals.sort(key=lambda x : x[0])
    res = []
    for s, e in intervals:
        if res and s <= res[-1][1]:
            res[-1][1] = max(res[-1][1], e)
        else:
            res.append([s, e])
    return res
print(Solution(intervals))


# [1,2,3,4 | 5,6,7]    k=3，从倒数第 k 个切开
#     A        B

# [5,6,7 | 1,2,3,4]    结果就是 B 接 A
#    B        A



# nums[:-k]   这个意思是取左边的部分
# nums[::-1]  这个意思是方向反转


nums = [1,2,3,4,5,6,7]
k = 5
def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]             # 切片赋值（属于进行原地修改）





# problem 3

matrix = [[1,2,3],[4,5,6],[7,8,9]]



# 旋转90度实际变化  (i, j)  →  (j, n-1-i)      行：第i行变到第n-1-i列       列：  行内的第 j 个  →  新位置的第 j 行
def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):               
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  # 先转置 (转置就是沿着对角线进行折叠 [i][j] = [j][i])
    for i in range(n):
        matrix[i] = matrix[i][::-1]                                  #  反转每一行\


# 不是记算法，而是养成"我的数据有什么特殊结构可以利用"的反射， 这块还是没有悟道
matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
# 这个矩阵从上到下，从左到右递增！！！！！！
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    r, c = 0, len(matrix[0]) - 1
    while r < len(matrix) and c >= 0:
        if matrix[r][c] == target:          # 从右上角走楼梯相当于是
            return True
        elif matrix[r][c] > target:
            c -= 1                        # 当前值太大，左移一列
        else:
            r += 1                        # 当前值太小，下移一行
    return False
print(searchMatrix(matrix2, 5))


# 这个其实是一个数据结构的问题
# 找 9 的路径:
#      1   4   7* 11* 15*      ← 路径右上方：全部 > 9（已排除）
#      2   5   8* 12  19
#      3   6   9* 16  22       ← 路径左下方：全部 < 9（已排除）
#     10  13  14  17  24
#     18  21  23  26  30