"""
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：
          4
       /     \
     2        7
   /   \    /   \
  1    3   6     9
镜像输出：

           4
       /     \
    7         2
   / \     / \
9     6 3       1

"""


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


headnode = TreeNode(4)
node2 = TreeNode(2)
node7 = TreeNode(7)
node1 = TreeNode(1)
node3 = TreeNode(3)
node6 = TreeNode(6)
node9 = TreeNode(9)

headnode.left = node2
headnode.right = node7
node2.left = node1
node2.right = node3
node7.left = node6
node7.right = node9


class Solution:
    def mirrorTree(self, root: TreeNode):
        if not root:
            return

        left_node = root.left
        root.left = self.mirrorTree(root.right)
        root.right = self.mirrorTree(left_node)

        return root


s = Solution()
s.mirrorTree(headnode)

print(headnode.val)
print(headnode.left.val,headnode.right.val)
print(headnode.left.left.val,headnode.left.right.val,
      headnode.right.left.val,headnode.right.right.val)
