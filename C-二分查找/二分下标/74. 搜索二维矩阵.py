"""
给你一个满足下述两条属性的 m x n 整数矩阵：

每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。



示例 1：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true

示例 2：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false


提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
"""
from typing import List


# todo 二分下标

# 二维矩阵使用二分查找优化写法（推荐）
# todo 二维数组转换为一纬数组，(x, y) => x * cols + y
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) << 1
            # todo 根据一维数组mid下标 计算 对应的二维数组所在的行列坐标
            mid_val = matrix[mid // cols][mid % cols]
            if mid_val < target:
                left = mid + 1
            elif mid_val > target:
                right = mid - 1
            else:
                return True
        return False
    
    
# 二维矩阵使用二分查找常规写法
class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        r0, r1 = 0, rows - 1
        while r0 <= r1:
            r_mid = (r0 + r1) // 2
            if matrix[r_mid][0] > target:
                r1 = r_mid - 1
            elif matrix[r_mid][cols - 1] < target:
                r0 = r_mid + 1
            else:
                # r0 <= t <= r1
                c0, c1 = 0, cols - 1
                while c0 <= c1:
                    c_mid = (c0 + c1) // 2
                    if matrix[r_mid][c_mid] < target:
                        c0 = c_mid + 1
                    elif matrix[r_mid][c_mid] > target:
                        c1 = c_mid - 1
                    else:
                        return True
                return False
        return False



