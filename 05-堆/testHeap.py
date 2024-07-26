"""1.PriorityQueue"""
import queue

# 创建一个PriorityQueue对象
q = queue.PriorityQueue()
# 添加元素到队列中
q.put((2, 'data1'))
q.put((1, 'data2'))
q.put((3, 'data3'))
# 从队列中取出元素
item = q.get()
print(item)
# 检查队列是否为空
if q.empty():
    print("队列为空")
else:
    print("队列不为空")
# 获取队列中的元素个数
size = q.qsize()
print("队列中有{}个元素".format(size))


"""2.heapq"""
import heapq

# 创建一个空的堆
heap = []
# 向堆中添加元素
heapq.heappush(heap, (5, 'data1'))
heapq.heappush(heap, (3, 'data2'))
heapq.heappush(heap, (4, 'data3'))
# 从堆中弹出元素
item = heapq.heappop(heap)
print(item)
# 获取堆中最小的元素
item = heap[0]
print(item)
