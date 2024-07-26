class MinHeap:
    # 把最大堆实现中不等号的方向反向就可以了
    def __init__(self, capacity):
        # 因为数组从索引 1 开始存放数值
        # 所以开辟 capacity + 1 这么多大小的空间
        self.data = [0 for _ in range(capacity + 1)]
        self.count = 0
        self.capacity = capacity

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def insert(self, item):
        if self.count + 1 > self.capacity:
            raise Exception('堆的容量不够了')
        self.count += 1
        self.data[self.count] = item
        self.__swim(self.count)

    def __swim(self, k):
        # 上浮，与父节点进行比较
        temp = self.data[k]
        while k > 1 and self.data[k // 2] > temp:
            self.data[k] = self.data[k // 2]
            k //= 2
        self.data[k] = temp

    def extract_min(self):
        if self.count == 0:
            raise Exception('堆里没有可以取出的元素')
        ret = self.data[1]
        self.data[1] = self.data[self.count]
        self.count -= 1
        self.__sink(1)
        return ret

    def __sink(self, k):
        # 下沉
        temp = self.data[k]
        while 2 * k <= self.count:
            j = 2 * k
            if j + 1 <= self.count and self.data[j + 1] < self.data[j]:
                j += 1
            if temp <= self.data[j]:
                break
            self.data[k] = self.data[j]
            k = j
        self.data[k] = temp
