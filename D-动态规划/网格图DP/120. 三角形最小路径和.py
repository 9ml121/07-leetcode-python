"""
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。


示例 1：
输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

示例 2：
输入：triangle = [[-10]]
输出：-10


提示：
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104


进阶：

你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？
"""
from typing import List

# todo 动态规划(多维dp)
# 写法1
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 给定一个三角形 triangle ，找出自顶向下的最小路径和。
        # 如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1
        n = len(triangle)
        # todo dp[i][j] 表示从三角形顶点到[i,j]的最小路径和，最后返回结果是dp最后一行的最小值
        dp = [[0] * (i + 1) for i in range(n)]  # 第i行的长度为i+1
        dp[0][0] = triangle[0][0]

        # 从三角形第2行开始向下递推
        for i in range(1, n):
            for j in range(i + 1): # 枚举第i行每个位置
                if j == 0:
                    # 当前行第一个位置
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif j == i:
                    # 当前行最后一个位置
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    # 当前行中间位置
                    dp[i][j] = min(dp[i - 1][j-1], dp[i - 1][j]) + triangle[i][j]

        # 返回结果是dp最后一行的最小值
        return min(dp[-1])

# todo 写法2(推荐写法！！)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 给定一个三角形 triangle ，找出自顶向下的最小路径和。
        # 如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1
        n = len(triangle)
        # todo dp[i][j] 表示从点 triangle[i-1, j] 到顶点的最小路径和,最后返回结果是dp[0][0]
        # 注意：这里行数是n+1，最后多的一行初始值为0, 方便后面dp推导不用考虑越界
        dp = [[0] * (i + 1) for i in range(n + 1)]

        # 从三角形的最后一行(dp的倒数第二行)开始向上递推
        for i in range(n-1, -1, -1):
            for j in range(i + 1):  # 枚举第i行每个位置
                dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])

        return dp[0][0]


# dp空间优化：二维数组压缩为滚动更新的一维数组
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 给定一个三角形 triangle ，找出自顶向下的最小路径和。
        # 如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1
        n = len(triangle)
        # todo dp[i] 表示 triangle[i]这条边计算得到的最小路径和, 初始化为triangle最后一行，最后返回结果是dp[0]
        # dp会在后面遍历中滚动更新
        dp = triangle[-1]

        # 从三角形的最后一行(也是dp的最后一行)开始向上递推
        for i in range(n-1, -1, -1):
            for j in range(i + 1):  # 枚举第i行每个位置
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
    
        return dp[0]


if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
