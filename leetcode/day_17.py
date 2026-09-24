'''

base problem 1


给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。

请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。

 

示例  1：



输入：mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]
输出：25
解释：对角线的和为：1 + 5 + 9 + 3 + 7 = 25
请注意，元素 mat[1][1] = 5 只会被计算一次。



base problem 2

给你一个整数数组 salary ，数组里每个数都是 唯一 的，其中 salary[i] 是第 i 个员工的工资。

请你返回去掉最低工资和最高工资以后，剩下员工工资的平均值。

 

示例 1：

输入：salary = [4000,3000,1000,2000]
输出：2500.00000
解释：最低工资和最高工资分别是 1000 和 4000 。
去掉最低工资和最高工资以后的平均工资是 (2000+3000)/2= 2500



给定由一些正数（代表长度）组成的数组 nums ，返回 由其中三个长度组成的、面积不为零的三角形的最大周长 。如果不能形成任何面积不为零的三角形，返回 0。

 

示例 1：

输入：nums = [2,1,2]
输出：5
解释：你可以用三个边长组成一个三角形:1 2 2。
示例 2：

输入：nums = [1,2,1,10]
输出：0
解释：
你不能用边长 1,1,2 来组成三角形。
不能用边长 1,1,10 来构成三角形。
不能用边长 1、2 和 10 来构成三角形。
因为我们不能用任何三条边长来构成一个非零面积的三角形，所以我们返回 0。



给定一个整数数组 coordinates ，其中 coordinates[i] = [x, y] ，
 [x, y] 表示横坐标为 x、纵坐标为 y 的点。请你来判断，这些点是否在该坐标系中属于同一条直线上。



 
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
输入:a = "11", b = "1"
输出："100"





输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：


'''

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]


def diagonalSum(mat):
    n = len(mat)                # 行数
    total = sum(mat[i][i] + mat[i][n - 1 - i] for i in range(n))  # 主对角线   和   副对角线的和（注意副对角线写法）
    if n % 2 == 1:                                  # 如果是奇数行（观察发现只有奇数的时候才有重叠）
        total -= mat[n // 2][n // 2]                # 减去中间的那个数
    return total

print(diagonalSum(mat))  # 输出结果



salary = [4000,3000,1000,2000]


def average(salary):
    salary.sort()
    average_salary = sum(salary[1:-1])/ len(salary[1:-1])  # 去掉最低工资和最高工资以后的平均工资
    return average_salary

print(average(salary))  # 输出结果


nums = [2,1,2]

def largestPerimeter(nums):
    nums.sort(reverse=True)  # 从大到小排序
    for i in range(len(nums) - 2):
        if nums[i] < nums[i + 1] + nums[i + 2]:
            return nums[i] + nums[i + 1] + nums[i + 2]  # 返回最大周长
    return 0  # 如果不能形成任何面积不为零的三角形，
print(largestPerimeter(nums))  # 输出结果


coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]



#  这个可以想成是两点共线，或者是向量叉积的形式

'''
A = (x1-x0, y1-y0)    P0 → P1
B = (x -x0, y -y0)    P0 → Pi
二维叉积定义为 Ax·By - Ay·Bx，代进去：

(x1-x0)(y-y0) - (y1-y0)(x-x0)


'''
def checkStraightLine(coordinates):
    x0, y0 = coordinates[0]  # 第一个点
    x1, y1 = coordinates[1]  # 第二个点
    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        if (y1 - y0) * (x - x0) != (y - y0) * (x1 - x0):  # 判断斜率是否相等
            return False
    return True


a, b = "11", "1"                                # 理解这个过程可能是需要手算一遍


# ① 手算时，我在重复做什么动作？   → 循环体
# ② 做这个动作需要知道什么？       → 需要哪些变量
# ③ 做完一次后，什么变了？         → 变量怎么更新
# ④ 什么时候不用再做了？           → 循环条件



def addBinary(a, b):
    i, j = len(a) - 1, len(b) - 1           # 构建两个指针
    carry = 0
    res =[]
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        res.append(str(total % 2))  # 取余数
        carry = total // 2           # 进位
    return ''.join(res[::-1])        # 反转结果并返回


list1 = [1,2,4]
list2 = [1,3,4]



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(vals):                       # 列表 → 链表（测试用）
    dummy = ListNode()                               # tail 最后只能看到尾巴，但是dummy是可以看到全局的
    tail = dummy
    for v in vals:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def show(node):                        # 链表 → 列表（看结果用）
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


def mergeTwoLists(list1, list2):
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        import ipdb; ipdb.set_trace()
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 or list2         # ← 补上这行        这里是直接将剩余链表拼接上去了，因为原本的链表就是升序的
    return dummy.next


list1 = build([1, 2, 4])
list2 = build([1, 3, 4])
print(show(mergeTwoLists(list1, list2)))   # [1, 1, 2, 3, 4, 4]