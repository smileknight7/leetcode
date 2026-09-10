'''
hot problems

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

'''



nums = [2, 7, 11, 15]
target = 9
def two_sum(nums, target):
    num_index = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target: 
                num_index.append(i)
                num_index.append(j)
                return num_index
print(two_sum(nums, target=target))

'''

pandas

Views 表：

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
此表可能会存在重复行。（换句话说，在 SQL 中这个表没有主键）
此表的每一行都表示某人在某天浏览了某位作者的某篇文章。
请注意，同一人的 author_id 和 viewer_id 是相同的。
 

请查询出所有浏览过自己文章的作者。

结果按照作者的 id 升序排列。

查询结果的格式如下所示：
'''

import pandas as pd

df_views = pd.DataFrame({
    'article_id': [2, 1, 3, 4, 5],
    'author_id': [1, 2, 4, 4, 5],
    'viewer_id': [1, 2, 3, 4, 5],
    'view_date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'])
})

df_result = df_views[df_views['author_id'] == df_views['viewer_id']]
df_result = df_result[['author_id']].drop_duplicates().sort_values(by='author_id').reset_index(drop=True).rename(columns={'author_id': 'id'})
print(df_result)