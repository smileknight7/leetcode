


# 贪心算法

'''

给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

'''


# 这里要将每次的跳跃路径转为最远跳多远:    贪心为什么成立: 可达集合是连续的

# ① 重复什么动作    看当前位置，更新"最远能到哪"
# ② 需要什么变量    最远可达下标
# ③ 一轮后什么变了  最远可达可能被刷新
# ④ 什么时候停      走完全程，或者发现当前位置已经不可达


nums = [2,3,1,1,4]              # 跳跃区间： 1,2,3,4
def canJump(nums):
    max_reach = 0
    for i, step in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + step)
    return True
print(canJump(nums))


numRows = 5
def generate(numRows):
    if numRows == 0:
        return []
    triangle = [[1]]
    import ipdb;ipdb.set_trace()  # 断点调试
    for i in range(1, numRows):         # 假设numRows是3
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j -1] + triangle[i - 1][j]                 # i 和整个triangle绑定，i-1就表示上一行
        triangle.append(row)                                                    #  j-1 表示左上，j表示右上
    
    return triangle
print(generate(numRows))
# 感觉还是想不到这个题怎么去做！！！！！




# 图论

'''

你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的

'''
numCourses = 2
prerequisites = [[1,0],[0,1]]

# [a, b] 表示"学 a 之前必须先学 b"
#       →  画成一条边：b ────→ a
#          （先修在前，后续在后）


# ① 重复什么动作    取一门入度为0的课，学掉，把它的后继课程入度各减1
# ② 需要什么变量    邻接表（谁指向谁）、入度数组、队列、已学课程数
# ③ 一轮后什么变了  已学+1，某些课入度减少，可能有新课入队s
# ④ 什么时候停      队列空了

from collections import deque

def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    
    for a, b in prerequisites:
        graph[b].append(a)                              # b是key， a是value 表示学完b之后才能学a
        indegree[a] += 1            


    q = deque(i for i in range(numCourses) if indegree[i] == 0)         # q中存放所有入度为0的课程
    learned = 0

    while q:
        cur = q.popleft()
        learned += 1
        for nxt in graph[cur]:
            indegree[nxt] -= 1                              # 找对应后置可能将入度减为0
            if indegree[nxt] == 0:                          # 继续走对列
                q.append(nxt)
    return learned == numCourses                            # 一直记录学习课程数量