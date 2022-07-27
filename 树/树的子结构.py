"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

        3
      / \
     4    5
   / \
  1    2
给定的树 B：

     4
   /
  1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


nodeHead1 = TreeNode(3)
node4 = TreeNode(4)
node1 = TreeNode(1)
node2 = TreeNode(2)
node5 = TreeNode(5)
nodeHead1.left = node4
nodeHead1.right = node5
node4.left = node1
node4.right = node2

nodeHead2 = TreeNode(4)
node_1 = TreeNode(1)
nodeHead2.left = node_1


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        if not A or not B:
            return False

        # b 为测试的二叉树
        def recur(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)


s = Solution()
res = s.isSubStructure(nodeHead1, nodeHead2)
print(res)
