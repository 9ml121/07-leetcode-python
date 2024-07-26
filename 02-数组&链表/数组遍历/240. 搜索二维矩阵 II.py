"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
 

示例 1：


输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true
示例 2：


输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
输出：false
 

提示：

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matrix[i][j] <= 109
每行的所有元素从左到右升序排列
每列的所有元素从上到下升序排列
-109 <= target <= 109

注意：本题与LCR 121. 寻找目标值 - 二维数组 相同:
https://leetcode.cn/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/description/
"""

import bisect
from typing import List


# 方法1：直接查找，时间复杂度O(M*N)
# todo 方法2：Z字形遍历: 类似 03-数组&链表\数组\6. Z 字形变换.py  (贪心思想)
# 时间复杂度 O(M+N) ：其中，M 和 N 分别为矩阵行数和列数，此算法最多循环 M+N次。
class Solution:
    # 写法1：
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 查找二维矩阵matrix是否有目标值target
        # 每行的元素从左到右升序排列
        # 每列的元素从上到下升序排列。
        
        # todo 将开始查找位置[x, y]设置为第一行最后一个数
        m, n = len(matrix), len(matrix[0])
        x = 0
        y = n - 1
        while x < m and y >= 0:
            num = matrix[x][y]
            if target == num:
                # 找到目标值
                return True
            if target < num:
                # 1.目标值小于行尾值，目标值只可能在当前行前面的元素中，y切换到当前行前一列值
                y -= 1
            else:
                # 2.目标值大于行尾值，目标值只可能在后面行，x切换到下一行
                x += 1
        return False

    # 写法2
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        # 查找二维矩阵matrix是否有目标值target
        # 每行的元素从左到右升序排列
        # 每列的元素从上到下升序排列。

        # todo 将开始查找位置[x, y]设置为最后一行第一个数
        m, n = len(matrix), len(matrix[0])
        x = m-1
        y = 0
        while x >= 0 and y < n:
            num = matrix[x][y]
            if target > num:
                # 如果target 大于行首元素，target只可能在该行右侧
                y += 1
            elif target < num:
                # 如果target 小于行首元素，target只可能在该行上边
                x -= 1
            else:
                return True

        return False

# 方法3：二分查找
# 由于矩阵 matrix 中每一行的元素都是升序排列的，因此我们可以对每一行都使用一次二分查找，判断 target 是否在该行中
# 时间复杂度：O(mlog⁡n)。对一行使用二分查找的时间复杂度为 O(log⁡n)，最多需要进行 m 次二分查找。
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            idx = bisect.bisect_left(row, target)
            if idx < len(row) and row[idx] == target:
                return True
        return False
