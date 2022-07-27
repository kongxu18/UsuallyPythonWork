"""
输入一个链表，输出该链表中倒数第k个结点


此题我们可以先定义两个指针，p和q。让p和q都指向头结点。在定义一个i，i的初始值为0。
然后进入一个for循环，直到p走到链表结尾，每次i++。当i < k 的我们让p走，q不走。
当i >= k 的时候我们让p和q同时走一步。
当p走到结尾的时候，那么q走的值就是倒数k的位置，我们返回这个值就好了。

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


def findKthToTail(node, k):
    i = 0
    k_node = node
    while node:
        if i >= k:
            k_node = k_node.next

        node = node.next
        i += 1

    return k_node


print(findKthToTail(head, 3).val)
