"""
给你一个长度为 n 的整数数组 nums ，其中 nums 的所有整数都在范围 [1, n] 内，且每个整数出现 一次 或 两次 。请你找出所有出现 两次 的整数，并以数组形式返回。

你必须设计并实现一个时间复杂度为 O(n) 且仅使用常量额外空间的算法解决此问题。



示例 1：

输入：nums = [4,3,2,7,8,2,3,1]
输出：[2,3]
示例 2：

输入：nums = [1,1,2]
输出：[1]
示例 3：

输入：nums = [1]
输出：[]


提示：

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
nums 中的每个元素出现 一次 或 两次
"""
from typing import List


# 解法 1：利用一个布尔数组模拟哈希集合：空间复杂度不满足 O(1)的需求
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        # 用数组模拟哈希集合
        seen = [False] * (n + 1)

        for num in nums:
            if seen[num] == False:
                seen[num] = True
            else:
                res.append(num)
        return res


# 解法 2：原地哈希:将元素交换到对应的位置，可以满足时间复杂度 O(n),空间复杂度 O(1)的需求
# 技巧：将遍历过的数字修改为负数
"""
nums = [4,3,2,7,8,2,3,1]
idx  0 1 2 3 4 5 6 7
     4 3 2 7 8 2 3 1
i=0  7 3 2 4 
i=0  3 3 2 4 8 2 7 1
i=0  2 3 3  
i=0  3 2 3
i=1  3 2 3 4 8 2 7 1
i=2  3 2 3 4 8 2 7 1
i=3  ...
i=4  3 2 3 4 1 2 7 8
i=4  1 2 3 4 3 2 7 8
i=5  1 2 3 4 3 2 7 8
"""


class Solution2:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        # 1.将元素交换到对应下标位置
        for i in range(n):
            # 数字范围[1..n],对应下标有 1 个偏移
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # 2.再次遍历 nums, 如检播到 nums[i] != i+1,表示重复
        for i in range(n):
            if nums[i] != i + 1:
                res.append(nums[i])

        return res


# 方法 3：使用正负号作为标记
"""
方法二：使用正负号作为标记
思路与算法：我们也可以给 nums[i] 加上「负号」表示数 i+1 已经出现过一次。
具体地，我们首先对数组进行一次遍历。
当遍历到位置 i 时，我们考虑 nums[nums[i]−1] 的正负性：
    1.如果 nums[nums[i]−1] 是正数，说明 nums[i] 还没有出现过，我们将 nums[nums[i]−1] 加上负号；
    2.如果 nums[nums[i]−1] 是负数，说明 nums[i] 已经出现过一次，我们将 nums[i] 放入答案。

细节
由于 nums[i] 本身可能已经为负数，因此在将 nums[i] 作为下标或者放入答案时，需要取绝对值。

 0  1  2  3  idx
 4  2  2  3  nums
 4  2  2 -3  i=0
 4 -2  2 -3  i=1
 4 -2  2 -3  i=2
res = [2]
 4 -2 -2 -3  i=3
"""


class Solution3:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            x = abs(x)
            if nums[x - 1] > 0:
                nums[x - 1] = -nums[x - 1]
            else:
                ans.append(x)
        return ans
