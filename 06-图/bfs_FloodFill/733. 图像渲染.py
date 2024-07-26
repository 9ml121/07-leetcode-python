"""
有一幅以 m x n 的二维整数数组表示的图画 image ，其中 image[i][j] 表示该图画的像素值大小。
你也被给予三个整数 sr ,  sc 和 newColor 。你应该从像素 image[sr][sc] 开始对图像进行 上色填充 。

为了完成 上色工作 ，从初始像素开始，记录初始坐标的 上下左右四个方向上 像素值与初始坐标相同的相连像素点，
接着再记录这四个方向上符合条件的像素点与他们对应 四个方向上 像素值与初始坐标相同的相连像素点，……，
重复该过程。将所有有记录的像素点的颜色值改为 newColor 。

最后返回 经过上色渲染后的图像 。


示例 1:
输入: image = [[1,1,1],
              [1,1,0],
              [1,0,1]]，
              sr = 1, sc = 1, newColor = 2
输出: [[2,2,2],
      [2,2,0],
      [2,0,1]]
解析: 在图像的正中间，(坐标(sr,sc)=(1,1)),在路径上所有符合条件的像素点的颜色都被更改成2。
注意，右下角的像素没有更改为2，因为它不是在上下左右四个方向上与初始点相连的像素点。

示例 2:
输入: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
输出: [[2,2,2],[2,2,2]]


提示:
m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], newColor < 216
0 <= sr < m
0 <= sc < n
"""
import collections
from typing import List


# 注意：题目要求是直接修改输入数据的
# 方法 1：dfs, 直接修改输入数据，不需要布尔数组
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # 特判
        originColor = image[sr][sc]
        if originColor == color:
            return image

        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row, col = len(image), len(image[0])

        def inArea(x, y):
            return 0 <= x < row and 0 <= y < col

        def dfs(x, y):
            image[x][y] = color
            for offsetX, offsetY in offsets:
                newX = x + offsetX
                newY = y + offsetY
                if inArea(newX, newY) and image[newX][newY] == originColor:
                    dfs(newX, newY)

        dfs(sr, sc)
        return image


# 方法 2：BFS
class Solution2:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originColor = image[sr][sc]
        if originColor == color:
            return image

        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row, col = len(image), len(image[0])

        def inArea(x, y):
            return 0 <= x < row and 0 <= y < col

        dq = collections.deque([(sr, sc)])
        image[sr][sc] = color
        while dq:
            level_size = len(dq)
            for _ in range(level_size):
                x, y = dq.popleft()
                for offsetX, offsetY in offsets:
                    newX = x + offsetX
                    newY = y + offsetY
                    if inArea(newX, newY) and image[newX][newY] == originColor:
                        # 这里直接修改输入数据，就不需要 visited布尔数组
                        image[newX][newY] = color
                        dq.append((newX, newY))

        return image


# 方法 3：dfs, 不修改输入数据，使用 visited 布尔数组
class Solution3:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # 前面这个特殊的判断很重要
        originColor = image[sr][sc]
        if originColor == color:
            return image

        # 注意：复制输入二维数组,不能用 image.copy()
        res = [row[:] for row in image]
        res[sr][sc] = color

        row, col = len(image), len(image[0])
        visited = [[False] * col for _ in range(row)]
        visited[sr][sc] = True

        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(sr, sc):
            nonlocal row, col
            for offsetX, offsetY in offsets:
                newSr = sr + offsetX
                newSc = sc + offsetY
                if 0 <= newSr < row and 0 <= newSc < col \
                        and image[newSr][newSc] == image[sr][sc] \
                        and not visited[newSr][newSc]:
                    visited[newSr][newSc] = True
                    res[newSr][newSc] = color
                    dfs(newSr, newSc)

        dfs(sr, sc)
        return res

# 方法 4：并查集
# 略
