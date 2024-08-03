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


# todo 方法3：左右双指针（最优解）
# 11. 盛最多水的容器.py

class Solution:
    def trap(self, height: List[int]) -> int:
        # 计算下雨之后height数组可以接到的雨水量
        n = len(height)
        ans = 0

        # l 和 r 两个指针分别指向数组的左右两端，left_max 和 right_max 来记录左边和右边的最大值
        l = 0
        r = n-1
        l_max = 0
        r_max = 0

        # 从左右两端开始，向中间移动指针,并在每一步计算当前位置可以接到的雨水
        # 当 left 和 right 指针相遇时，我们就计算出了整个数组中可以存储的雨水量
        while l <= r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])

            # todo 类似11题，前、后缀最大值，哪边短就移动哪边指针，并在每一步计算当前位置可以接到的雨水
            if l_max <= r_max:
                ans += l_max - height[l]
                l += 1
            else:
                ans += r_max - height[r]
                r -= 1
        return ans


# todo 方法2：前后缀分解，动态转移只依赖前一个/后一个位置，进行空间压缩之后就是方法3的双指针解法
# 845. 数组中的最长山脉.py
# 1186. 删除一次得到子数组最大和.py


class Solution2:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # pre[i]代表height[i]的前缀最大值
        pre = [0] * n
        pre[0] = height[0]
        for i in range(1, n):  # 正向遍历
            pre[i] = max(height[i], pre[i - 1])

        # suf_max[i]代表height[i]的后缀最大值
        suf = [0] * (n)
        suf[n-1] = height[n-1]
        for i in range(n - 2, -1, -1):  # 逆向遍历
            suf[i] = max(height[i], suf[i + 1])

        # 遍历height每根柱子，计算能接的雨水总量
        ans = 0
        for h, pre, suf in zip(height, pre, suf):
            ans += min(pre, suf) - h

        return ans

# todo 方法4：单调栈：及时去掉无用数据，保持栈的单调性（最优解）


class Solution:
    def trap(self, height: List[int]) -> int:
        # 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
        ans = 0
        # st单调递减, 保存前面还不能计算凹槽面积的柱子索引
        st = []

        for i, h in enumerate(height):
            while st and h > height[st[-1]]:
                top = st.pop()

                if not st:  # 不能形成凹槽
                    break

                # todo 计算凹槽面积：
                # 根据木桶原理，凹槽高度取决于 i 的高度和弹栈以后的新栈顶元素的高度
                dh = min(h, height[st[-1]]) - height[top]
                # 凹槽宽度
                dw = i - st[-1] - 1
                ans += dh * dw

            st.append(i)
        return ans


# 方法1：暴力解法：O(N^2)，超时
"""
为此我们设计的暴力解法如下：
1.遍历每一个位置，计算每一个每一个位置能够储存的雨水的格子数。很容易知道，第 1 个位置和最后 1 个位置的柱子只能作为边界，它们不能储存雨水，
    因此需要计算的区间在 [1,len−2]；
2.遍历区间 [1,len−2] 里的每一个格子，计算出它左边的柱子的最高高度、右边的柱子的最高高度，取二者的最小值 minHeight。
3.然后和当前的柱子高度进行比较，如果当前柱子的高度严格小于 minHeight，就可以存雨水，存雨水的量就是二者之差。

时间复杂度：$O(n^2)$ 
空间复杂度：$O(1)$ 

暴力解法每一个位置能存水的格子数的计算我们都遍历了整个数组一次。
看到这个问题的时间复杂度与空间复杂度的关系，我们就不难看出优化的思路是「空间换时间」，
需要把遍历的结果记录下来。
"""


class Solution1:
    def trap(self, height: List[int]) -> int:
        # 计算按此排列的柱子，下雨之后能接多少雨水
        ans = 0
        n = len(height)

        def find_left_max(i: int) -> int:
            # 找height索引i左边最高柱子
            left_max = 0
            for i in range(i - 1, -1, -1):
                left_max = max(left_max, height[i])
            return left_max

        def find_right_max(i: int) -> int:
            # 找height索引i右边最高柱子
            right_max = 0
            for i in range(i + 1, n):
                right_max = max(right_max, height[i])
            return right_max

        # 遍历height每根柱子，统计能接到的所有雨水
        for i, h in enumerate(height):
            left_max = self.find_left_max(i)
            right_max = self.find_right_max(i)
            # 核心逻辑：只有当前柱子比左右两边最高柱子的较低值存在高度差，才能接到雨水
            if h < min(left_max, right_max):
                ans += min(left_max, right_max) - h
        return ans
