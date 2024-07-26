"""
给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数，citations 已经按照 升序排列 。
计算并返回该研究者的 h 指数。

h 指数的定义：h 代表“高引用次数”（high citations），
一名科研人员的 h 指数是指他（她）的 （n 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。

请你设计并实现对数时间复杂度的算法解决此问题。



示例 1：
输入：citations = [0,1,3,5,6]
输出：3
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 0, 1, 3, 5, 6 次。
     由于研究者有3篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3 。

示例 2：
输入：citations = [1,2,100]
输出：2


提示：
n == citations.length
1 <= n <= 105
0 <= citations[i] <= 1000
citations 按 升序排列
"""
from typing import List


# 方法 1：常规查找
# 时间复杂度 O(N)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        for i, num in enumerate(reversed(citations)):
            if i + 1 >= num:
                return max(i, num)

        return len(citations)


# 方法 2：二分答案
# 时间复杂度：O(logn)
class Solution2:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2  # 中间靠左
            if citations[mid] >= n - mid:  # 有n−mid 篇论文被引用了至少 citations[mid] 次
                right = mid - 1
            else:
                left = mid + 1

        return n - left


# 二分查找写法 2：闭区间写法
class Solution3:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        # 在区间 [left, right] 内询问
        left = 1
        right = n

        while left <= right:  # 区间不为空, 最后 left > right
            # 循环不变量：
            # left-1 的回答一定为「是」
            # right+1 的回答一定为「否」
            mid = (left + right) // 2  # 中间靠左

            # 判断：有 mid 篇论文被引用了至少 citations[-mid] 次
            if citations[-mid] >= mid:
                # 引用次数最多的 mid 篇论文，引用次数均 >= mid，询问范围缩小到 [mid+1, right]
                left = mid + 1
            else:
                right = mid - 1

        # 循环结束后 right 等于 left-1，回答一定为「是」
        # 根据循环不变量，right 现在是最大的回答为「是」的数
        return right


if __name__ == '__main__':
    citations = [0, 1, 3, 5, 6]  # 3
    # citations = [1, 2, 100]  # 2
    # nums = [0]  # 0
    # nums = [8, 8]  # 2
    nums = [0, 0, 4, 4]  # 2
    print(Solution2().hIndex(citations))
    print(Solution2().hIndex(nums))
