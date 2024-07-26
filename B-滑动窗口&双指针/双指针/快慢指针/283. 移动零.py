"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。


示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

示例 2:
输入: nums = [0]
输出: [0]


提示:
1 <= nums.n <= 10^4
-2^31 <= nums[i] <= 2^31 - 1


进阶：你能尽量减少完成的操作次数吗？
"""

from typing import List

# todo 简单的快慢指针
# 类似 A-滑动窗口&双指针\双指针\27. 移除元素.py

class Solution:
    """
    解题思路：
    如果题目没有要求 modify in-place 的话，可以先遍历一遍nums将包含 0 的和不包含 0 的存到两个数组，然后拼接两个数组即可
    如果 modify in-place ，空间复杂度降低为 1, 可以使用读写双指针来做。具体来说使用一个慢指针表示写指针，快指针表示读指针
    """
    # 写法1：赋值
    def moveZeroes(self, nums: List[int]) -> None:
        """原地移动数组nums中的元素0到数组末尾"""
        n = len(nums)
        # nums[0..l)不包含0, l代表写指针，r代表读指针
        l = 0
        for r, num in enumerate(nums):
            # 读指针不断往后移动。如果遇到非 0，则将读到的值写入写指针，触发写指针移动（其他情况写指针不动），读指针走到头算法结束。
            if num != 0:
                nums[l] = num
                l += 1

        # nums[l..n)全部为0
        for r in range(l, n):
            # 经过上面处理，最终写指针l的位置前面就是所有的非 0 数了， 最后将写指针l后的 位置全部修改为 0 即可。
            nums[r] = 0

    # 写法2：交换
    def moveZeroes(self, nums: List[int]) -> None:
        """原地移动数组nums中的元素0到数组末尾"""
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
            fast += 1
