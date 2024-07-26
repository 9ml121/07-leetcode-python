"""
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例 1：
输入：board = [["X","X","X","X"],
              ["X","O","O","X"],
              ["X","X","O","X"],
              ["X","O","X","X"]]
输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

示例 2：
输入：board = [["X"]]
输出：[["X"]]


提示：
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] 为 'X' 或 'O'
"""
from typing import List

# 方法 1：DFS
"""
关键：与边界相连 O 不能被替换成 X。
具体步骤：
- 第 1 步：把四周有 O的地方都替换成为 -，在四周进行 floodfill 算法（染色）；
- 第 2 步：再从头到尾遍历一遍，把 O 换成 X，把 - 换成 O。
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def inArea(x, y):
            return 0 <= x < rows and 0 <= y < cols

        # 第 1 步：把四周的 `0` 以及与 `0` 连通的 `0` 都设置成 `#`
        def dfs(x, y):
            board[x][y] = '#'

            for offsetX, offsetY in offsets:
                newX, newY = x + offsetX, y + offsetY
                if inArea(newX, newY) and board[newX][newY] == 'O':
                    dfs(newX, newY)

        # 把第一列和最后一列为'O'的坐标进行 dfs
        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][cols - 1] == 'O':
                dfs(i, cols - 1)
        # 把第一行和最后一行为'O'的坐标进行 dfs
        for j in range(cols):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[rows - 1][j] == 'O':
                dfs(rows - 1, j)

        # 第 2 步：遍历一次棋盘，
        # 1. 剩下的 0 就是被 X 包围的 0，
        # 2. '#' 是原来不能被包围的 0，恢复成 0
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'

        print(board)


# 方法 2：BFS
# step1.把四周的 'O' 全部推入队列，通过广度优先遍历，把与 'O' 连通的地方全部编辑
# step2.恢复

# 方法 3：并查集
# 把四周的 O 都和一个虚拟结点合并起来；
# 在内部，只看两个方向，把 O 都合并起来；
# 最后再扫一次数组，不和「虚拟结点」连接的 O 都标记成 X。
# 并查集的写法容易受 floorfill 的影响，用并查集的时候，其实 只用每一行的右边和下面都看一下，只针对 O，能合并就合并一下。

if __name__ == '__main__':
    # board = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
    board = [["X", "O", "X"],
             ["O", "X", "O"],
             ["X", "O", "X"]]
    board2 = [["O", "X", "X", "O", "X"],
              ["X", "O", "O", "X", "O"],
              ["X", "O", "X", "O", "X"],
              ["O", "X", "O", "O", "O"],
              ["X", "X", "O", "X", "O"]]
    print(Solution().solve(board))
