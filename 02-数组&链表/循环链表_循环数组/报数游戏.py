"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/127215504

题目描述
100个人围成一圈，每个人有一个编码，编号从1开始到100。

他们从1开始依次报数，报到为M的人自动退出圈圈，然后下一个人接着从1开始报数，直到剩余的人数小于M。

请问最后剩余的人在原先的编号为多少？

输入描述
输入一个整数参数 M

输出描述
如果输入参数M小于等于1或者大于等于100，输出“ERROR!”；

否则按照原先的编号从小到大的顺序，以英文逗号分割输出编号字符串

用例1
输入
3
输出
58,91
说明
输入M为3，最后剩下两个人。

用例2
输入
4
输出
34,45,97
说明
输入M为4，最后剩下三个人。
"""


# 获取输入
jump = int(input())


# 方法1:动态数组实现循环链表
def solution():
    if jump <= 1 or jump >= 100:
        return 'ERROR!'

    # 编号从1开始到100
    arr = list(range(1, 101))
    n = 100
    i = 0
    while n >= jump:
        i = (i+jump-1) % n  # todo 注意这里动态数组索引变换规律
        arr.pop(i)
        n -= 1

    return ','.join(map(str, arr))


print(solution())

# 方法2:自己实现循环链表
# 注意：Python自定义循环链表的性能表现不佳，反而使用动态数组性能更好。
# 双向节点
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


# 循环链表
class CycleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, val):
        node = Node(val)

        if self.size > 0:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node

        self.head.prev = self.tail
        self.tail.next = self.head
        self.size += 1

    def remove(self, cur):
        pre = cur.prev
        nxt = cur.next

        pre.next = nxt
        nxt.prev = pre

        cur.next = cur.prev = None

        if self.head == cur:
            self.head = nxt

        if self.tail == cur:
            self.tail = pre

        self.size -= 1

        return nxt

    def __str__(self):
        arr = []
        cur = self.head

        for i in range(self.size):
            arr.append(str(cur.val))
            cur = cur.next

        return ",".join(arr)


# 输入获取
m = int(input())


# 算法入口
def getResult():
    if m <= 1 or m >= 100:
        return "ERROR!"

    cycList = CycleLinkedList()
    for i in range(1, 101):
        cycList.append(i)

    idx = 1
    cur = cycList.head

    while cycList.size >= m:
        if idx == m:
            idx = 1
            cur = cycList.remove(cur)
        else:
            idx += 1
            cur = cur.next

    return str(cycList)


# 算法调用
print(getResult())
