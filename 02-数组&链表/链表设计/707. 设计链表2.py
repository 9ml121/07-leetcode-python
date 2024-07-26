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


# Definition for double-linked list.
class ListNode:

    def __init__(self, val):
        """方法2：双向向链表(这里构造参数不包含next、prev)"""
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        """设置2个哨兵（sentinel）节点作为 头节点和 尾节点(好处就是不用判断头节点或者尾节点是否为空)
        size用来保存链表有效节点数（不包括哨兵节点）
        """
        self.head, self.tail = ListNode(-1), ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def getNode(self, index: int) -> ListNode:
        """根据索引index查找所在的节点。 注意：这里没有判断索引越界！！
        查找时间O(index)
        index=2     size=4
        idx  head  0    1    2    3    tail
             -1 -> 1 -> 2 -> 3 -> 4 -> -1
             -1 <- 1 <- 2 <- 3 <- 4 <- -1
              p                         p
        index=1
        """
        midIdx = self.size // 2
        if index >= midIdx:
            # 从tail开始，使用prev往前找, 查找范围[0..size-index)
            p = self.tail
            for _ in range(self.size - index):
                p = p.prev
        else:
            # 从head开始，使用next往后找, 查找范围[0..index)
            p = self.head.next
            for _ in range(index):
                p = p.next
        return p

    def get(self, index: int) -> int:
        """根据索引index查找节点val，index有效范围为[0..self.size)
        """
        if index < 0 or index >= self.size:
            return -1
        return self.getNode(index).val

    def addAtHead(self, val: int) -> None:
        """头部添加节点： O(1)时间"""
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """尾部添加节点： O(1)时间"""
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """在 index前面添加值为val的节点，index有效范围为[0..self.size]
        """
        if index < 0 or index > self.size:
            return

        p = self.getNode(index)  # p代表要添加的index位置节点，在p前面添加val,
        prev = p.prev
        addNode = ListNode(val)
        # 维护双向链表prev和next指针
        prev.next, p.prev = addNode, addNode
        addNode.prev, addNode.next = prev, p
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """删除index所在节点，index有效范围为[0..self.size)
        """
        if index < 0 or index >= self.size:
            return

        p = self.getNode(index)  # 要删除的index所在的节点
        prev = p.prev
        next_ = p.next
        prev.next, next_.prev = next_, prev
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

