"""
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。


示例 1：
输入：
matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]]
输出：4

示例 2：
输入：
matrix = [
        ["0","1"],
        ["1","0"]]
输出：1

示例 3：
输入：matrix = [["0"]]
输出：0
 

提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] 为 '0' 或 '1'
"""
from typing import List

# todo 方法1：动态规划(多维dp，推荐写法) 
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
        
        m, n = len(matrix), len(matrix[0])
        # 可以找到的正方形最大边长
        max_edge = 0
        # todo dp[i][j] 代表 以matrix[i][j]这个位置为正方形的最后一个位置，可以得到的最大边长
        dp = [[0] * n for _ in range(m)]
        
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        # 第一行，或者第一列的坐标
                        dp[i][j] = 1
                    else:
                        # 从第二行，第二列开始的dp状态可能由左边，上边或者左上角3个位置传递过来
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1],
                                       dp[i-1][j-1]) + 1

                    max_edge = max(max_edge, dp[i][j])

        return max_edge * max_edge

# todo 动态规划写法2
class Solution2:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
        ans = 0
        m, n = len(matrix), len(matrix[0])
        offsets = [(-1, 0), (0, -1), (-1, -1)]  # 左，上，左上角
        # todo dp[i][j] 代表 以matrix[i][j]这个位置为正方形的最后一个位置，可以得到的最大边长
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    # todo edge代表当前位置的左，上和左上角3个位置为正方形的最后一个位置，最小的那个正方形边长
                    edge = float('inf')
                    
                    for ox, oy in offsets:  # 遍历左，上和左上角3个位置
                        nx, ny = i + ox, j + oy
                        # 其中任意一个位置越界，或者值为0 => 必然不能组成正方形
                        if not (0<=nx<m and 0<=ny<n) or dp[nx][ny] == 0:
                            edge = 0
                            break
                
                        edge = min(edge, dp[nx][ny])
                    
                    # todo 当前位置为正方形的最后一个位置，能够获得的最大边长    
                    dp[i][j] = edge + 1  
                    # 更新ans
                    ans = max(ans, dp[i][j] * dp[i][j])

        return ans
