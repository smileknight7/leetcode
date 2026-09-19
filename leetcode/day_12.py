'''

pandas


+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class)是该表的主键（不同值的列的组合）。
该表的每一行表示学生的名字和他们注册的课程。
 

查询 至少有 5 个学生 的所有课程。

以 任意顺序 返回结果表。

结果格式如下所示。

 

示例 1:

输入: 
Courses 表:
+---------+----------+
| student | class    |
+---------+----------+
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
+---------+----------+
输出: 
+---------+ 
| class   | 
+---------+ 
| Math    | 
+---------+


'''


import pandas as pd  


courses = pd.DataFrame({
    'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'class': ['Math', 'English', 'Math', 'Biology', 'Math', 'Computer', 'Math', 'Math', 'Math']
})

def find_classes(courses):
    df = courses.groupby('class').size().reset_index(name='student_count')              # 这世界上会忽略除了goupby()之外的其他列表
    result = df[df['student_count'] >= 5][['class']]
    return result

print(find_classes(courses))    

'''

+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
在 SQL 中，Order_number是该表的主键。
此表包含关于订单ID和客户ID的信息。
 

查找下了 最多订单 的客户的 customer_number 。

测试用例生成后， 恰好有一个客户 比任何其他客户下了更多的订单。

查询结果格式如下所示。


'''


orders = pd.DataFrame({
    'order_number': [1, 2, 3, 4, 5, 6, 7],
    'customer_number': [101, 102, 101, 103, 101, 102, 101]
})


def largest_orders(orders):
    df = orders.groupby('customer_number').size().reset_index(name='order_count')
    result = df[df['order_count']==df['order_count'].max()][['customer_number']]
    return result
print(largest_orders(orders))




'''
base problem 1 

给你两个字符串 haystack 和 needle ，
请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。
输入：haystack = "sadbutsad", needle = "sad"
输出：0
解释："sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。
 


base problem 2

给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。

 

示例 1:

输入: s = "abab"
输出: true
解释: 可由子串 "ab" 重复两次构成。



'''
haystack = "leetcode"
needle = "leeto"


def strStr(haystack, needle):
    index = haystack.find(needle)
    return index

def strStr(haystack, needle):
    n, m = len(haystack), len(needle)
    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:            # 这种方式每次都重新比较所有字符
            return i
    return -1

# KMP方法  (有点搞不懂这个方法好吧)
def strStrKMP(haystack, needle):
    n, m = len(haystack), len(needle)

    # ===== 第一步：构建 next 数组（前缀函数）=====
    nxt = [0] * m
    k = 0                                      # k = 当前最长相同前后缀的长度
    for i in range(1, m):
        while k > 0 and needle[i] != needle[k]:
            k = nxt[k - 1]                      # 失配就回退
        if needle[i] == needle[k]:
            k += 1
        nxt[i] = k

    # ===== 第二步：匹配，i 永不回退 =====
    j = 0                                      # j = 已经匹配上的长度
    for i in range(n):
        while j > 0 and haystack[i] != needle[j]:
            j = nxt[j - 1]                     # 只回退 j，i 原地不动
        if haystack[i] == needle[j]:
            j += 1
        if j == m:
            return i - m + 1                   # 匹配成功，算出起点
    return -1




s = 'abab'
def repeatedSubstringPattern(s):            # nxt数组值永远长度，下标表示位置，这里k-1只是恰好等于上个相同的下标，
    n = len(s)
    nxt = [0] * n
    k = 0
    for i in range(1, n):                           # 回退一下
        while k and s[i] !=s[k]:
            k = nxt[k - 1]

        import ipdb; ipdb.set_trace()
        if s[i] == s[k]:                             # 向前走对应
            k += 1
        nxt[i] = k                                   # 走完成第一轮nxt= [0, 0, 1, 2]
    L = nxt[n -1]
    return L > 0 and n % (n - L) == 0

print(repeatedSubstringPattern(s))  




'''
hot problm



'''