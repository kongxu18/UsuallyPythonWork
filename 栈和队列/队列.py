"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

队列是一种特殊的线性表，特殊之处在于它只允许在表的前端（front）进行删除操作，而在表的后端（rear）进行插入操作，
和栈一样，队列是一种操作受限制的线性表。进行插入操作的端称为队尾，进行删除操作的端称为队头。
队列中没有元素时，称为空队列。
"""


class Solution:
    """
    栈A用来作入队列
    栈B用来出队列，当栈B为空时，栈A全部出栈到栈B,栈B再出栈（即出队列）
    """

    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, item):
        """
        队列加入
        :return:
        """
        self.stackA.append(item)

    def pop(self):
        if self.stackB:
            return self.stackB.pop()
        elif not self.stackA:
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()


s = Solution()
for i in range(10):
    s.push(i)

print(s.stackA)
num = s.pop()
print(num)
