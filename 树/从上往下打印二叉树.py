"""
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

例如:
给定二叉树:  [3,9,20,null,null,15,7],

     3
    / \
   9  20
 / \   / \
1  2 15   7
返回：

[3,9,20,15,7]
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


head = TreeNode(3)
node9 = TreeNode(9)
node1 = TreeNode(1)
node2 = TreeNode(2)
node9.left = node1
node9.right = node2
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)

head.left = node9
head.right = node20
node20.left = node15
node20.right = node7


class Solution:
    def __init__(self):
        self.res = []

    def levelOrder(self, root: TreeNode):
        if not root:
            return
        arr, i = [], 0

        def push(arr, i):
            for item in arr[i:]:
                if not item.left or item.right:
                    return
                arr.append(item.left)
                arr.append(item.right)
                i += 1
            return push(arr, i)

        return arr


def traverse(root):
    if not root:
        return
    val = root.val
    print(val)
    left = traverse(root.left)
    right = traverse(root.right)


traverse(head)
