



'''
hot problem
接雨水


给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 



'''
height   = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# 这个要想成每个格子头顶可以接多少水
# O(n^2)的解法，暴力法
def trap_On2(height):
    water = 0
    for i in range(len(height)):
        left_max = max(height[:i + 1])      # 每次都重新扫一遍
        right_max = max(height[i:])
        water += min(left_max, right_max) - height[i]
    return water



#  left_max [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
#  right_max [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
# 前后缀On时间On
def trap_On(height):
    n = len(height)
    if n == 0:
        return 0

    left_max = [0] * n                          # 预先填好位置
    left_max[0] = height[0]
    for i in range(1, n):                       # 从左往右攒
        left_max[i] = max(left_max[i - 1], height[i])

    right_max = [0] * n
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):              # 从右往左攒
        right_max[i] = max(right_max[i + 1], height[i])
    import ipdb; ipdb.set_trace()
    return sum(min(left_max[i], right_max[i]) - height[i] for i in range(n))



# 双指针方法
def trap(height):
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]     # 左边的水位由 left_max 说了算
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1
    return water

print(trap_On(height))

'''

pandas
查找有效邮箱

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
| mail          | varchar |
+---------------+---------+
user_id 是该表的主键（具有唯一值的列）。
该表包含了网站已注册用户的信息。有一些电子邮件是无效的。
 

编写一个解决方案，以查找具有有效电子邮件的用户。

一个有效的电子邮件具有前缀名称和域，其中：

 前缀 名称是一个字符串，可以包含字母（大写或小写），数字，下划线 '_' ，点 '.' 和（或）破折号 '-' 。前缀名称 必须 以字母开头。
域 必须是小写的 '@leetcode.com'。


Users 表:
+---------+-----------+-------------------------+
| user_id | name      | mail                    |
+---------+-----------+-------------------------+
| 1       | Winston   | winston@leetcode.com    |
| 2       | Jonathan  | jonathanisgreat         |
| 3       | Annabelle | bella-@leetcode.com     |
| 4       | Sally     | sally.come@leetcode.com |
| 5       | Marwan    | quarz#2020@leetcode.com |
| 6       | David     | david69@gmail.com       |
| 7       | Shapiro   | .shapo@leetcode.com     |
+---------+-----------+-------------------------+
输出：
+---------+-----------+-------------------------+
| user_id | name      | mail                    |
+---------+-----------+-------------------------+
| 1       | Winston   | winston@leetcode.com    |
| 3       | Annabelle | bella-@leetcode.com     |
| 4       | Sally     | sally.come@leetcode.com |
+---------+-----------+-------------------------+
解释：
用户 2 的电子邮件没有域。 
用户 5 的电子邮件带有不允许的 '#' 符号。
用户 6 的电子邮件没有 leetcode 域。 
用户 7 的电子邮件以点开头。
'''
import pandas as pd
users = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5, 6, 7],
    'name': ['Winston', 'Jonathan', 'Annabelle', 'Sally', 'Marwan', 'David', 'Shapiro'],
    'mail': ['winston@leetcode.com', 'jonathanisgreat', 'bella-@leetcode.com', 'sally.come@leetcode.com', 'quarz#2020@leetcode.com', 'david69@gmail.com', '.shapo@leetcode.com']
})


# 正则表达式：

# ^                  字符串的开头
# [A-Za-z]           第 1 个字符：必须是一个字母（大写或小写）
# [A-Za-z0-9_.-]*    第 2 个字符起：字母/数字/下划线/点/连字符，任意多个（可以 0 个）
# @leetcode          字面量 "@leetcode"
# \.                 一个真正的点号
# com                字面量 "com"
# $                  字符串的结尾



# 常用正则表达式
# 在 []外          在 []内
# .   任意字符  →  一个点
# *   重复量词  →  一个星号
# +   一次或多次 → 一个加号
# ?   可选      →  一个问号
# (   分组      →  一个括号
# |   或        →  一个竖线
# {   次数      →  一个花括号



def valid_email(users):
    # 定义正则表达式模式
    pattern = r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$'
    
    # 使用正则表达式过滤有效的电子邮件
    valid_users = users[users['mail'].str.match(pattern)]
    
    return valid_users
print(valid_email(users))