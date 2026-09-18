




'''
pandas


+-------------+------+
| Column Name | Type |
+-------------+------+
| emp_id      | int  |
| event_day   | date |
| in_time     | int  |
| out_time    | int  |
+-------------+------+
在 SQL 中，(emp_id, event_day, in_time) 是这个表的主键。
该表显示了员工在办公室的出入情况。
event_day 是此事件发生的日期，in_time 是员工进入办公室的时间，而 out_time 是他们离开办公室的时间。
in_time 和 out_time 的取值在1到1440之间。
题目保证同一天没有两个事件在时间上是相交的，并且保证 in_time 小于 out_time。
 

计算每位员工每天在办公室花费的总时间（以分钟为单位）。 请注意，在一天之内，同一员工是可以多次进入和离开办公室的。 在办公室里一次进出所花费的时间为out_time 减去 in_time。

返回结果表单的顺序无要求。
查询结果的格式如下：

 

示例 1：

输入：
Employees table:
+--------+------------+---------+----------+
| emp_id | event_day  | in_time | out_time |
+--------+------------+---------+----------+
| 1      | 2020-11-28 | 4       | 32       |
| 1      | 2020-11-28 | 55      | 200      |
| 1      | 2020-12-03 | 1       | 42       |
| 2      | 2020-11-28 | 3       | 33       |
| 2      | 2020-12-09 | 47      | 74       |
+--------+------------+---------+----------+
输出：
+------------+--------+------------+
| day        | emp_id | total_time |
+------------+--------+------------+
| 2020-11-28 | 1      | 173        |
| 2020-11-28 | 2      | 30         |
| 2020-12-03 | 1      | 41         |
| 2020-12-09 | 2      | 27         




'''
import pandas as pd
employees = pd.DataFrame({
    'emp_id': [1, 1, 1, 2, 2],
    'event_day': ['2020-11-28', '2020-11-28', '2020-12-03', '2020-11-28', '2020-12-09'],
    'in_time': [4, 55, 1, 3, 47],
    'out_time': [32, 200, 42, 33, 74]
})

def total_time(employees):                  # groupby这个函数可以对列中的内容进行分组
    employees['total_time'] = employees['out_time'] - employees['in_time']
    # import ipdb; ipdb.set_trace()
    result = employees.groupby(['event_day', 'emp_id'], as_index=False)['total_time'].sum()
    result.rename(columns={'event_day': 'day'}, inplace=True)                       # 这里是对列名字进行修改
    return result

print(total_time(employees))




'''
-------------+------+
| Column Name | Type |
+-------------+------+
| teacher_id  | int  |
| subject_id  | int  |
| dept_id     | int  |
+-------------+------+
在 SQL 中，(subject_id, dept_id) 是该表的主键。
该表中的每一行都表示，该教师(teacher_id)在该系(dept_id)里教授的课程(subject_id)。
 

查询每位老师在大学里教授的科目种类的数量。

以 任意顺序 返回结果表。

查询结果格式示例如下。

 

示例 1:

输入: 
Teacher 表:
+------------+------------+---------+
| teacher_id | subject_id | dept_id |
+------------+------------+---------+
| 1          | 2          | 3       |
| 1          | 2          | 4       |
| 1          | 3          | 3       |
| 2          | 1          | 1       |
| 2          | 2          | 1       |
| 2          | 3          | 1       |
| 2          | 4          | 1       |
+------------+------------+---------+
输出:  
+------------+-----+
| teacher_id | cnt |
+------------+-----+
| 1          | 2   |
| 2          | 4   |
+------------+-----+
解释: 
教师 1:
  - 他在 3、4 系教科目 2。
  - 他在 3 系教科目 3。
教师 2:
  - 他在 1 系教科目 1。
  - 他在 1 系教科目 2。
  - 他在 1 系教科目 3。
  - 他在 1 系教科目 4。



'''

teacher = pd.DataFrame({
    'teacher_id': [1, 1, 1, 2, 2, 2, 2],
    'subject_id': [2, 2, 3, 1, 2, 3, 4],
    'dept_id': [3, 4, 3, 1, 1, 1, 1]
})

def count_unique_subjects(teacher):
    result = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()            # nunique()这个是聚合函数
    result.rename(columns={'subject_id': 'cnt'}, inplace=True)
    return result
print(count_unique_subjects(teacher))
    






'''
base problem



已知函数 signFunc(x) 将会根据 x 的正负返回特定值：

如果 x 是正数，返回 1 。
如果 x 是负数，返回 -1 。
如果 x 是等于 0 ，返回 0 。
给你一个整数数组 nums 。令 product 为数组 nums 中所有元素值的乘积。

返回 signFunc(product) 。

 

示例 1：

输入：nums = [-1,-2,-3,-4,3,2,1]
输出：1
解释：数组中所有值的乘积是 144 ，且 signFunc(144) = 1


'''


nums = [-1,-2,-3,-4,3,2,1]


def arraySign(nums):
    product = 1
    for num in nums:
        product*= num
    if product > 0:
        return 1
    elif product < 0:
        return -1
    else:
        return 0
print('arraySign, result')
print(arraySign(nums))





'''
base problem


给你一个数字数组 arr 。

如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为 等差数列 。

如果可以重新排列数组形成等差数列，请返回 true ；否则，返回 false 。

 

示例 1：

输入：arr = [3,5,1]
输出：true
解释：对数组重新排序得到 [1,3,5] 或者 [5,3,1] ，任意相邻两项的差分别为 2 或 -2 ，可以形成等差数列。


'''


arr = [3,5,1]

def canMakeArithmeticProgression(arr):
    arr.sort()                      # 先对数组进行重排序
    d = arr[1] - arr[0]              
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] != d:        
            return False
    return True


'''
hot problem


给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组是数组中的一个连续部分。

 

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。


Kadane 算法 动态规划算法中的入门题目

直接问"最大子数组是哪个"很难。换成问每个位置：
以 i 结尾的子数组里，最大和是多少？
把每个位置的答案都算出来，取最大值，就是全局答案。
'''

nums = [-2,1,-3,4,-1,2,1,-5,4]



# 先对序列进行拆分
#     [ -3 ]        + 4
#     [ 1, -3 ]     + 4
#     [ -2, 1, -3 ] + 4
#       └────┬────┘
#    这些全都是"以 -3 结尾的子数组"！（-3 是上一个位置）
# cur = max(x, cur + x)关键公式是这个
def maxSubArray(nums):
    cur = best = nums[0]
    for x in nums[1:]:
        import ipdb; ipdb.set_trace()
        cur = max(x, cur + x)           # 当x对累积有害的时候会触发重开，从当前x再累积
        best = max(best, cur)           # 全局最大和
    return best

print('hot probem')
print(maxSubArray(nums))