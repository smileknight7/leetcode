'''
hot problem






给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。



找到字符串中所有字母的异位词

示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
'''

# 还是滑动窗口

from collections import Counter

# 暴力版本
# def findAnagrams(s, p):
#     m = len(p)
#     need = Counter(p)
#     return [i for i in range(len(s) - m + 1) if Counter(s[i:i+m]) == need]

s = "cbaebabacd"
p = "abc"

def findAnagrams( s: str, p: str):
    '''s 是检测序列, p是目标序列s'''
    n, m = len(s), len(p)
    if n < m:
        return []
    need = Counter(p)                       # 目标顺序
    window = Counter(s[:m])
    res = [0] if window == need else []
    for i in range(m, n):
        import ipdb; ipdb.set_trace()
        window[s[i]] += 1                    # 这边就是在做这个滑动部分
        window[s[i-m]] -= 1
        if window[s[i-m]] == 0:
            del window[s[i-m]]
        if window == need:
            res.append(i - m + 1)
    return res
    
print(findAnagrams(s, p))  # 输出: [0,6]





'''
pandas


-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id 是该表的主键（列中的值互不相同）。
该表的每一行都包含有关员工工资的信息。
 

编写一个解决方案查询 Employee 表中第 n 高的 不同 工资。如果少于 n 个不同工资，查询结果应该为 null 。

查询结果格式如下所示。

Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
输出: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
'''

# 先去重，然后排序，最后判断是否合理，再输出
import pandas as pd
employee = pd.DataFrame({
    'id': [1, 2, 3],
    'salary': [100, 200, 300]
})  
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    col = f'getNthHighestSalary({N})'
    s = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if N <= 0 or len(s) < N:
        return pd.DataFrame({col: [None]})
    return pd.DataFrame({col: [s.iloc[N - 1]]})

print(nth_highest_salary(employee, 2))  # 输出: 200