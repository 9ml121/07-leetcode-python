"""
设计实现双端队列。

实现 MyCircularDeque 类:

MyCircularDeque(int k) ：构造函数,双端队列最大为 k 。
boolean insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true ，否则返回 false 。
boolean insertLast() ：将一个元素添加到双端队列尾部。如果操作成功返回 true ，否则返回 false 。
boolean deleteFront() ：从双端队列头部删除一个元素。 如果操作成功返回 true ，否则返回 false 。
boolean deleteLast() ：从双端队列尾部删除一个元素。如果操作成功返回 true ，否则返回 false 。
int getFront() )：从双端队列头部获得一个元素。如果双端队列为空，返回 -1 。
int getRear() ：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1 。
boolean isEmpty() ：若双端队列为空，则返回 true ，否则返回 false  。
boolean isFull() ：若双端队列满了，则返回 true ，否则返回 false 。


示例 1：

输入
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
输出
[null, true, true, true, false, 2, true, true, true, 4]

解释
MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
circularDeque.insertLast(1);			        // 返回 true
circularDeque.insertLast(2);			        // 返回 true
circularDeque.insertFront(3);			        // 返回 true
circularDeque.insertFront(4);			        // 已经满了，返回 false
circularDeque.getRear();  				// 返回 2
circularDeque.isFull();				        // 返回 true
circularDeque.deleteLast();			        // 返回 true
circularDeque.insertFront(4);			        // 返回 true
circularDeque.getFront();				// 返回 4



提示：

1 <= k <= 1000
0 <= value <= 1000
insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull  调用次数不大于 2000 次
"""

"""
这道题的前导问题是「力扣」第 622 题：设计循环队列。
在实现上几乎是一模一样的，要注意的地方有：

1.定义循环变量 front 和 rear 。一直保持这个定义，到底是先赋值还是先移动指针就很容易想清楚了。
    - head：指向队列头部第 1 个有效数据的位置；
    - tail：指向队列尾部（即最后 1 个有效数据）的 下一个位置，即下一个从队尾入队元素的位置。
说明：这个定义是依据「动态数组」的定义模仿而来。

2.为了避免「队列为空」和「队列为满」的判别条件冲突，我们有意浪费了一个位置；
浪费一个位置是指：循环数组中任何时刻一定至少有一个位置不存放有效元素。
    - 判别队列为空的条件是：front == rear;；
    - 判别队列为满的条件是：(rear + 1) % capacity == front;。
    可以这样理解，当 rear 循环到数组的前面，要从后面追上 front，还差一格的时候，判定队列为满。

3.因为有循环的出现，要特别注意处理数组下标可能越界的情况。
    - 指针后移的时候，下标 +1，要取模；
    - 指针前移的时候，为了循环到数组的末尾，需要先加上数组的长度，然后再对数组长度取模。


"""


class MyCircularDeque:
    """循环双端队列"""

    def __init__(self, k: int):
        # 队列的最大容量：多加1个的原因，是为了方便后面判断队列是否已经加满数据：
        # (self.tail + 1) % self.capacity == self.head
        # 也就是说tail所指向的位置始终是空的
        self.capacity = k + 1
        self.data = [0] * self.capacity
        # 头部指向第 1 个存放元素的位置，
        # 插入时，先减，再赋值
        # 删除时，索引 +1（注意取模）
        self.head = 0
        # 尾部指向下一个插入元素的位置
        # 插入时，先赋值，再加
        # 删除时，索引 -1（注意取模）
        self.tail = 0

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.head = (self.head - 1 + self.capacity) % self.capacity
            self.data[self.head] = value
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.data[self.tail] = value
            self.tail = (self.tail + 1) % self.capacity
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            # head 被设计在数组的开头，所以是 +1
            self.head = (self.head + 1) % self.capacity
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            #  tail 被设计在数组的末尾，所以是 -1
            self.tail = (self.tail - 1 + self.capacity) % self.capacity
            return True
        return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.data[self.head]
        return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            # 当 tail 为 0 时防止数组越界
            return self.data[(self.tail - 1 + self.capacity) % self.capacity]
        return -1

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def isFull(self) -> bool:
        # 注意：这个设计是非常经典的做法
        return (self.tail + 1) % self.capacity == self.head


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

if __name__ == '__main__':
    # [null, true, true, -1, true, true, 0, 5, 0, 0, 5, false]
    # [null, true, true, -1, true, true, 0, 0, 0, 0, 0, false]
    # [[2],[7],[],[],[5],[0],[],[],[],[],[],[0]]
    deque = MyCircularDeque(2)
    print(deque.insertFront(7))
    print(deque.deleteLast())
    print(deque.data)  # [-1, 7]

    print(deque.getFront())
    print(deque.insertLast(5))
    print(deque.insertFront(0))
    print(deque.getFront())
    print(deque.data)  # [0, 7]

    print(deque.getRear())  # [5]
    print(deque.getFront())
    print(deque.getFront())
    print(deque.getRear())
    print(deque.insertLast(0))
