"""
给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。

根据维基百科上 h 指数的定义：h 代表“高引用次数” ，一名科研人员的 h 指数 是指他（她）至少发表了 h 篇论文，
并且每篇论文 至少 被引用 h 次。如果 h 有多种可能的值，h 指数 是其中最大的那个。



示例 1：
输入：citations = [3,0,6,1,5]
输出：3
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
     由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。

示例 2：
输入：citations = [1,3,1]
输出：1


提示：
n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
"""
from typing import List


# 方法 1：排序
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i, num in enumerate(citations):
            if i + 1 >= num:
                return max(num, i)

        return len(citations)


# 方法2:计数(推荐)
class Solution2:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counts = [0] * (n + 1)
        for val in citations:
            counts[min(n, val)] += 1  # 引用次数 > n，等价于引用次数为 n
        # print(counts)    #  [1, 1, 0, 1, 0, 2]

        H = 0
        for i in range(n, -1, -1):  # i=0 的时候，H>=i 一定成立
            H += counts[i]
            if H >= i:  # 说明有至少 i 篇论文的引用次数至少为 i
                return i


if __name__ == '__main__':
    nums = [3, 0, 6, 1, 5]
    nums = [1, 1, 3]
    nums = [8, 8]
    nums = [0, 0, 4, 4]
