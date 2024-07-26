"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:
MinStack() 初始化堆栈对象。
void push(int value) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。


示例 1:
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.


提示：
-2^31 <= value <= 2^31 - 1
pop、top 和 getMin 操作总是在 非空栈 上调用
push, pop, top, and getMin最多被调用 3 * 10^4 次
"""

# todo 单调栈

# 方法1：使用两个栈
class MinStack:
    # 能在常数时间内检索到最小元素的栈
    def __init__(self):
        # 数据栈：记录栈中的所有元素, push，pop都是正常操作这个正常栈
        self.stack = []
        # 辅助栈：阶段性记录栈中的最小元素
        # - 每次push，如果比最小栈的栈顶还小，我们就push进最小栈，否则不操作
        # - 每次pop的时候，我们都判断其是否和最小栈栈顶元素相同，如果相同，那么我们pop掉最小栈的栈顶元素即可
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        top = self.stack.pop()
        if self.minStack and self.minStack[-1] == top:
            self.minStack.pop()
        return top

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]



# 方法2：使用一个栈
class MinStack:
    # 能在常数时间内检索到最小元素的栈
    def __init__(self):
        self.minV = float('inf')
        self.stack = []

    def push(self, x: int) -> None:
        # 每次入栈的时候，stack保存的不再是真正的数字，而是它与当前最小值的差
        self.stack.append(x - self.minV)
        if x < self.minV:
            self.minV = x

    def pop(self) -> None:
        if not self.stack:
            return
        top = self.stack.pop()
        if top < 0:
            self.minV -= top

    def top(self) -> int:
        # top的时候涉及到对数据的还原，这里千万注意是上一个最小值
        if not self.stack:
            return
        top = self.stack[-1]
        if top < 0:
            return self.minV
        else:
            return self.minV + top

    def getMin(self) -> int:
        return self.minV


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
