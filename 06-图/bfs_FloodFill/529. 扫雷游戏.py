"""
让我们一起来玩扫雷游戏！

给你一个大小为 m x n 二维字符矩阵 board ，表示扫雷游戏的盘面，其中：
'M' 代表一个 未挖出的 地雷，
'E' 代表一个 未挖出的 空方块，
'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的 已挖出的 空白方块，
数字（'1' 到 '8'）表示有多少地雷与这块 已挖出的 方块相邻，
'X' 则表示一个 已挖出的 地雷。

给你一个整数数组 click ，其中 click = [clickr, clickc] 表示在所有 未挖出的 方块（'M' 或者 'E'）中的下一个点击位置
（clickr 是行下标，clickc 是列下标）。

根据以下规则，返回相应位置被点击后对应的盘面：
如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X' 。
如果一个 没有相邻地雷 的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的 未挖出 方块都应该被递归地揭露。
如果一个 至少与一个地雷相邻 的空方块（'E'）被挖出，修改它为数字（'1' 到 '8' ），表示相邻地雷的数量。
如果在此次点击中，若无更多方块可被揭露，则返回盘面。


示例 1：
输入：board = [["E","E","E","E","E"],
              ["E","E","M","E","E"],
              ["E","E","E","E","E"],
              ["E","E","E","E","E"]], click = [3,0]
输出：[["B","1","E","1","B"],
      ["B","1","M","1","B"],
      ["B","1","1","1","B"],
      ["B","B","B","B","B"]]

示例 2：
输入：board = [["B","1","E","1","B"],
              ["B","1","M","1","B"],
              ["B","1","1","1","B"],
              ["B","B","B","B","B"]], click = [1,2]
输出：[["B","1","E","1","B"],
      ["B","1","X","1","B"],
      ["B","1","1","1","B"],
      ["B","B","B","B","B"]]


提示：
m == board.length
n == board[i].length
1 <= m, n <= 50
board[i][j] 为 'M'、'E'、'B' 或数字 '1' 到 '8' 中的一个
click.length == 2
0 <= clickr < m
0 <= clickc < n
board[clickr][clickc] 为 'M' 或 'E'
"""
import collections
from typing import List


# bfs思路: 8个方向
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # 1.如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X' 。
        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        rows, cols = len(board), len(board[0])
        # 枚举8个方向
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        visited = [[False] * cols for _ in range(rows)]

        def inArea(x, y):
            return 0 <= x < rows and 0 <= y < cols

        if board[i][j] == 'E':
            dq = collections.deque([(i, j)])
            visited[i][j] = True

            while dq:
                x, y = dq.popleft()
                list_E = []  # 技巧：提前统计当前坐标相邻，还没有挖出的空方块'E'

                # 2.统计当前坐标8个方向有几个地雷
                cnt_M = 0
                for offsetX, offsetY in offsets:
                    newX, newY = x + offsetX, y + offsetY

                    if inArea(newX, newY):
                        if board[newX][newY] == 'M':
                            cnt_M += 1
                        if board[newX][newY] == 'E' and not visited[newX][newY]:
                            list_E.append((newX, newY))

                # 3.如果当前坐标8个方向至少有1个地雷，修改当前坐标值为数字（'1' 到 '8' ），
                # 8个方向的坐标不用再继续遍历
                if cnt_M > 0:
                    board[x][y] = str(cnt_M)
                # 4.如果一个 没有相邻地雷 的空方块（'E'）被挖出，修改它为（'B'），
                # 并且所有和其相邻的 未挖出 方块都应该被递归地揭露
                else:
                    board[x][y] = 'B'
                    for pos in list_E:
                        # 关键：加入dq的坐标，要马上标记为true,避免重复访问
                        visited[pos[0]][pos[1]] = True
                        dq.append(pos)

        return board


# dfs思路
class Solution2:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click
        # 1.如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X' 。
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        else:
            # board[x][y] == 'E'
            rows, cols = len(board), len(board[0])
            offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

            def inArea(x, y):
                return 0 <= x < rows and 0 <= y < cols

            def dfs(x, y):
                cnt_M = 0
                # 2.统计8个方向有几个地雷
                for ox, oy in offsets:
                    newX, newY = x + ox, y + oy
                    if inArea(newX, newY) and board[newX][newY] == 'M':
                        cnt_M += 1
                # 2.1 如果当前坐标8个方向至少有1个地雷，修改当前坐标值为地雷数字（'1' 到 '8' ）
                # 周边8个方向的坐标不再递归遍历
                if cnt_M > 0:
                    board[x][y] = str(cnt_M)
                # 2.2 如果一个 没有相邻地雷 的空方块（'E'）被挖出，修改它为（'B'），
                # 并且所有和其相邻的 未挖出 方块都应该被递归地揭露。
                else:
                    # 注意：这里要先修改愿坐标为'B', 再dfs遍历8个方向中为E的坐标
                    board[x][y] = 'B'
                    for ox, oy in offsets:
                        newX, newY = x + ox, y + oy
                        if inArea(newX, newY) and board[newX][newY] == 'E':
                            dfs(newX, newY)

            dfs(x, y)
            return board


if __name__ == '__main__':
    board = [["E", "E", "E", "E", "E"],
             ["E", "E", "M", "E", "E"],
             ["E", "E", "E", "E", "E"],
             ["E", "E", "E", "E", "E"]]
    click = [3, 0]
    print(Solution().updateBoard(board, click))
    print(Solution2().updateBoard(board, click))

    # [["B", "1", "E", "1", "B"],
    #  ["B", "1", "M", "1", "B"],
    #  ["B", "1", "1", "1", "B"],
    #  ["B", "B", "B", "B", "B"]]
