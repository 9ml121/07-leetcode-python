"""
给定一个二进制数组 nums 和一个整数 k 。

k位翻转 就是从 nums 中选择一个长度为 k 的 子数组 ，同时把子数组中的每一个 0 都改成 1 ，把子数组中的每一个 1 都改成 0 。

返回数组中不存在 0 所需的最小 k位翻转 次数。如果不可能，则返回 -1 。

子数组 是数组的 连续 部分。

 

示例 1：
输入：nums = [0,1,0], K = 1
输出：2
解释：先翻转 A[0]，然后翻转 A[2]。

示例 2：
输入：nums = [1,1,0], K = 2
输出：-1
解释：无论我们怎样翻转大小为 2 的子数组，我们都不能使数组变为 [1,1,1]。

示例 3：
输入：nums = [0,0,0,1,0,1,1,0], K = 3
输出：3
解释：
翻转 A[0],A[1],A[2]: A变成 [1,1,1,1,0,1,1,0]
翻转 A[4],A[5],A[6]: A变成 [1,1,1,1,1,0,0,0]
翻转 A[5],A[6],A[7]: A变成 [1,1,1,1,1,1,1,1]
 

提示：
1 <= nums.length <= 10^5
1 <= k <= nums.length
"""


import collections
# 3191. 使二进制数组全部等于 1 的最少操作次数 I.py  进阶题目
# 3192. 使二进制数组全部等于 1 的最少操作次数 II.py
# 995. K 连续位的最小翻转次数

# todo 方法二：固定长度滑窗 + 双向队列
class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        # 翻转长度为k的子数组，将0和1互改，返回nums不存在0的最少翻转次数
        n = len(nums)
        # todo 队列模拟滑动窗口，该滑动窗口的含义是前面 k-1 个元素中，以哪些位置起始的 子区间 进行了翻转
        # 该滑动窗口从左向右滑动，如果当前位置 i 需要翻转，则把该位置存储到队列中。
        # 遍历到新位置 j(j<i+K) 时，队列中元素的个数代表了 i 被前面 k-1 个元素翻转的次数。
        q = collections.deque()
        ans = 0
        
        for i in range(n):
            # todo 出：窗口固定长度为 k, q[0]代表窗口左边姐元素坐标，超过长度 k要及时移除左边界
            if q and i >= q[0] + k:
                q.popleft()
            
            # todo 入：通过判断当前元素值和窗口内前面元素翻转次数是奇数还是偶数次，判断是否要进行翻转
            # 如果nums[i]==0 并且 当前窗口前面翻转了偶数次，表示当前元素需要翻转，把i加到队列中。
            # 如果nums[i] == 1 并且 当前窗口前面翻转了奇数次，表示当前元素需要翻转，因此也要将i加到队列中。
            if len(q) % 2 == nums[i]: 
                if i + k > n:
                    # todo 当 i+k>n 时，说明需要翻转大小为 K 的子区间，但是后面剩余的元素不到 K 个了，所以返回 -1。
                    return -1
                q.append(i)
                ans += 1
        return ans
    
# 方法一：模拟翻转，时间复杂度：O(N*K)，超时。
class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        # 翻转长度为k的子数组，将0和1互改，返回nums不存在0的最少翻转次数
        n = len(nums)
        ans = 0
        # 1.模拟翻转：从左到右遍历nums，遇到数字为 0，那么翻转以该数字为起始的 K 个数字
        for i in range(n-k + 1):
            if nums[i] == 0:
                ans += 1
                for j in range(k):
                    nums[i + j] ^= 1
                
        # 2.判断最后 k-1位是否都为 1
        for i in range(n-k+1, n):
            if nums[i] == 0:
                return -1
        return ans


