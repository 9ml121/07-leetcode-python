from typing import List


class MaxHeap:
    def __init__(self, arr: List[int]):
        self.capacity = len(arr) + 1
        self.data = [0] * self.capacity
        self.size = len(arr)

        for i in range(self.size):
            self.data[i + 1] = arr[i]

        # 从 1 开始编号的堆最后一个非叶子结点的下标是 size // 2 （画图就可以观察出来）
        for i in range(self.size // 2, 0, -1):
            self.siftDown(i)

    def siftDown(self, k: int):
        while 2 * k <= self.size:
            j = 2 * k
            if j + 1 <= self.size and self.data[j + 1] > self.data[j]:
                j += 1
            if self.data[k] >= self.data[j]:
                break
            self.data[k], self.data[j] = self.data[j], self.data[k]
            k = j

