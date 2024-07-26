"""
中位数是有序序列最中间的那个数。如果序列的长度是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。

例如：

[2,3,4]，中位数是 3
[2,3]，中位数是 (2 + 3) / 2 = 2.5
给你一个数组 nums，有一个长度为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。

 

示例：

给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。

窗口位置                      中位数
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7      -1
 1  3 [-1  -3  5] 3  6  7      -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
 因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。


提示：
你可以假设 k 始终有效，即：k 始终小于等于输入的非空数组的元素个数。
与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。
"""

import collections
import heapq
from heapq import *
from typing import List

# 中位数需要数组有序才能找到，用2个堆分别维护窗口最大值和最小值
# todo 双堆对顶 + 延迟删除（困难题，具体原理看官方高赞）

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # 找nums长度为k的滑动窗口中位数
        ans = []
        n = len(nums)

        small_maxHeap = []  # 大根堆保存math.ceil(k/2)的较小元素
        large_minHeap = []  # 小根堆保存k//2的较大元素
        remove_dict = collections.defaultdict(int)  # 字典保存需要从窗口移除的数字和个数

        # 第一个窗口
        for i in range(k):  
            heapq.heappush(small_maxHeap, -nums[i])
        for j in range(k//2):
            num = -heapq.heappop(small_maxHeap)
            heapq.heappush(large_minHeap, num)

        if k % 2 == 1:
            ans.append(-small_maxHeap[0])
        else:
            ans.append((large_minHeap[0]-small_maxHeap[0])/2)

        # 后续窗口
        balance = 0  # 标识small和large的元素是否达到平衡
        for i in range(k, n):  
            # 1.统计要移除的元素
            remove = nums[i-k]  
            remove_dict[remove] += 1

            if remove <= (-small_maxHeap[0]):  # todo remove需要从small中删除， 先不删除，只是记录
                balance += 1
            else:
                balance -= 1

            # 2.入
            insert = nums[i]
            if insert <= (-small_maxHeap[0]): # insert在small中插入
                heappush(small_maxHeap, -insert)
                balance -= 1
            else:
                heappush(large_minHeap, insert)
                balance += 1

            if balance > 0:  # balance > 0: 需要从large分元素到small
                heappush(small_maxHeap, -large_minHeap[0])
                heappop(large_minHeap)
            elif balance < 0:  # balance < 0: 需要从small分元素到large
                heappush(large_minHeap, -small_maxHeap[0])
                heappop(small_maxHeap)
            balance = 0  # 重置reset，表明已平衡

            # todo 3.出(处理欠债数):只有当2个堆顶元素(中位数)是要移出的数字时，才进行删除  
            while small_maxHeap and remove_dict[-small_maxHeap[0]] > 0:  
                remove_dict[-small_maxHeap[0]] -= 1
                heappop(small_maxHeap)
                
            while large_minHeap and remove_dict[large_minHeap[0]] > 0:
                remove_dict[large_minHeap[0]] -= 1
                heappop(large_minHeap)

            if k % 2 == 1:
                ans.append(-small_maxHeap[0])
            else:
                ans.append((large_minHeap[0]-small_maxHeap[0])/2)

        return ans
