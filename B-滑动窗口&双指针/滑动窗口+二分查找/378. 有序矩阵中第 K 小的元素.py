"""
给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。

你必须找到一个内存复杂度优于 O(n2) 的解决方案。

 

示例 1：
输入：matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
输出：13
解释：矩阵中的元素为 [1,5,9,10,11,12,13,13,15]，第 8 小元素是 13

示例 2：
输入：matrix = [[-5]], k = 1
输出：-5
 

提示：
n == matrix.length
n == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
题目数据 保证 matrix 中的所有行和列都按 非递减顺序 排列
1 <= k <= n2
 

进阶：

你能否用一个恒定的内存(即 O(1) 内存复杂度)来解决这个问题?
你能在 O(n) 的时间复杂度下解决这个问题吗?这个方法对于面试来说可能太超前了，但是你会发现阅读这篇文章（ this paper ）很有趣。
"""

import heapq
from typing import List

# todo 方法3：二分答案（最优解！）+ 双指针 (困难~)
# 类似：B-滑动窗口&双指针\滑动窗口\滑动窗口+二分查找\719. 找出第 K 小的数对距离.py


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # n x n 矩阵matrix每行和每列元素均按升序排序，返回矩阵中第 k 小的元素
        n = len(matrix)

        def check(mid: int) -> bool:
            # 判断矩阵中小于等于mid的元素个数，是否>=k
            i = n - 1  # 行索引
            j = 0      # 列索引
            cnt = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    # 由于每列都是升序，该列[0..i]行元素都是<=mid，总个数为i+1; j切换到下一列
                    cnt += i + 1
                    j += 1
                else:
                    # matrix[i][j] > mid, 由于每行都是升序，该行[j..n-1]列元素都是>mid; i切换到上一行
                    i -= 1
            return cnt >= k

        # 矩阵中元素的最小值和最大值
        lo = matrix[0][0]
        hi = matrix[-1][-1]
        while lo < hi:
            # 二分答案，每次取中间值，然后判断有没有可能是第k小的元素
            mid = (lo + hi) // 2
            if check(mid):
                # mid是一个可能解
                hi = mid
            else:
                lo = mid + 1

        return lo


# todo 方法2：堆 + 链表双指针 + 归并排序
# 类似： 23. 合并K个升序链表
# 由题目给出的性质可知，这个矩阵的每一行均为一个有序数组。问题即转化为从这 n 个有序数组中找第 k 大的数，
# 可以想到利用归并排序的做法，归并到第 k 个数即可停止。
# 一般归并排序是两个数组归并，而本题是 nnn 个数组归并，所以需要用小根堆维护，以优化时间复杂度。

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # n x n 矩阵matrix每行和每列元素均按升序排序，返回矩阵中第 k 小的元素
        n = len(matrix)

        # 初始化优先级队列，把每一行的第一个元素装进去
        # 存储二元组 (matrix[i][j], i, j)
        # i, j 记录当前元素的索引位置，用于生成下一个节点
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)

        # n 个有序数组中找第 k 大的数
        for _ in range(k-1):
            num, x, y = heapq.heappop(pq)
            # 链表中的下一个节点加入优先级队列
            if y + 1 < n:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))

        return heapq.heappop(pq)[0]


# 方法一：直接排序
# 最直接的做法是将这个二维数组转成一维数组，并对该一维数组进行排序。最后这个一维数组中的第 k 个数即为答案。
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = sorted(sum(matrix, []))
        """
        sum(matrix, []) 将嵌套列表 matrix 展开为一个单一的列表，通过连接其子列表中的元素
            sum() 函数遍历可迭代对象中的每个元素（在这里是 matrix 的子列表）。
            它从一个空列表（[]）作为初始值开始。
            对于每个子列表，它将其元素添加到累加总和中。
            最终结果是包含原始矩阵中所有元素的展开列表。
        >>> matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
        >>> print(sum(matrix, []))  # [1, 5, 9, 10, 11, 13, 12, 13, 15]
        """

        return ans[k - 1]


"""
写在最后
上述三种解法，
第一种没有利用矩阵的性质，所以时间复杂度最差；
第二种解法只利用了一部分性质（每一行是一个有序数列，而忽视了列之间的关系）；
第三种解法则利用了全部性质，所以时间复杂度最佳。
"""
