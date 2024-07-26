"""
给你一个大小为 n x n 的整数矩阵 board ，方格按从 1 到 n2 编号，编号遵循 转行交替方式 ，
从左下角开始 （即，从 board[n - 1][0] 开始）每一行交替方向。

玩家从棋盘上的方格 1 （总是在最后一行、第一列）开始出发。

每一回合，玩家需要从当前方格 curr 开始出发，按下述要求前进：
选定目标方格 next ，目标方格的编号符合范围 [curr + 1, min(curr + 6, n2)] 。
该选择模拟了掷 六面处存在蛇或梯子，那么玩家会传送到蛇或梯子的目的地。否则，玩家传送到目标方格 next 。
当玩家到达编号 n2 的方格时，游戏结束。体骰子 的情景，无论棋盘大小如何，玩家最多只能有 6 个目的地。
传送玩家：如果目标方格 next

r 行 c 列的棋盘，按前述方法编号，棋盘格中可能存在 “蛇” 或 “梯子”；
如果 board[r][c] != -1，那个蛇或梯子的目的地将会是 board[r][c]。
编号为 1 和 n2 的方格上没有蛇或梯子。

注意，玩家在每回合的前进过程中最多只能爬过蛇或梯子一次：就算目的地是另一条蛇或梯子的起点，玩家也 不能 继续移动。

举个例子，假设棋盘是 [[-1,4],[-1,3]] ，第一次移动，玩家的目标方格是 2 。
那么这个玩家将会顺着梯子到达方格 3 ，但 不能 顺着方格 3 上的梯子前往方格 4 。
返回达到编号为 n2 的方格所需的最少移动次数，如果不可能，则返回 -1。


示例 1：
输入：board = [[-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1],
              [-1,35,-1,-1,13,-1],
              [-1,-1,-1,-1,-1,-1],
              [-1,15,-1,-1,-1,-1]]
输出：4
解释：
首先，从方格 1 [第 5 行，第 0 列] 开始。
先决定移动到方格 2 ，并必须爬过梯子移动到到方格 15 。
然后决定移动到方格 17 [第 3 行，第 4 列]，必须爬过蛇到方格 13 。
接着决定移动到方格 14 ，且必须通过梯子移动到方格 35 。
最后决定移动到方格 36 , 游戏结束。
可以证明需要至少 4 次移动才能到达最后一个方格，所以答案是 4 。

示例 2：
输入：board = [[-1,-1],[-1,3]]
输出：1


提示：
n == board.length == board[i].length
2 <= n <= 20
grid[i][j] 的值是 -1 或在范围 [1, n^2] 内
编号为 1 和 n^2 的方格上没有蛇或梯子
"""
import collections
from typing import List


# bfs算法:同类型题
# 773. 滑动谜题.py
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n

        # todo 1.根据数字判断该数字所在矩阵的坐标
        def get_position(num):
            row = (num - 1) // n  # 数字所在矩阵的行索引
            col = (num - 1) % n  # 数字所在的列索引
            if row % 2 == 1:
                col = n - 1 - col
            row = n - 1 - row
            return row, col

        # todo 2.bfs遍历每一次移动可以到达的数字坐标
        def bfs():
            queue = collections.deque([(1, 0)])  # (position, moves)
            visited = [False] * (target + 1)
            visited[1] = True

            while queue:
                position, moves = queue.popleft()

                for i in range(1, 7):
                    next_pos = position + i
                    if next_pos > target:
                        break

                    row, col = get_position(next_pos)
                    if board[row][col] != -1:  # 存在蛇或梯子
                        next_pos = board[row][col]

                    if next_pos == target:  # 到达终点
                        return moves + 1

                    if not visited[next_pos]:
                        visited[next_pos] = True
                        queue.append((next_pos, moves + 1))  # 扩展新状态

            return -1

        return bfs()


# bfs朴实解法
class Solution2:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        start = 1
        num_to_pos = [(0, 0) for _ in range(n ** 2 + 1)]

        for i in range(n - 1, -1, -1):
            if i % 2 == (n - 1) % 2:
                for j in range(n):
                    num_to_pos[start] = (i, j)
                    start += 1
            else:
                for j in range(n - 1, -1, -1):
                    num_to_pos[start] = (i, j)
                    start += 1
        # print(num_to_pos)

        dq = collections.deque([1])
        visited = [False] * (n ** 2 + 1)
        visited[1] = True

        step = 0
        while dq:
            sz = len(dq)
            step += 1
            for _ in range(sz):
                num = dq.popleft()
                # 判断跳6格是否能到终点
                if num + 6 >= n ** 2:
                    return step

                tmp = -1
                for next_num in range(num + 1, num + 7):
                    pos = num_to_pos[next_num]
                    jump_num = board[pos[0]][pos[1]]

                    if jump_num == n ** 2:
                        return step

                    # 走梯子或者蛇
                    if jump_num != -1 and not visited[jump_num]:
                        dq.append(jump_num)
                        visited[jump_num] = True

                    # 加入6步之内能到的最远点
                    if jump_num == -1 and not visited[next_num]:
                        tmp = next_num
                        visited[next_num] = True
                if tmp != -1:
                    dq.append(tmp)
        return -1
