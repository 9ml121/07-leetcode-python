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


# 计数排序版本一：不考虑负数,可以保证排序稳定性,
# 非原地排序(需要一个长度max_val + 1的计数数组和nums_copy数组)
def countingSort(nums):
    """
    nums = [2, 5, 3, 0, 2, 3, 0, 3]
    """
    # 1.找到数组中的最大值，以确定计数数组的长度
    max_val = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        if num > max_val:
            max_val = nums[i]
        # 数据有效性校验，因为要将数值作为数组 count 的下标使用，因此 nums[i] 不能小于 0
        if num < 0:
            raise ValueError("该数组不适合使用计数排序")

    # 2.对原始数组进行计数，这里将原始数组的值，作为了计数数组的下标
    count = [0] * (max_val + 1)  # +1是因为有0值
    for num in nums:
        count[num] += 1

    # 3.将 count 数组改造成前缀和数组，我们需要的是前缀和，在原地进行变换即可
    # 由前缀和数组就可以推出这个元素所在的位置
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    # 4.从后向前扫描nums_copy，依次把看到的数写回原始数组，从后向前是为了保证稳定性
    # 为了写回去，需要对原始数组做一个拷贝
    nums_copy = nums.copy()
    for num in reversed(nums_copy):
        # 位置有一个偏移，在纸上写出来就很容易发现规律
        idx = count[num] - 1
        # 把看到的数覆盖回去
        nums[idx] = num
        # 前缀和减一，作为下一个看到的相同数存放位置的依据
        count[num] -= 1


# 计数排序版本二：考虑到负数的计数排序，但是不考虑稳定性
def countingSort2(nums):
    """
    nums = [-1, 0, 1, -2, 3, -2]
    """
    # 1. 找出最大和最小值,以确定计数数组的长度
    max_val = max(nums)
    min_val = min(nums)

    # 2.初始化计数数组, 并统计每个数字出现的次数
    count = [0] * (max_val - min_val + 1)
    for num in nums:
        count[num - min_val] += 1

    # 4.创建结果数组的起始索引idx，并遍历计数数组, 将计数数组对应的数字按照位数排序
    idx = 0
    for i in range(len(count)):
        for _ in range(count[i]):  # count[i]代表i+min_val的出现次数
            nums[idx] = i + min_val
            idx += 1


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        countingSort(nums)
        # countingSort2(nums)
        return nums


if __name__ == '__main__':
    solution = Solution()

    nums1 = [2, 5, 3, 0, 2, 3, 0, 3]
    print(solution.sortArray(nums1))

    # nums2 = [-1, 0, 1, -2, 3, -2]
    # print(solution.sortArray(nums2))
