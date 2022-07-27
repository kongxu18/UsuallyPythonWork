"""
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树  [1,2,2,3,4,4,3] 是对称的。

      1
     / \
   2    2
  / \  / \
3   4 4   3
但是下面这个  [1,2,2,null,3,null,3] 则不是镜像对称的:

      1
     / \
   2    2
     \    \
     3      3

"""


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


headnode = TreeNode(1)
node2 = TreeNode(2)
node2_ = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node3_ = TreeNode(3)
node4_ = TreeNode(4)

headnode.left = node2
headnode.right = node2_
node2.left = node3
node2.right = node4
node2_.left = node4_
node2_.right = node3_


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def recur(left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return recur(left.left, right.right) and recur(left.right, right.left)

        return recur(root.left, root.right)


s = Solution()
res = s.isSymmetric(headnode)
print(res)