"""
给定一个二维矩阵 matrix，以下类型的多个请求：

计算其子矩形范围内元素的总和，该子矩阵的 左上角 为 (row1, col1) ，右下角 为 (row2, col2) 。
实现 NumMatrix 类：

NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化
int sumRegion(int row1, int col1, int row2, int col2) 返回 左上角 (row1, col1) 、右下角 (row2, col2) 所描述的子矩阵的元素 总和 。

输入:
["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
输出:
[null, 8, 11, 12]

解释:
NumMatrix numMatrix = new NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (红色矩形框的元素总和)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (绿色矩形框的元素总和)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (蓝色矩形框的元素总和)


提示：
m == matrix.n
n == matrix[i].n
1 <= m, n <= 200
-105 <= matrix[i][j] <= 105
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
最多调用 104 次 sumRegion 方法
"""
from typing import List

'''
在一唯矩阵的基础上,要思考二维矩阵计算局部面积的方式:
sumRegion(self, row1: int, col1: int, row2: int, col2: int)
1.以(0,0)为原点,先计算原点到(row2, col2)形成的矩阵数据前缀和sum
2.以(0,0)为原点,在计算原点到(row2, col1)的前缀和sum1
3.以(0,0)为原点,在计算原点到(row1, col2)的前缀和sum2
4.以(0,0)为原点,在计算原点到(row1, col1)的前缀和sum3
最后计算(row1, col1) 到 (row2, col2)形成的矩阵 所有数据之和ans = sum - sum1 -sum2 + sum3
'''

# todo 二维矩阵前缀和数组
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        # 二维数组前缀和
        m = len(matrix)
        if m == 0: return  # 排除特殊情况
        n = len(matrix[0])
        
        # todo：preSum[i][j] 记录 matrix[i-1][j-1]到原点(0,0) 的累加和
        self.preSum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # todo 矩阵原点到当前位置的累加和 = 当前位置左边的累加和 + 上边的累加和 + 当前位置元素 - 左上角累加和
                self.preSum[i][j] = matrix[i - 1][j - 1] \
                                    + self.preSum[i][j - 1] \
                                    + self.preSum[i-1][j] \
                                    - self.preSum[i-1][j-1]

    # 计算子矩阵 [x1, y1, x2, y2] 的元素和
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.preSum[row2 + 1][col2 + 1] \
              - self.preSum[row2 + 1][col1] \
              - self.preSum[row1][col2 + 1] \
              + self.preSum[row1][col1]
        return ans




if __name__ == '__main__':
    matrix = [[3, 0, 1, 4, 2],
              [5, 6, 3, 2, 1],
              [1, 2, 0, 1, 5],
              [4, 1, 0, 1, 7],
              [1, 0, 3, 0, 5]]
    cls = NumMatrix(matrix)
    # [2,1,4,3],[1,1,2,2],[1,2,2,4]
    # [8, 11, 12]
    # pos = [2, 1, 4, 3]
    # pos = [1, 1, 2, 2]
    pos = [1, 2, 2, 4]
    res1 = cls.preSum
    ans = cls.sumRegion(*pos)
    print(res1)
    print(ans)

s = [[0, 0, 0, 0, 0, 0],
     [0, 3, 3, 4, 8, 10],
     [0, 8, 14, 18, 24, 27],
     [0, 9, 17, 21, 28, 36],
     [0, 13, 22, 26, 34, 49],
     [0, 14, 23, 30, 38, 58]]