# 最小堆完整代码
import heapq

# 新建一个列表
minHeap = []
# 将列表堆化，即将列表转换为最小堆
heapq.heapify(minHeap)
# 分别往最小堆中添加3，1，2
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 1)
heapq.heappush(minHeap, 2)
# 查看最小堆的所有元素，结果为：[1,3,2]
print("minHeap: ", minHeap)
# 获取最小堆的堆顶元素
peekNum = minHeap[0]
# 结果为：1
print("peek number: ", peekNum)
# 删除最小堆的堆顶元素
popNum = heapq.heappop(minHeap)
# 结果为：1
print("pop number: ", popNum)
# 查看删除1后最小堆的堆顶元素，结果为：2
print("peek number: ", minHeap[0])
# 查看最小堆的所有元素，结果为：[2,3]
print("minHeap: ", minHeap)
# 获取堆的元素个数，即堆的长度
size = len(minHeap)
# 结果为：2
print("minHeap size: ", size)
