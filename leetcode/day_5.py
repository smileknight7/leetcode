
'''

hot problem

给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 
满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。


'''

# 首先要构建成有序数组
# 这个是双指针的进阶，感觉还有点难，可能还要再想想
nums = [-1,0,1,2,-1,-4]
def three_sum(nums):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:   # 去重，第一个数不能重复作为起点（确保没有相等的数值）
            continue
        left, right = i + 1, n - 1  
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1                       # 这里是进行去重
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return res

'''
pandas

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id 是该表的主键(具有唯一值的列)。
该表包含用户的 ID 和名字。名字仅由小写和大写字符组成。
 

编写解决方案，修复名字，使得只有第一个字符是大写的，其余都是小写的。

返回按 user_id 排序的结果表。

返回结果格式示例如下。

 

示例 1：

输入：
Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+
输出：
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |
+---------+-------+


'''
import pandas as pd
users = pd.DataFrame({
    'user_id': [1, 2],
    'name': ['aLice', 'bOB']
})

def fix_names(users):
    users['name'] = users['name'].str.capitalize()
    return users.sort_values('user_id')
print(fix_names(users))


# lambda表达式使用:
