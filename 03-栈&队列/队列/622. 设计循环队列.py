"""
设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：

MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。


示例：

MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
circularQueue.enQueue(1);  // 返回 true
circularQueue.enQueue(2);  // 返回 true
circularQueue.enQueue(3);  // 返回 true
circularQueue.enQueue(4);  // 返回 false，队列已满
circularQueue.Rear();  // 返回 3
circularQueue.isFull();  // 返回 true
circularQueue.deQueue();  // 返回 true
circularQueue.enQueue(4);  // 返回 true
circularQueue.Rear();  // 返回 4


提示：

所有的值都在 0 至 1000 的范围内；
操作数将在 1 至 1000 的范围内；
请不要使用内置的队列库。
"""
"""
思路分析：
「循环队列」特指用 数组 实现的队列，队列中的数据在数组中 循环赋值，利用了数组能够随机存储的特点，使得入队和出队操作的时间复杂度为 O(1)。

可以用数组实现栈，这是因为我们在数组真正存放数据的末尾维护了一个变量 size，在数组的末尾添加和删除元素是方便的。
事实上，在数组的开始位置也可以维护一个变量，通过这个变量维护添加或者删除元素在什么位置。

我们下面的描述都选择「在数组的末尾添加元素，在数组的开始位置删除元素」。
事实上，两个位置维护添加和删除操作都是容易的，请见本节例题 2。

1.设计 front 和 rear 变量
为了保证 出队 操作和 入队 操作都是 O(1) 时间复杂度，我们分别使用了两个指针变量 front 和 rear 分别指向队列的队首和队尾。
    - 队首位置 front 是数组中是第 1 个真正存放元素的位置，右移 front 表示将这个元素移出队列；
    - 队尾位置 rear 是下一个元素将要存放的位置，右移 rear 表示有新的元素加入队列。
即我们定义区间 [front, rear) 保存的是真正在队列中的元素，刚开始的时候，front 和 rear 指向同一个位置，表示此时队列为空。
这个定义像极了我们对于 滑动窗口 的定义，事实上，真正存放数据的区域在数组里就是像滑动窗口一样 循环向右 滑动。
    - 入队：在队列末尾添加一个元素。先将元素的值赋值到 rear 位置，然后维护 rear 的定义，将 rear 后移一格；
    - 出队：读取队首的元素，然后维护 front 的定义，将 front 向后移动一位即可。

2.如何实现循环利用
为了 让 front 指针变量前面的空间能够重复利用 ，我们让 front 和 rear 变量在数组上循环移动起来，
即 两个指针变量移动到数组的末尾 +1 位置的时候，让它们来到数组的开始位置 ，这一步操作对数组的长度取模即可，这就是 循环 的意思，
循环使得数组空间得到了有效的利用。


"""


class MyCircularQueue:

    def __init__(self, k: int):
        # 队列最大容量设置为 k
        self.capacity = k
        # 用数组实现循环赋值
        self.data = [0] * self.capacity
        # head 指向当前队列中最早入队的元素
        self.head = 0
        # tail 指向下一个添加到队尾的元素
        self.tail = 0
        # 队列实际元素个数
        self.size = 0

    def enQueue(self, value: int) -> bool:
        """向循环队列尾部插入一个元素"""
        if not self.isFull():
            self.data[self.tail] = value
            self.tail = (self.tail + 1) % self.capacity
            self.size += 1
            return True
        return False

    def deQueue(self) -> bool:
        """从循环队列头部删除一个元素"""
        if not self.isEmpty():
            self.head = (self.head + 1) % self.capacity
            self.size -= 1
            return True
        return False

    def Front(self) -> int:
        """从队首获取元素"""
        if not self.isEmpty():
            return self.data[self.head]
        return -1

    def Rear(self) -> int:
        """获取队尾元素"""
        if not self.isEmpty():
            # 防止索引越界
            return self.data[(self.tail - 1 + self.capacity) % self.capacity]
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
