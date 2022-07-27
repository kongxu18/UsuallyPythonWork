"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
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

head.next = n3
n3.next = n5

n2.next = n4
n4.next = n6
n6.next = n7


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 初始化一个空节点
        cur = dum = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next


s = Solution()
node = s.mergeTwoLists(head, n2)

while node:
    print(node.val)
    node = node.next
