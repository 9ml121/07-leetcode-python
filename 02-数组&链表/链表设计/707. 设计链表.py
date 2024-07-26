"""
你可以选择使用单链表或者双链表，设计并实现自己的链表。

单链表中的节点应该具备两个属性：value 和 next 。value 是当前节点的值，next 是指向下一个节点的指针/引用。

如果是双向链表，则还需要属性 prev 以指示链表中的上一个节点。假设链表中的所有节点下标从 0 开始。

实现 MyLinkedList 类：

MyLinkedList() 初始化 MyLinkedList 对象。
int get(int index) 获取链表中下标为 index 的节点的值。如果下标无效，则返回 -1 。
void addAtHead(int value) 将一个值为 value 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。
void addAtTail(int value) 将一个值为 value 的节点追加到链表中作为链表的最后一个元素。
void addAtIndex(int index, int value) 将一个值为 value 的节点插入到链表中下标为 index 的节点之前。如果 index 等于链表的长度，那么该节点会被追加到链表的末尾。如果 index 比长度更大，该节点将 不会插入 到链表中。
void deleteAtIndex(int index) 如果下标有效，则删除链表中下标为 index 的节点。


示例：

输入
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
输出
[null, null, null, null, 2, null, 3]

解释
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // 链表变为 1->2->3
myLinkedList.get(1);              // 返回 2
myLinkedList.deleteAtIndex(1);    // 现在，链表变为 1->3
myLinkedList.get(1);              // 返回 3


提示：

0 <= index, value <= 1000
请不要使用内置的 LinkedList 库。
调用 get、addAtHead、addAtTail、addAtIndex 和 deleteAtIndex 的次数不超过 2000 。
"""


# Definition for singled-linked list.
class ListNode:

    def __init__(self, val):
        """方法1：单向链表(这里构造参数不包含next节点，注意：有些示例是包含的)"""
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """设置一个哨兵（sentinel）节点作为头节点，size用来保存链表有效节点数
        """
        self.head = ListNode(-1)
        self.size = 0

    def get(self, index: int) -> int:
        """根据索引index查找节点值，index有效范围为[0, self.size)
        """
        if index < 0 or index >= self.size:
            return -1
        p = self.head.next
        for i in range(index):
            p = p.next
        return p.value

    def addAtHead(self, val: int) -> None:
        """头部添加节点：O(1)时间"""
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """尾部添加节点：O(n)时间"""
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """在index节点前添加值为val的节点，index有效范围[0..self.size]
        idx  head  0  1  2  3  size=4
        value  -1 -> 1->2->3->4->None
        """
        if index < 0 or index > self.size:
            return
        else:
            addNode = ListNode(val)
            p = self.head  # p指向index前一个节点
            for i in range(index):
                p = p.next
            addNode.next = p.next
            p.next = addNode
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """删除index所在位置节点，index有效范围[0..size)
        """
        if index < 0 or index >= self.size:
            return
        else:
            p = self.head  # p指向index前一个节点
            for i in range(index):
                p = p.next
            p.next = p.next.next
        self.size -= 1

    def __str__(self):
        """
        打印格式：1 -> 2 -> 3 -> None
        """
        cur = self.head
        output = ""
        while cur:
            output += str(cur.val) + "->"
            cur = cur.next
        output += "None"
        return output


if __name__ == '__main__':
    myLinkedList = MyLinkedList()
    print(f'初始状态: {myLinkedList}')
    myLinkedList.addAtHead(11)
    myLinkedList.addAtTail(99)
    print(f'头部添加11，尾部添加99：{myLinkedList}')
    print(f'index=1节点val: {myLinkedList.get(1)}')
    myLinkedList.addAtIndex(1, 66)
    print(f'index=1前面添加66：{myLinkedList}')
    myLinkedList.deleteAtIndex(1)
    print(f'index=1删除： {myLinkedList}')
    myLinkedList.addAtIndex(3, 66)
    print(f'index=3前面添加66：{myLinkedList}')
    myLinkedList.deleteAtIndex(9)
    print(f'index=3删除： {myLinkedList}')
    print(f'index=3节点val: {myLinkedList.get(3)}')

"""
复杂度分析
时间复杂度：
    初始化消耗 O(1)，
    get 消耗 O(index)，
    addAtHead 消耗 O(1)，
    addAtTail 消耗 O(n)，其中 n 为链表当前长度，即 addAtHead，addAtTail 和 addAtIndex 已调用次数之和
    addAtIndex 消耗 O(index)

空间复杂度：
    所有函数的单次调用空间复杂度均为 O(1)，
    总体空间复杂度为 O(n)，
    其中 n 为 addAtHead 和 addAtIndex 调用次数之和。
"""
