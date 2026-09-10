'''

给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。


输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

'''
# 时间复杂度O(n)问题：
# 串行起来是O(n)复杂度，但是嵌套起来就是O(n^2)复杂度了，下面这里虽然是嵌套的，但是每一次不是全部遍历，有continue所有一次只做一个
nums = [100, 4, 200, 1, 3, 2]
def longstConsecutive(nums):
    num_set = set(nums)
    best = 0 
    for x in num_set:
        if x - 1 in num_set:                    # 总体复杂度是外部n次 + while累积小于n次
            continue
        y = x
        while y + 1 in num_set:
            y += 1
        best = max(best, y - x + 1)
    return best




# 下面这种是暴力解法
# def solve(nums):
#     best = 0
#     for x in nums:                 # n 次
#         y, length = x, 1
#         while y + 1 in nums:       # list 的 in 本身就是 O(n)，while 最多 n 轮
#             y += 1; length += 1
#         best = max(best, length)
#     return best



'''
pandas

可回收低脂产品
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id 是该表的主键（具有唯一值的列）。
low_fats 是枚举类型，取值为以下两种 ('Y', 'N')，其中 'Y' 表示该产品是低脂产品，'N' 表示不是低脂产品。
recyclable 是枚举类型，取值为以下两种 ('Y', 'N')，其中 'Y' 表示该产品可回收，而 'N' 表示不可回收。
 

编写解决方案找出既是低脂又是可回收的产品编号。

返回结果 无顺序要求 。

返回结果格式如下例所示：

 

示例 1：

输入：
Products 表：
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
输出：
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
解释：
只有产品 id 为 1 和 3 的产品，既是低脂又是可回收的产品。

'''

import pandas as pd
products = pd.DataFrame({
    'product_id': [0, 1, 2, 3, 4],
    'low_fats': ['Y', 'Y', 'N', 'Y', 'N'],
    'recyclable': ['N', 'Y', 'Y', 'Y', 'N']
})

df_result = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')][['product_id']]

