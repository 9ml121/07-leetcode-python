"""
给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

 

示例 1：
输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
输出：[[0,0,0],[0,1,0],[0,0,0]]

示例 2：
输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
输出：[[0,0,0],[0,1,0],[1,2,1]]
 

提示：
m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
mat 中至少有一个 0 

"""


import collections
from typing import List

# todo 多源最短路径问题：bfs
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # 输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
        m, n = len(mat), len(mat[0])
        ans = [[0] * n for _ in range(m)]

        # 1. 先将所有0的坐标加入dq, 后续是将遍历到的1坐标分批加入
        dq = collections.deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dq.append((i, j))

        # 2. bfs遍历，更新ans
        offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        # vis数组记录所有1的坐标位置有没有被dq遍历过（也可以用集合）
        vis = [[False] * n for _ in range(m)]
        level = 0  # bfs当前层数

        while dq:
            new_dq = []
            for x, y in dq:
                # 更新ans
                ans[x][y] = level

                for ox, oy in offsets:
                    nx = x + ox
                    ny = y + oy

                    # 越界，值为0, 值为1但被访问过：跳过
                    if not (0 <= nx < m and 0 <= ny < n) or mat[nx][ny] == 0 or vis[nx][ny]:
                        continue

                    # 没被访问过的1 mat[nx][ny]=1
                    new_dq.append((nx, ny))
                    vis[nx][ny] = True
            dq = new_dq
            level += 1

        return ans
