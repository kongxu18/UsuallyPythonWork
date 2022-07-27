"""
二叉树的下一个节点

题目描述：给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None


# 构建二叉树
a1 = TreeLinkNode(1)
a2 = TreeLinkNode(2)
a3 = TreeLinkNode(3)
a4 = TreeLinkNode(4)
a5 = TreeLinkNode(7)
a1.left = a2
a1.right = a3
a3.left = a4
a3.right = a5
a1.parent = None
a2.parent = a1
a3.parent = a1
a4.parent = a3
a5.parent = a3


def get_next(pNode):
    if not pNode:
        return
    # 如果该节点有右子树，那么下一个节点就是它右子树中的最左节点
    elif pNode.right is not None:
        pNode = pNode.right
        while pNode.left is not None:
            pNode = pNode.left
        return pNode

    # 如果一个节点没有右子树，，并且它还是它父节点的右子节点
    elif pNode.parent is not None and pNode.parent.right == pNode and pNode.right is None:
        while pNode.parent is not None and pNode.parent.left != pNode:
            pNode = pNode.parent
        return pNode.parent
    # 如果一个节点是它父节点的左子节点，那么直接返回它的父节点
    else:
        return pNode.parent
