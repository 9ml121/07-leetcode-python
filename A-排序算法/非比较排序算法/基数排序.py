"""
leetcode912题：排序数组
给你一个整数数组 nums，请你将该数组升序排列。

示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]


提示：

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""
from typing import List


# 基数排序(基于计数排序)版本一： 只考虑非负整数，考虑排序的稳定性
# 非原地排序：需要借助一个长度为10的数位数组和nums_copy数组
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.radixSort(nums)

    def radixSort(self, nums: list) -> List:
        """
        nums = [329, 457, 657, 839, 436, 720, 355]
        1. 首先按照个位数字进，得到 [720, 355, 436, 457, 657, 329, 839]；
        2. 然后按照十位数字，得到 [720, 329, 436, 839, 355, 457, 657]；
        3. 然后按照百位数字，得到 [329, 355, 436, 457, 657, 720, 839]。
        """
        # 第 1 步：找出最大的数字,并校验数据有效性
        max_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > max_num:
                max_num = nums[i]
            if nums[i] < 0:
                #  数据有效性校验，因为要将数值作为 count 的索引用，因此 nums[i] 不能小于 0
                raise ValueError('该数组不适合使用计数排序')

        # 第 2 步：根据数位进行循环排序
        # 用于指定当前位数的值
        """
        // 表征关键字的量：除数
        // 1 表示按照个位关键字排序
        // 10 表示按照十位关键字排序
        // 100 表示按照百位关键字排序
        // 1000 表示按照千位关键字排序
        """
        carry = 1
        # 当最大值除以当前位数大于0时，说明还有更高位数需要排序
        while (max_num // carry) > 0:
            # 使用计数排序对当前位数进行排序
            self.countingSort(nums, carry)
            # print(nums)
            # 位数carry自增，表示采用低位优先的基数排序
            carry *= 10
        return nums

    def countingSort(self, nums, carry):
        """计数排序"""
        # 1.统计同一数位上出现的数字次数
        count = [0] * 10
        for num in nums:
            #  计算数位上的数是几，先取个位，再十位、百位
            remainder = (num // carry) % 10
            count[remainder] += 1

        # 2.计算每个数字在排序后的数组中的位置(前缀和)
        # 当统计每个数字出现的次数时，前缀和数组可以计算出数字的相对顺序
        for i in range(1, 10):
            count[i] += count[i - 1]

        # 3.从拷贝数组的末尾开始遍历，根据当前位数的值将数字放入对应位置(保证排序稳定性)
        # 为了写回去，需要对原始数组做一个拷贝
        nums_copy = nums.copy()
        for num in reversed(nums_copy):
            remainder = (num // carry) % 10
            # 位置有一个偏移
            idx = count[remainder] - 1
            nums[idx] = num
            count[remainder] -= 1


# 基数排序，考虑负数，考虑排序的稳定性
class Solution2:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.radixSort(nums)

    def radixSort(self, nums: list) -> List:
        # 1.找出数组中最大数和最小数
        max_num = float('-inf')
        min_num = float('inf')
        for num in nums:
            max_num = max(max_num, num)
            min_num = min(min_num, num)

        # 2.根据最小数将nums全部转换为非负整数
        for i in range(len(nums)):
            nums[i] += abs(min_num)
        max_num = max_num + abs(min_num)

        # 3.根据最大数的数位进行循环计数排序
        carry = 1
        while (max_num // carry) > 0:
            self.countingSort(nums, carry)
            carry *= 10

        # 4.将nums还原为原本数字
        for i in range(len(nums)):
            nums[i] -= abs(min_num)

        return nums

    # 计数排序
    def countingSort(self, nums, carry):
        # 1.计数数组统计每个数位上的数字出现的次数
        count = [0] * 10
        for num in nums:
            remainder = (num // carry) % 10
            count[remainder] += 1

        # 2.计算每个数字在排序后的数组中的位置(前缀和)
        for i in range(1, 10):
            count[i] += count[i - 1]

        # 3.根据计数数组计算排序后的数组中的位置
        nums_copy = nums.copy()
        for num in reversed(nums_copy):
            remainder = (num // carry) % 10
            # 位置有一个偏移
            idx = count[remainder] - 1
            nums[idx] = num
            count[remainder] -= 1


if __name__ == '__main__':
    nums = [329, 457, 657, 839, 436, 720, 355]
    sol = Solution()
    print(sol.sortArray(nums))

    arr = [170, -45, 75, -90, 802, -24, 2, -66]
    sol2 = Solution2()
    print(sol2.sortArray(arr))
