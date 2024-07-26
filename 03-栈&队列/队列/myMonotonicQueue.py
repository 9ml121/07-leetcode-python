import queue
from collections import deque
from typing import List


class MonotonicQueue:
    """实现单调递增队列"""

    def __init__(self):
        # 双向链表，支持头部和尾部增删元素
        # 维护其中的元素自尾部到头部单调递增
        self.maxq = deque()

    # 在尾部添加一个元素 n，维护 maxq 的单调性质
    def push(self, n: int) -> None:
        # 将前面小于自己的元素都删除
        while len(self.maxq) > 0 and self.maxq[-1] < n:
            self.maxq.pop()
        self.maxq.append(n)

    def max(self) -> int:
        # The first element of the queue is definitely the largest
        return self.maxq[0]  # 队头的元素肯定是最大的

    def pop(self, n: int) -> None:
        if n == self.maxq[0]:  # 如果当前最大值被弹出，则弹出队首元素
            self.maxq.pop(0)


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    """单调队列解决滑动窗口求最大值问题"""
    window = MonotonicQueue()
    res = []

    for i in range(len(nums)):
        if i < k - 1:
            # 先填满窗口的前 k - 1
            window.push(nums[i])
        else:
            # 窗口向前滑动，加入新数字
            window.push(nums[i])
            # 记录当前窗口的最大值
            res.append(window.max())
            # 移出旧数字
            window.pop(nums[i - k + 1])
    return res
