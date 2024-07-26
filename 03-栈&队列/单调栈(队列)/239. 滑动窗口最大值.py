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


# todo 考察 固定长度滑窗 + 单调队列

# 暴力解法：遍历 所有 k 个长度的子区间，分别求出它们的最大值。
class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 滑窗大小为k, 返回 滑动窗口中的最大值
        n = len(nums)
        ans = [float('-inf')] * (n - k + 1)  # 滑动窗口个数为n-k+1
        
        for i in range(n - k + 1):
            for j in range(i, i + k):
                ans[i] = max(ans[i], nums[j])
        return ans



# todo 固定长度滑窗 + 单调双向队列: 及时去掉无用数据，保证队列单调性
# 写法1
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        # todo dq保存当前窗口的最大值，非严格单调递减，窗口最大值就在dq[0]
        dq = collections.deque()

        # 第一个窗口
        for i, x in enumerate(nums):
            x = nums[i]
            while dq and x > dq[-1]:  # 这里必须严格大于，因为dq保存的是值，要保留重复最大值
                dq.pop()

            dq.append(x)
        ans.append(dq[0])

        # 后续窗口
        for i in range(k, len(nums)):
            x = nums[i]
            # 判断窗口移除元素nums[i-k]是否是最大元素
            if dq and nums[i-k] == dq[0]:
                dq.popleft()

            while dq and x > dq[-1]:
                dq.pop()

            dq.append(x)

            # 添加当前窗口最大值到结果列表
            ans.append(dq[0])

        return ans

# 写法2：
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        # todo dq保存当前窗口的最大值索引，单调递减，窗口最大值就在dq[0]
        dq = collections.deque()

        for i, x in enumerate(nums):
            # 1.入
            while dq and x >= nums[dq[-1]]: # 这里严格或者非严格都可以，因为dq保存索引，具有唯一性
                dq.pop()

            dq.append(i)  

            # 2.出
            if i >= k and  i - k == dq[0]:
                dq.popleft()

            # 3.记录答案
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    cls = Solution()
    print(cls.maxSlidingWindow(nums, k))
