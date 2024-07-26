"""
给你一个已经 排好序 的整数数组 nums 和整数 a 、 b 、 c 。对于数组中的每一个元素 nums[i] ，
计算函数值 f(x) = ax^2 + bx + c ，请 按升序返回数组 。

 

示例 1：

输入: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
输出: [3,9,15,33]
示例 2：

输入: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
输出: [-23,-5,1,7]
 

提示：

1 <= nums.length <= 200
-100 <= nums[i], a, b, c <= 100
nums 按照 升序排列
 

进阶：你可以在时间复杂度为 O(n) 的情况下解决这个问题吗？
"""
from typing import List

# todo 数学 + 左右双指针


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        # f(x) = ax^2 + bx + c 是一个抛物线，对称轴两边都是一个有序数组
        n = len(nums)
        ans = []

        def calc(x: int) -> int:
            return a * (x**2) + b*x + c

        # todo 执行合并两个有序数组的逻辑
        l = 0
        r = n-1
        while l <= r:
            nx = calc(nums[l])
            ny = calc(nums[r])
            if a >= 0:
                # 开口向上, 最终结果的最大值等于左右指针的较大值
                if nx >= ny:
                    ans.append(nx)
                    l += 1
                else:
                    ans.append(ny)
                    r -= 1
            else:
                # 开口向下, 最终结果的最小值等于左右指针的较小值
                if nx >= ny:
                    ans.append(ny)
                    r -= 1
                else:
                    ans.append(nx)
                    l += 1
        if a >= 0:
            ans.reverse()
        return ans
