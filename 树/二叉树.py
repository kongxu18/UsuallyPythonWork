"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
前序遍历：根结点 —> 左子树 —> 右子树（先遍历根节点，然后左右）
中序遍历：左子树—> 根结点 —> 右子树（在中间遍历根节点）
后序遍历：左子树 —> 右子树 —> 根结点（最后遍历根节点）
"""


class TreeNode:
    def __init__(self, x):
        # 二叉树节点
        self.val = x
        self.left = None
        self.right = None


def BFS(root):
    """
    层次遍历
    :param root:
    :return:
    """
    if root is None:
        return
    # queue队列，保存节点
    queue = [root]
    # res保存节点值，作为结果
    # vals = []
    while queue:
        # 拿出队首节点
        currentNode = queue.pop(0)
        # vals.append(currentNode.val)
        print(currentNode.val, end=' ')
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)


# 前
dlr = [1, 2, 4, 7, 3, 5, 6, 8]
# 中
ldr = [4, 7, 2, 1, 5, 3, 8, 6]
"""
前序遍历顺序为根左右。中序遍历结果为左根右。前序遍历结果与中序遍历结果长度一致。

前序遍历首个为根，找到该根在中序遍历结果中的位置。就可以把树分为左子树与右子树。这样递归调用该函数，
"""


def reConstructBinaryTree(pre, tin):
    if not pre or not tin:
        return
    node = TreeNode(pre[0])
    for i in range(len(tin)):
        if tin[i] == node.val:
            root_i_tin = i

    node.left = reConstructBinaryTree(pre[1:root_i_tin + 1], tin[:root_i_tin])
    node.right = reConstructBinaryTree(pre[root_i_tin + 1:], tin[root_i_tin + 1:])

    return node


node = reConstructBinaryTree(dlr, ldr)
BFS(node)
print('')
print('    ', node.val)
print(' ', node.left.val, '     ', node.right.val)
print(node.left.left.val, ' ', end='')
print('   ', node.right.left.val, '   ', node.right.right.val)
print(' ', node.left.left.right.val, end='')
print('       ',node.right.right.left.val)
