"""
从尾到头打印链表

输入一个链表，从尾到头打印链表每个节点的值
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 创建一个链表 特点只能从头到尾部遍历
head = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)

head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7


# 方法一：栈
# 由于单链表只能从头到尾遍历，想要从尾至头的输出，可以考虑借用栈。从头到尾遍历单链表并压栈，带全部元素都进栈了再出栈，这样就完成了从尾至头的输出。
# 时间复杂度O(n)，空间复杂度O(n)。
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        # 进栈
        self.items.append(item)

    def pop(self):
        # 从后往前进入，也从后往外弹出
        return self.items.pop()

    def isempty(self):
        return len(self.items) != 0


stack = Stack()
node = head
res = []
while node:
    stack.push(node.val)
    node = node.next

while stack.isempty():
    node = stack.pop()
    res.append(node)
print(res)


# python list 特性
def printListFromTailToHead(listNode):
    # write code here
    if not listNode:
        return []
    res = []
    while listNode:
        res.append(listNode.val)
        listNode = listNode.next
    return res[::-1]


print(printListFromTailToHead(head))
