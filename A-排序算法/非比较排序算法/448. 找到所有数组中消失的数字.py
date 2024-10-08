"""
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。



示例 1：

输入：nums = [4,3,2,7,8,2,3,1]
输出：[5,6]
示例 2：

输入：nums = [1,1]
输出：[2]


提示：

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
进阶：你能在不使用额外空间且时间复杂度为 O(n) 的情况下解决这个问题吗? 你可以假定返回的数组不算在额外空间内。
"""
from typing import List


# 方法 1：两个集合取差集
# 不满足空间复杂度 O（1）
class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        allSet = set(range(1, n + 1))
        subSet = set(nums)

        diff = allSet - subSet
        return list(diff)


# 方法 2：原地哈希
# 满足时间复杂度 O(N), 空间复杂的 O(1)
class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)

        for i in range(n):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # print(nums)
        for i in range(n):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res


# 方法 3：原地修改
"""
方法一：原地修改
思路及解法
我们可以用一个哈希表记录数组 nums 中的数字，由于数字范围均在 [1,n] 中，记录数字后我们再利用哈希表检查 [1,n] 中的每一个数是否出现，从而找到缺失的数字。
由于数字范围均在 [1,n] 中，我们也可以用一个长度为 n 的数组来代替哈希表。这一做法的空间复杂度是 O(n) 的。我们的目标是优化空间复杂度到 O(1)。

注意到 nums 的长度恰好也为 n，能否让 nums 充当哈希表呢？
由于 nums 的数字范围均在 [1,n]中，我们可以利用这一范围之外的数字，来表达「是否存在」的含义。

具体来说，
1. 遍历 nums，每遇到一个数 x，就让 nums[x−1] 增加 n。由于 nums 中所有数均在 [1,n] 中，增加以后，这些数必然大于 n。
2. 最后我们遍历 nums，若 nums[i] 未大于 n，就说明没有遇到过数 i+1。
3. 这样我们就找到了缺失的数字。

注意，当我们遍历到某个位置时，其中的数可能已经被增加过，因此需要对 n 取模来还原出它本来的值。
"""


class Solution3:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            x = (num - 1) % n
            nums[x] += n

        # print(nums)
        ret = [i + 1 for i, num in enumerate(nums) if num <= n]
        return ret


# 其他写法
class Solution4:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * (n + 1)
        for num in nums:
            count[num] += 1
        res = []
        for num in range(1, n + 1):
            if count[num] == 0:
                res.append(num)
        return res


class Solution5:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            # 注意索引，元素大小从 1 开始，有一位索引偏移
            if nums[abs(num) - 1] < 0:
                # 之前已经把对应索引的元素变成负数了，
                # 这说明 num 重复出现了两次，但我们不用做，让索引继续保持负数
                pass
            else:
                # 把索引 num - 1 置为负数
                nums[abs(num) - 1] *= -1

        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                # 说明没有元素和这个索引对应，即找到一个缺失元素
                res.append(i + 1)

        return res
