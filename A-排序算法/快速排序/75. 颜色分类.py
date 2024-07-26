"""
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。



示例 1：
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

示例 2：
输入：nums = [2,0,1]
输出：[0,1,2]


提示：
n == nums.n
1 <= n <= 300
nums[i] 为 0、1 或 2


进阶：
你能想出一个仅使用常数空间的一趟扫描算法吗？
"""
from typing import List

# todo 快速排序(原地排序)中的3指针技巧
# 题目最后给出的「进阶」要求，其实考察的是「快速排序」的子过程 partition，即：通过一次遍历，把数组分成三个部分。


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # nums只包含0,1,2三个元素，对nums原地排序， nums = [2,0,2,1,1,0]
        n = len(nums)

        l = 0  # l指向下一个要赋值为0的位置下标
        r = n-1  # r指向下一个要赋值为2的位置下标
        mid = 0  # mid用来遍历nums, 将0和2交换为l和r

        # [0..l) = 0
        # [l..mid) = 1
        # (r..n) == 2
        while mid <= r:
            if nums[mid] == 0:
                nums[l], nums[mid] = nums[mid], nums[l]
                l += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                # nums[mid] == 2
                nums[r], nums[mid] = nums[mid], nums[r]
                r -= 1


"""
上述代码指针移动图解：
        L         R
nums  1 0 2 2 0 1
        M
        L       R
nums  1 0 2 2 0 1
        M
            L     R
nums  0 1 2 2 0 1
        M
            L   R
nums  0 1 1 2 0 2
        M
            L R
nums  0 1 1 2 0 2
        M
            L
nums  0 1 1 0 2 2
        M   R
                L
nums  0 0 1 1 2 2
        M   R
       
"""
