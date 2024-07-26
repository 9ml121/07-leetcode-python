"""
给你一个 m 行 n 列的二维网格 grid 和一个整数 k。你需要将 grid 迁移 k 次。

每次「迁移」操作将会引发下述活动：

位于 grid[i][j] 的元素将会移动到 grid[i][j + 1]。
位于 grid[i][n - 1] 的元素将会移动到 grid[i + 1][0]。
位于 grid[m - 1][n - 1] 的元素将会移动到 grid[0][0]。
请你返回 k 次迁移操作后最终得到的 二维网格。

 

示例 1：



输入：grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
输出：[[9,1,2],[3,4,5],[6,7,8]]
示例 2：



输入：grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
输出：[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
示例 3：

输入：grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
输出：[[1,2,3],[4,5,6],[7,8,9]]
 

提示：

m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100
"""


from typing import List


# 方法 1：模拟法
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                x = (i + (j+k)//n) % m
                y = (j+k) % n
                ans[x][y] = grid[i][j]

        return ans

# 方法 2：三次旋转
# 同189. 轮转数组
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        # 二维到一维
        arr = [grid[i][j] for i in range(n) for j in range(m)]
        # 取模，缩小k的范围，避免无意义的运算
        k %= m * n
        res = []
        
        # 首尾交换法
        def reverse(l:int, r:int)->None:
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
                
        # 三次旋转
        reverse(0, m * n - k - 1)
        reverse(m * n - k, m * n - 1)
        reverse(0, m * n - 1)
        
        # 一维到二维
        row = []
        for i in range(m * n):
            if i > 0 and i % m == 0:
                res.append(row)
                row = []
            row.append(arr[i])
        res.append(row)

        return res
