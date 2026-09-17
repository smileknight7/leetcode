



'''
hot problem

给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。
示例 1：

输入：nums = [1,1,1], k = 2
输出：2

'''



from  collections import defaultdict

nums = [2, 4, 6]
k = 6




# 这个还是有点没搞懂这个哈希表的问题
# 这里的count构建的dict就是一个哈希表？？？？？

def subarraySum(nums, k):
    count = defaultdict(int)
    count[0] = 1
    prefix = 0
    res = 0 
    for x in nums:
        prefix += x                         # 最初使用0进行占位，实际表示大的是累积值
        res += count[prefix - k]            # 检查的账本() 只要有差值就相当于累积有k？？？   prefix[j] - prefix[i] = k    ----->   prefix[i] = prefix[j] - k
        count[prefix] += 1
    import ipdb;ipdb.set_trace()
    return res


print(subarraySum(nums, k))  






'''
pandas

-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id 是该表的主键列(具有唯一值的列)。
该表的每一行包含一封电子邮件。电子邮件将不包含大写字母。
 

编写解决方案 删除 所有重复的电子邮件，只保留一个具有最小 id 的唯一电子邮件。

（对于 SQL 用户，请注意你应该编写一个 DELETE 语句而不是 SELECT 语句。）

（对于 Pandas 用户，请注意你应该直接修改 Person 表。）

运行脚本后，显示的答案是 Person 表。驱动程序将首先编译并运行您的代码片段，然后再显示 Person 表。Person 表的最终顺序 无关紧要 。

返回结果格式如下示例所示。

 

示例 1:

输入: 
Person 表:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
输出: 
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
解释: john@example.com重复两次。我们保留最小的Id = 1。
'''



import pandas as pd

person = pd.DataFrame({
    'id': [1, 2, 3],
    'email': ['john@example.com', 'bob@example.com', 'john@example.com']
})


def delete_duplicate_emails(person):
    # 使用 drop_duplicates 保留每个 email 的第一条记录（即最小 id）
    person.sort_values(by='id', inplace=True)  # 确保按 id 排序
    person.drop_duplicates(subset='email', keep='first', inplace=True)
    return person
print(delete_duplicate_emails(person))




'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store1      | int     |
| store2      | int     |
| store3      | int     |
+-------------+---------+
在 SQL 中，这张表的主键是 product_id（产品Id）。
每行存储了这一产品在不同商店 store1, store2, store3 的价格。
如果这一产品在商店里没有出售，则值将为 null。
 

请你重构 Products 表，查询每个产品在不同商店的价格，使得输出的格式变为(product_id, store, price) 。如果这一产品在商店里没有出售，则不输出这一行。

输出结果表中的 顺序不作要求 。

查询输出格式请参考下面示例。

 

示例 1：

输入：
Products table:
+------------+--------+--------+--------+
| product_id | store1 | store2 | store3 |
+------------+--------+--------+--------+
| 0          | 95     | 100    | 105    |
| 1          | 70     | null   | 80     |
+------------+--------+--------+--------+
输出：
+------------+--------+-------+
| product_id | store  | price |
+------------+--------+-------+
| 0          | store1 | 95    |
| 0          | store2 | 100   |
| 0          | store3 | 105   |
| 1          | store1 | 70    |
| 1          | store3 | 80    |
+------------+--------+-------+
解释：
产品 0 在 store1、store2、store3 的价格分别为 95、100、105。
产品 1 在 store1、store3 的价格分别为 70、80。在 store2 无法买到。


'''

protucts = pd.DataFrame({
    'product_id': [0, 1],
    'store1': [95, 70],
    'store2': [100, None],
    'store3': [105, 80]
})


def restructure_products(products):                 # .melt 这个函数的作用是将来横向的列名竖起来
    return products.melt(
        id_vars='product_id',
        value_vars=['store1', 'store2', 'store3'],
        var_name='store',
        value_name='price'
    ).dropna(subset=['price'])



print(protucts)
print(restructure_products(protucts))
