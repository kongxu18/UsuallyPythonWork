"""
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


node = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
node.next = n2
n2.next = n3
n3.next = n4


class Solution:
    def deleteNode(self, head: ListNode, val: int):
        if head.val == val:
            return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur:
            pre.next = cur.next
        return head


# 1234
s = Solution()
s.deleteNode(head=node, val=3)

while node:
    print(node.val)
    node = node.next
