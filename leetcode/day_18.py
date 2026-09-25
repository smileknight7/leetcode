'''

困于环中的机器人
中等
相关标签
premium lock icon
相关企业
提示
在无限的平面上，机器人最初位于 (0, 0) 处，面朝北方。注意:

北方向 是y轴的正方向。
南方向 是y轴的负方向。
东方向 是x轴的正方向。
西方向 是x轴的负方向。
机器人可以接受下列三条指令之一：

"G"：直走 1 个单位
"L"：左转 90 度
"R"：右转 90 度
机器人按顺序执行指令 instructions，并一直重复它们。

只有在平面中存在环使得机器人永远无法离开时，返回 true。否则，返回 false。



输入：instructions = "GGLLGG"
输出：true
解释：机器人最初在(0,0)处，面向北方。
“G”:移动一步。位置:(0,1)方向:北。
“G”:移动一步。位置:(0,2).方向:北。
“L”:逆时针旋转90度。位置:(0,2).方向:西。
“L”:逆时针旋转90度。位置:(0,2)方向:南。
“G”:移动一步。位置:(0,1)方向:南。
“G”:移动一步。位置:(0,0)方向:南。
重复指令，机器人进入循环:(0,0)——>(0,1)——>(0,2)——>(0,1)——>(0,0)。
在此基础上，我们返回true。







base problem 2

给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。



base problem 3


给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

 

示例 1：


输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]




base problem 4


给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。
输入: num1 = "2", num2 = "3"
输出: "6"


base problem 5  链表

给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。
输入：l1 = [7,2,4,3], l2 = [5,6,4]
输出：[7,8,0,7]


'''


instructions = "GGLLGG"

# 关键在于一直重复这个指令，所以只要方向有变化就一定会成环
def isRobotBounded(instructions):
    dirs = [(0,1), (1, 0), (0,-1), (-1,0)]  # 北，东，南，西
    d = 0 # 初始方向是北
    x, y = 0, 0
    for c in instructions:
        if c == 'G':                    # G表示直行，
            dx, dy  = dirs[d]
            x += dx
            y += dy                     
        if c == 'L':                    # 逆时针退一格(控制方向)
            d = (d - 1) % 4
        if c == 'R':                    # 顺时针进一格(控制方向)
            d = (d + 1) % 4
    return (x, y) == (0, 0) or d != 0


# 最终结果要求方向不朝向北方不在远离原点，或者最终位置在原点， 这种就会绕回来
matrix = [[1,2,3],[4,5,6],[7,8,9]]
def spiralOrder(matrix):
    res = []
    while matrix:
        res += matrix.pop(0)
        if matrix:
            for row in matrix:
                res.append(row.pop())
        if matrix and matrix[0]:                # pop 掉之后会有空[]
            res += matrix.pop()[::-1]           # 取出最后一行并反转

        if matrix and matrix[0]:                # 从下向上添加每一行第一个元素
            for row in matrix[::-1]:
                res.append(row.pop(0))
    return res




matrix2 = [[1,1,1],[1,0,1],[1,1,1]]
def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    rows, cols = set(), set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in range(m):
        for j in range(n):
            if i in rows or j in cols:
                matrix[i][j] = 0
    # for i in rows:
    #     for j in range(n):
    #         matrix[i][j] = 0
    return matrix



num1 = "2"
num2 = "3"


def multiply(num1, num2):        # 先考虑一下特殊情况               # 本质上是先按顺序乘，再错位相加
    if num1 == "0" or num2 == "0":
        return "0"
    m, n = len(num1), len(num2)
    res = [0] * (m + n)            
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            sum_ = mul + res[i+j+1]  # 当前位置的和
            res[i+j+1] = sum_ % 10   # 当前位
            res[i+j] += sum_ // 10   # 进位
    idx = 0                                  # 去前导零
    while idx < len(res) and res[idx] == 0:
        idx += 1
    return ''.join(map(str, res[idx:]))


# 链表



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




l1 = build([7,2,4,3])
l2 = build([5,6,4])


# 这个链表是要使用栈思路，先按顺序压栈然后再取出来就是倒叙了
def addTwoNumbers(l1, l2):
    s1, s2 = [], []
    while l1:
        s1.append(l1.val)                       # ([7, 2, 4, 3]
        l1 = l1.next
    while l2:
        s2.append(l2.val)                       # [5, 6, 4])
        l2 = l2.next
    carry = 0
    head = None
    while s1 or s2 or carry:
        total = carry
        if s1:
            total += s1.pop()                   # pop默认是倒序取值的
        if s2:
            total += s2.pop()
        node = ListNode(total % 10)              # 取余数
        node.next = head                         # 头插法
        head = node
        carry = total // 10                      # 进位
    return head 
print(addTwoNumbers(l1, l2))