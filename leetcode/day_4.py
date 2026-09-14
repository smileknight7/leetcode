
'''
hot problem

给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。
'''


# 有两种方法O(n)2 求解，双指针
# 双指针方式：
# left = 0, right = n - 1，从最宽的一对开始往中间收。每轮算一次面积，然后移动矮的那一边。
# 这里的left和right就是指针
# while和for循环： while 实际上就相当于是for + if
height = [1,8,6,2,5,4,8,3,7]
def max_area(height):
    left, right = 0 ,len(height) - 1
    best = 0 
    while left < right:
        area = (right - left) * min(height[left], height[right])
        best = max(best, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best

print(max_area(height))




'''
+-------------+---------+
| 列名        | 类型     |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+
employee_id 是这个表的主键(具有唯一值的列)。
此表的每一行给出了雇员id ，名字和薪水。
 

编写解决方案，计算每个雇员的奖金。如果一个雇员的 id 是 奇数 并且他的名字不是以 'M' 开头，那么他的奖金是他工资的 100% ，否则奖金为 0 。

返回的结果按照 employee_id 排序。

返回结果格式如下面的例子所示。

 

示例 1:

输入：
Employees 表:
+-------------+---------+--------+
| employee_id | name    | salary |
+-------------+---------+--------+
| 2           | Meir    | 3000   |
| 3           | Michael | 3800   |
| 7           | Addilyn | 7400   |
| 8           | Juan    | 6100   |
| 9           | Kannon  | 7700   |
+-------------+---------+--------+
输出：
+-------------+-------+
| employee_id | bonus |
+-------------+-------+
| 2           | 0     |
| 3           | 0     |
| 7           | 7400  |
| 8           | 0     |
| 9           | 7700  |
+-------------+-------+
解释：
因为雇员id是偶数，所以雇员id 是2和8的两个雇员得到的奖金是0。
雇员id为3的因为他的名字以'M'开头，所以，奖金是0。
其他的雇员得到了百分之百的奖金。

lambda表达式使用:
lambda x: 函数
'''


# 在使用pandas时，能用列运算符，就尽量不要用apply(apply会相对慢很多)

import pandas as pd
employees = pd.DataFrame({
    'employee_id': [2, 3, 7, 8, 9],
    'name': ['Meir', 'Michael', 'Addilyn', 'Juan', 'Kannon'],
    'salary': [3000, 3800, 7400, 6100, 7700]
})
def calculate_bonus(employees):
    is_odd = employees['employee_id'] % 2 == 1
    not_m = ~employees['name'].str.startswith('M')
    employees['bonus'] = employees['salary'].where(is_odd & not_m, 0)
    return employees[['employee_id', 'bonus']].sort_values('employee_id')
print(calculate_bonus(employees))

#     employees['bonus'] = employees.apply(lambda x: x['salary'] if x['employee_id'] % 2 == 1 and not x['name'].startswith('M') else 0, axis=1)