"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回 滑动窗口中的最大值 。

示例 1：

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

示例 2：
输入：nums = [1], k = 1
输出：[1]


提示：
1 <= nums.n <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.n
"""
import collections
import heapq
from typing import List


# todo 考察固定长度滑窗 + 单调队列/堆（方便O(1)找到窗口最大值）

# 方法1：定长滑窗 + 单调队列（推荐！）
# 写法2：dq保存元素索引，对应的值单调递减；窗口一次性遍历完(推荐！)
class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 返回 大小为k固定长度的滑动窗口中的最大值
        ans = []
        # todo dq保存nums大小为k的窗口元素索引下标，对应的nums值单调递减，dq[0]就是当前窗口最大值索引
        dq = collections.deque()

        for i, x in enumerate(nums):
            # 入：维护dq单调递减(这里可以是严格，也可以非严格)
            while dq and x >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)  # dq尾部添加的是新进入队列的元素下标

            if i >= k - 1:
                # 记录ans：当i滑到k-1位置时，开始记录窗口最大值
                ans.append(nums[dq[0]])
                
                # 出：下一个窗口需要移除i-k+1位置元素，并判断i-k+1位置是不是​窗口最大值
                if dq[0] == i-k+1:
                    dq.popleft()

        return ans


# 写法1：dq保存元素值，窗口分2阶段遍历
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 返回 大小为k固定长度的滑动窗口中的最大值列表
        ans = []
        # todo dq保存nums大小为k的窗口元素 值，单调递减，dq[0]就是当前窗口最大值
        dq = collections.deque()

        # 第一个窗口
        for i in range(k):
            # 维护dq非严格单调递减
            while dq and dq[-1] < nums[i]:  # todo dq保存值，这里必须是严格小于
                dq.pop()

            dq.append(nums[i])
        ans.append(dq[0])

        # 后续窗口
        for i in range(k, len(nums)):
            # 出：判断窗口移除元素nums[i-k]是否是最大元素
            if dq and nums[i-k] == dq[0]:
                dq.popleft()

            # 入：维护dq非严格单调递减
            while dq and dq[-1] < nums[i]:
                dq.pop()
            dq.append(nums[i])

            # 更新ans
            ans.append(dq[0])

        return ans

# 方法2：滑动窗口 + 堆


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 返回 大小为k固定长度的滑动窗口中的最大值列表
        n = len(nums)

        # todo 大根堆维护窗口元素和对应索引，当前窗口最大值就是-max_heap[0][0]
        # 第一个窗口
        max_heap = [(-nums[i], i) for i in range(k)]  # 注意 Python 默认的优先队列是小根堆
        heapq.heapify(max_heap)
        ans = [-max_heap[0][0]]

        # 后续窗口
        for i in range(k, n):
            # 入
            heapq.heappush(max_heap, (-nums[i], i))
            
            # 出
            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            
            # 更新ans
            ans.append(-max_heap[0][0])

        return ans


# 暴力解法：暴力解法的思路是遍历 所有 k 个长度的子区间，分别求出它们的最大值。
class Solution3:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sz = len(nums)
        # 滑动窗口元素个数为sz-k+1
        ans = [float('-inf')] * (sz - k + 1)
        for i in range(sz - k + 1):
            # 依次遍历滑动窗口k个元素，寻找出最大值
            # 暴力解法做了很多重复的工作，除了最开始的 k−1 个数和倒数  k−1 个数以外，每一个数都参与比较了 k 次。
            for j in range(i, i + k):
                ans[i] = max(ans[i], nums[j])
        return ans


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    cls = Solution()
    print(cls.maxSlidingWindow(nums, k))
