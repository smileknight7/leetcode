


'''
hot problem

二叉树的顺序遍历


给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。





'''




# [1,null,2,3]  层序表示
# [1,3,2]     中序遍历

'''
        4
       / \
      2   6
     / \ / \
    1  3 5  7

层序 一层一层  : [4, 2, 6, 1, 3, 5, 7]
前序 根左右    : [4, 2, 1, 3, 6, 5, 7]
中序 左根右    : [1, 2, 3, 4, 5, 6, 7]
后序 左右根    : [1, 3, 2, 5, 7, 6, 4]


层序遍历BFS    广度优先
前序遍历DFS    深度优先
'''




# 构建中序遍历
#   1
#    \
#     2
#    /
#   3
#
# 从 1 开始：
#   ① 遍历 1 的左子树 → 空，跳过
#   ② 访问 1                        → [1]
#   ③ 遍历 1 的右子树（根是 2）：
#        ① 遍历 2 的左子树（根是 3）：
#             ① 3 的左子树 → 空
#             ② 访问 3               → [1,3]
#             ③ 3 的右子树 → 空
#        ② 访问 2                    → [1,3,2]
#        ③ 2 的右子树 → 空
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # 节点的值
        self.left = left      # 左孩子（也是 TreeNode，或 None）
        self.right = right    # 右孩子

# 递归方法
def inorderTraversal(root):
    res =[]
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)

    dfs(root)
    return res

print(inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3), None))))  # 输出: [1,3,2]

# 迭代方法``



'''
pandas 


+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id 是这个表的主键。
表的每一行包含员工的工资信息。
 

查询并返回 Employee 表中第二高的 不同 薪水 。如果不存在第二高的薪水，查询应该返回 null(Pandas 则返回 None) 。

查询结果如下例所示。

 

'''
import pandas as pd 



employee = pd.DataFrame({
    'id': [1, 2, 3],
    'salary': [100, 200, 300]
})
def  second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    col = 'SecondHighestSalary'
    s = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)
    import ipdb; ipdb.set_trace()
    if len(s) < 2:
        return pd.DataFrame({col: [None]})
    else:
        return pd.DataFrame({col: [s[1]]})                          # [1]这个就是第二高的
print(second_highest_salary(employee))  # 输出: 200



