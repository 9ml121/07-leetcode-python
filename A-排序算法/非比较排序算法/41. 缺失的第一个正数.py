"""
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。


示例 1：

输入：nums = [1,2,0]
输出：3
示例 2：

输入：nums = [3,4,-1,1]
输出：2
示例 3：

输入：nums = [7,8,9,11,12]
输出：1


提示：

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
"""
from typing import List


# 方法 1：借助hashSet实现，时间复杂度为O(N),空间复杂度为 O(N), 不符合题目空间复杂度 O(1)要求
class Solution1:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        n = len(nums)
        for i in range(1, n + 1):
            if i not in hashSet:
                return i
        return n + 1


# 方法 2：先排序，在找出缺少的最小正整数。时间复杂度为排序的时间 O(NlogN)，在加O(N)时间遍历一次数组，不符合题目时间复杂度 O(N)的需求
class Solution2:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 1.先排序
        nums.sort()

        # 2.遍历找到第一个突变的元素
        n = len(nums)
        seq = 0  # seq代表最小正整数的前一个数
        for i in range(n):
            if nums[i] == seq + 1:
                seq += 1
            elif nums[i] == seq or nums[i] <= 0:
                # 跳过非正整数和重复值
                continue
            elif nums[i] > seq + 1:
                # 找到第一个突变的元素
                break

        return seq + 1


# 方法3：原地哈希解法，时间复杂度O(N)， 空间复杂度O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        # 3 应该放在索引为 2 的地方
        # 4 应该放在索引为 3 的地方
        idx       0   1   2   3      n = 4
        nums    [ 3,  4, -1,  1]
        i=0     [-1,  4,  3,  1]
        i=1     [-1,  1,  3,  4]
                [ 1, -1,  3,  4]
        i=2     [ 1, -1,  3,  4]
        """
        n = len(nums)
        for i in range(n):
            # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # 注意：这里一定要把nums[nums[i] - 1]放在前面
                nums[nums[i] - 1], nums[i], = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


if __name__ == '__main__':
    nums = [3, 4, -1, 1]
    print(Solution().firstMissingPositive(nums))
