"""
题目描述：
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

示例 2：

输入：height = [4,2,0,3,2,5]
输出：9

提示：

- n == height.length
- 0 <= n <= 3 * 10^4
- 0 <= height[i] <= 10^5
"""
from typing import List

"""
# 前面用双指针做过一次，这次换单调栈解法:
从左向右 看，在柱形的高度递减（或者非递增）的时候，不能存雨水，我们将它们一次放入一个缓存中；
可以形成凹槽的条件是，
    当前看到的柱形的高度比此时在缓存中 最后添加 的那个柱形的高度严格大，
    由于 缓存中保存柱形的高度是单调不增 的，此时形成了一个凹槽，
    可以计算出缓存中 最后添加 的那个柱形与两边柱形形成的雨水量；

这种计算的顺序符合 后添加到缓存中的柱形先计算 的规律，因此，这个缓存是 栈；
由于计算存雨水量需要计算两边柱子之间的距离，因此我们 在栈里存的是柱形的下标；

雨水量 = 底 × 高。
    底 = 左右两个柱形（虚线当做不存在）的下标之差 - 1，
    高 = 左右两个柱形（虚线当做不存在）高度中较矮的那个。

"""

# todo 考察单调栈：及时去掉无用数据，保持栈的单调性
# 方法1：单调栈
class Solution:
    def trap(self, height: List[int]) -> int:
        # 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
        ans = 0
        # st单调递减, 保存前面还不能计算凹槽面积的柱子索引
        st = []

        for i, h in enumerate(height):
            while st and h > height[st[-1]]:
                top = st.pop()
    
                if not st: # 不能形成凹槽
                    break
                
                # todo 计算凹槽面积：
                # 根据木桶原理，凹槽高度取决于 i 的高度和弹栈以后的新栈顶元素的高度
                dh = min(h, height[st[-1]]) - height[top]
                # 凹槽宽度
                dw = i - st[-1] - 1
                ans += dh * dw

            st.append(i)
        return ans


# 方法2：双指针
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        l = 0
        r = n-1
        pre_max = 0  # 前缀最大值
        suf_max = 0  # 后缀最大值

        # 左右指针往中间移动，直到相遇
        while l <= r:
            pre_max = max(pre_max, height[l])
            suf_max = max(suf_max, height[r])
            if pre_max <= suf_max:
                ans += pre_max - height[l]
                l += 1
            else:
                ans += suf_max - height[r]
                r -= 1
        return ans
