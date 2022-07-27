"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

思路：
    首先定义一个cur指针，指向头结点，再定义一个pre指针，初始化为null。

    然后就要开始反转了，首先要把 cur->next 节点用tmp指针保存一下，也就是保存一下这个节点。

    为什么要保存一下这个节点呢，因为接下来要改变 cur->next 的指向了，将cur->next 指向pre ，此时已经反转了第一个节点了。

    接下来，就是循环走如下代码逻辑了，继续移动pre和cur指针。

    最后，cur 指针已经指向了null，循环结束，链表也反转完毕了。 此时我们return pre指针就可以了，pre指针就指向了新的头结点。

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


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head

        while cur:
            now_next = cur.next
            cur.next = pre
            pre, cur = cur, now_next

        return pre


s = Solution()
node = s.reverseList(head)
while node:
    print(node.val)
    node = node.next
