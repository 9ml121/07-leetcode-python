# 最大堆完整代码
import heapq

# 新建一个列表
maxHeap = []
# 将列表堆化，此时的堆是最小堆，我们需要将元素取反技巧，将最小堆转换为最大堆
heapq.heapify(maxHeap)
# 分别往堆中添加1，3，2，注意此时添加的是-1，-3，-2，原因是需要将元素取反，最后将最小堆转换为最大堆
heapq.heappush(maxHeap, 1 * -1)
heapq.heappush(maxHeap, 3 * -1)
heapq.heappush(maxHeap, 2 * -1)
# 查看堆中所有元素：[-3, -1, -2]
print("maxHeap: ", maxHeap)
# 查看堆中的最大元素，即当前堆中最小值*-1
peekNum = maxHeap[0]
# 结果为：3
print("peek number: ", peekNum * -1)
# 删除堆中最大元素，即当前堆中最小值
popNum = heapq.heappop(maxHeap)
# 结果为：3
print("pop number: ", popNum * -1)
# 查看删除3后堆中最大值， 结果为：2
print("peek number: ", maxHeap[0] * -1)
# 查看堆中所有元素，结果为：[-2,-1]
print("maxHeap: ", maxHeap)
# 查看堆的元素个数，即堆的大小
size = len(maxHeap)
# 结果为：2
print("maxHeap size: ", size)
