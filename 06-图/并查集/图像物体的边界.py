"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/127647130

OJ用例
题解 - 图像物体的边界 - Hydro

题目描述
给定一个二维数组M行N列，二维数组里的数字代表图片的像素，为了简化问题，仅包含像素1和5两种像素，每种像素代表一个物体，2个物体相邻的格子为边界，求像素1代表的物体的边界个数。

像素1代表的物体的边界指与像素5相邻的像素1的格子，边界相邻的属于同一个边界，相邻需要考虑8个方向（上，下，左，右，左上，左下，右上，右下）。

其他约束

地图规格约束为：

0<M<100 0<N<100

1）如下图，与像素5的格子相邻的像素1的格子（0,0）、（0,1）、（0,2）、（1,0）、（1,2）、（2,0）、（2,1）、（2,2）、（4,4）、（4,5）、（5,4）为边界，另（0,0）、（0,1）、（0,2）、（1,0）、（1,2）、（2,0）、（2,1）、（2,2）相邻，为1个边界，（4,4）、（4,5）、（5,4）相邻，为1个边界，所以下图边界个数为2。

image

2）如下图，与像素5的格子相邻的像素1的格子（0,0）、（0,1）、（0,2）、（1,0）、（1,2）、（2,0）、（2,1）、（2,2）、（3,3）、（3,4）、（3,5）、（4,3）、（4,5）、（5,3）、（5,4）、（5,5）为边界，另这些边界相邻，所以下图边界个数为1。



​注:（2,2）、（3,3）相邻。

输入描述
第一行，行数M，列数N

第二行开始，是M行N列的像素的二维数组，仅包含像素1和5

输出描述
像素1代表的物体的边界个数。

如果没有边界输出0（比如只存在像素1，或者只存在像素5）。

用例1
输入
6 6
1 1 1 1 1 1
1 5 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 5
输出
2

用例2
输入
6 6
1 1 1 1 1 1
1 5 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 5 1
1 1 1 1 1 1
输出
1
"""
"""
补充用例：
输入
1 8
1 5 1 1 5 5 1 1
输出
3

输入
8 1
1 
5
1
1
1 
5
5
1
输出：4
"""

# 获取输入
R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]
# print(grid)

# 1. 找像素1代表的物体的边界个数


class Ufs:
    def __init__(self, n):
        self.fa = list(range(n))
        self.cnt = n

    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        fa_x = self.find(x)
        fa_y = self.find(y)

        if fa_x != fa_y:
            self.fa[fa_y] = fa_x
            self.cnt -= 1


def main():
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
               (0, 1), (1, -1), (1, 0), (1, 1)]

    # 记录所有边界位置
    boundary = set()
    for i in range(R):
        for j in range(C):
            # 如果当前点是像素5,遍历像素5的相邻位置,如果该位置不越界，且为像素1，则是边界
            if grid[i][j] == 5:
                for ox, oy in offsets:
                    x = i + ox
                    y = j + oy
                    if not (0 <= x < R and 0 <= y < C):
                        continue
                    if grid[x][y] == 1:
                        boundary.add((x, y))

    print(boundary)

    # 2.利用并查集确认有哪些边界是相邻的
    boundary = list(boundary)
    n = len(boundary)

    ufs = Ufs(n)
    for i in range(n):
        x1, y1 = boundary[i]
        for j in range(i+1, n):
            x2, y2 = boundary[j]
            # todo 如果两个边界像素1的位置 横向、纵向距离均小于1，则相邻，可以进行合并
            if abs(x1-x2) <= 1 and abs(y1-y2) <= 1:
                ufs.union(i, j)
    return ufs.cnt


print(main())
