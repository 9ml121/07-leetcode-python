"""
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。



示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]


提示：

1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的


进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。
"""
import collections
import heapq
import queue
from typing import List


# 方法 1：利用collections.Counter的most_common功能数组
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        return [i[0] for i in counter.most_common(k)]


# 方法 2：利用优先队列自己实现 counter的 most_common功能
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        minHeap = [(-freq, num) for num, freq in counter.items()]
        heapq.heapify(minHeap)
        return [heapq.heappop(minHeap)[1] for i in range(k)]

    # 优先级队列的第2种写法
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        # 统计元素频率
        counter = collections.Counter(nums)

        # 创建优先队列
        pq = queue.PriorityQueue()

        # 将元素按照频率加入优先队列
        for num, freq in counter.items():
            pq.put((-freq, num))  # 使用负数表示频率，以实现最大堆

        # 取出前 k 个频率的元素
        result = []
        for _ in range(k):
            result.append(pq.get()[1])  # 取出元素值，忽略频率

        return result


"""
一种更优秀的解法是使用桶排序（Bucket Sort）。具体步骤如下： 
1. 首先，我们需要统计数组中每个元素的频率，存储在一个字典中。 
2. 创建一个列表，列表的索引表示元素的频率，列表的值表示对应频率的元素列表。 
3. 遍历字典中的每个元素，将元素按照频率放入对应频率的桶中。 
4. 从频率最高的桶开始，依次取出前 k 个元素，直到取出的元素数量达到 k。 

以上代码中，我们使用  Counter  类来统计元素频率，然后创建了一个桶列表  buckets 。
将元素按照频率放入对应的桶中，然后从频率最高的桶开始取出前 k 个元素，直到取出的元素数量达到 k。 
 
桶排序的时间复杂度为 O(n)，其中 n 是数组的长度。相较于使用优先队列的方法，桶排序的时间复杂度更低，更优秀。
下面是使用桶排序解答 LeetCode 347 题的 Python 代码示例：
"""


# 方法 3：桶排序解法
class Solution3:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计元素频率
        counter = collections.Counter(nums)

        # 创建桶， 桶的个数范围在[0..n]之间
        buckets = [[] for _ in range(len(nums) + 1)]

        # 将元素按照频率放入桶中
        for num, freq in counter.items():
            buckets[freq].append(num)

        # 从频率最高的桶开始取出前 k 个元素
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            result.extend(buckets[i])
            if len(result) >= k:
                break

        return result[:k]


"""
是的，除了使用优先队列和桶排序的方法，还有一种更优秀的解法是使用快速选择（Quick Select）算法。 
快速选择算法是基于快速排序的思想，可以在平均情况下以线性时间复杂度找到第 k 大的元素。具体步骤如下： 
1. 首先，我们需要统计数组中每个元素的频率，存储在一个字典中。 
2. 将字典中的键（即数组中的元素）存储在一个列表中。 
3. 使用快速选择算法找到第 k 大的频率。 
4. 遍历字典中的每个元素，将频率大于等于第 k 大频率的元素添加到结果列表中。 
下面是使用快速选择算法解答 LeetCode 347 题的 Python 代码示例：
"""


class Solution4:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计元素频率
        counter = collections.Counter(nums)
        # 将频率转换为列表
        freq_list = list(counter.values())

        # 使用快速选择算法找到第 k 大的频率
        def quick_select(left, right, k):
            pivot = freq_list[right]
            i = left
            for j in range(left, right):
                if freq_list[j] < pivot:
                    freq_list[i], freq_list[j] = freq_list[j], freq_list[i]
                    i += 1
            freq_list[i], freq_list[right] = freq_list[right], freq_list[i]
            if i == k:
                return freq_list[i]
            elif i < k:
                return quick_select(i + 1, right, k)
            else:
                return quick_select(left, i - 1, k)

        # 找到第 k 大的频率
        kth_freq = quick_select(0, len(freq_list) - 1, len(freq_list) - k)
        # 遍历字典，将频率大于等于第 k 大频率的元素添加到结果列表中
        result = []
        for num, freq in counter.items():
            if freq >= kth_freq:
                result.append(num)
        return result


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    sol = Solution4()
    print(sol.topKFrequent(nums, k))
