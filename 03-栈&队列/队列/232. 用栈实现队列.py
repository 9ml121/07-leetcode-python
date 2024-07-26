"""
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

实现 MyQueue 类：
    void push(int x) 将元素 x 推到队列的末尾
    int pop() 从队列的开头移除并返回元素
    int peek() 返回队列开头的元素
    boolean empty() 如果队列为空，返回 true ；否则，返回 false

说明：
你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。


示例 1：
输入：
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 1, 1, false]

解释：
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false


提示：
1 <= x <= 9
最多调用 100 次 push、pop、peek 和 empty
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）


进阶：
你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。
"""


# todo 利用辅助栈(双栈)，在 push 或者 pop 的时候，将数组在两个栈之间倒腾一次
class MyQueue:
    """请你仅使用两个栈实现先入先出队列。"""

    def __init__(self):
        self.st = []   
        self.help_st = []  

    def push(self, x: int) -> None:
        """将元素 x 推到队列的末尾"""
        while self.st:
            self.help_st.append(self.st.pop())
        self.help_st.append(x)
        
        while self.help_st:
            self.st.append(self.help_st.pop())

    def pop(self) -> int:
        """从队列的开头移除并返回元素"""
        return self.st.pop()

    def peek(self) -> int:
        """返回队列开头的元素"""
        return self.st[-1]

    def empty(self) -> bool:
        """判断队列是否为空"""
        return not self.st

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


"""
实际上现实中也有使用两个栈来实现队列的情况，那么为什么我们要用两个 stack 来实现一个 queue？

其实使用两个栈来替代一个队列的实现是为了在多进程中分开对同一个队列对读写操作。
一个栈是用来读的，另一个是用来写的。当且仅当读栈满时或者写栈为空时，读写操作才会发生冲突。
"""