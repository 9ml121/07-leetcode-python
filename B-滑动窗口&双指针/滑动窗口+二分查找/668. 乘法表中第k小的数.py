"""
几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第 k 小的数字吗？

乘法表是大小为 m x n 的一个整数矩阵，其中 mat[i][j] == i * j（下标从 1 开始）。

给你三个整数 m、n 和 k，请你在大小为 m x n 的乘法表中，找出并返回第 k 小的数字。

 

示例 1：


输入：m = 3, n = 3, k = 5
输出：3
解释：第 5 小的数字是 3 。
示例 2：


输入：m = 2, n = 3, k = 6
输出：6
解释：第 6 小的数字是 6 。
 

提示：

1 <= m, n <= 3 * 104
1 <= k <= m * n
"""


# 解法同：B-滑动窗口&双指针\滑动窗口\滑动窗口+二分查找\378. 有序矩阵中第 K 小的元素.py

# todo 最优解：二分答案 + 双指针
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        '''乘法表：每行每列都是升序
            1   2   3   4
        1   1   2   3   4
        2   2   4   6   8
        3   3   6   9   12
        4   4   8   12  16
        '''
        def check(mid: int) -> bool:
            # 判断矩阵中小于等于mid的元素个数，是否>=k
            i = m   # 最后一行开始元素
            j = 1   # 第一列开始元素
            cnt = 0
            while i >= 1 and j <= n:
                if i*j <= mid:
                    # 由于每列都是升序，该列[1..i]行元素都是<=mid，总个数为i; j切换到下一列
                    cnt += i
                    j += 1
                else:
                    # matrix[i][j] > mid, 由于每行都是升序，该行[j..n]元素都是>mid; i切换到上一行
                    i -= 1
            return cnt >= k

        # 乘法表中的最小值和最大值
        lo = 1
        hi = m*n
        while lo < hi:
            # 二分答案，每次取中间值，然后判断有没有可能是第k小的元素
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
