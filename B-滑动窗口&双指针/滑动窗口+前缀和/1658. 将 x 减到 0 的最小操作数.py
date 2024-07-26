"""
给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。
请注意，需要 修改 数组以供接下来的操作使用。

如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。

 
示例 1：
输入：nums = [1,1,4,2,3], x = 5
输出：2
解释：最佳解决方案是移除后两个元素，将 x 减到 0 。


示例 2：
输入：nums = [5,6,7,8,9], x = 4
输出：-1


示例 3：
输入：nums = [3,2,20,1,1,3], x = 10
输出：5
解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。
 

提示：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
1 <= x <= 10^9
"""



from math import inf
from typing import List

# todo 方法1：逆向思考 + 不固定长度滑窗（推荐！）
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 逆向思考：
        # 题目要求移出左右元素之和为x的最小操作数，可以转换为求剩下连续元素之和为s = sum(nums) - x 的最大长度max_cnt
        # 最后返回结果为n - max_cnt
        n = len(nums)
        s = sum(nums) - x
        if s < 0:
            return -1
        if s == 0:
            return n

        # win_sum：当前窗口元素之和，max_cnt:窗口元素之和为s的子序列最大长度
        # todo 循环不变量：nums[l..r]元素之和win_sum <= s
        win_sum = 0
        max_cnt = -inf

        l = 0
        for r, num in enumerate(nums):
            # 入
            win_sum += num

            # 出
            while win_sum > s:
                win_sum -= nums[l]
                l += 1

            # 更新ans
            if win_sum == s:
                max_cnt = max(max_cnt, r-l+1)

        # 最后答案
        ans = n - max_cnt if max_cnt != -inf else -1
        return ans


# todo 方法2：逆向思考 + 哈希表 + 前缀和
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 求移出左右元素之和为x的最小操作数，也就是求连续之数组之和为sum(nums)-x的最大长度
        n = len(nums)
        x = sum(nums) - x

        # todo vis[s] 表示nums前缀和为 s 的最小下标。
        vis = {0: -1}
        s = 0
        max_len = -inf

        for i, num in enumerate(nums):
            s += num
            if s not in vis:
                # 哈希表中不存在 s，则将其加入哈希表，其值为当前下标 i
                # todo nums[0..i]的前缀和为s
                vis[s] = i

            if s - x in vis:
                # todo 存在一个下标 j，nums[0..j]的和为s-x, 使得 nums[j+1,..i] 的和为 x
                j = vis[s-x]
                max_len = max(max_len, i-j)

        return -1 if max_len == -inf else n - max_len
