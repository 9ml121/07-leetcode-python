"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/134939367?spm=1001.2014.3001.5502

题目描述
假定街道是棋盘型的，每格距离相等，车辆通过每格街道需要时间均为 timePerRoad；

街道的街口（交叉点）有交通灯，灯的周期 T（=lights[row][col]）各不相同；

车辆可直行、左转和右转，其中直行和左转需要等相应 T 时间的交通灯才可通行，右转无需等待。

现给出 n * m 个街口的交通灯周期，以及起止街口的坐标，计算车辆经过两个街口的最短时间。

其中：

起点和终点的交通灯不计入时间，且可以在任意方向经过街口
不可超出 n * m 个街口，不可跳跃，但边线也是道路（即：lights[0][0] -> lights[0][1] 是有效路径）
入口函数定义：

/**
 * @param lights：n*m个街口每个交通灯的周期，值范围[0, 120]，n和m的范围为[1,9]
 * @param timePreRoad：相邻两个街口之间街道的通行时间，范围为[0,600]
 * @param rowStart：起点的行号
 * @param colStart：起点的列号
 * @param rowEnd：终点的行号
 * @param colEnd：终点的列号
 * @return lights[rowStart][colStart] 与 lights[rowEnd][colEnd] 两个街口之间的最短通行时间
 */
int calcTime(int[][] lights, int timePreRoad, int rowStart, int colStart, int rowEnd, int colEnd)
输入描述
第一行输入 n 和 m，以空格分隔

之后 n 行输入 lights矩阵，矩阵每行m个整数，以空格分隔

之后一行输入 timePerRoad

之后一行输入 rowStart colStart，以空格分隔

最后一行输入 rowEnd colEnd，以空格分隔

输出描述
lights[rowStart][colStart] 与 lights[rowEnd][colEnd] 两个街口之间的最短通行时间

用例1
输入
3 3
1 2 3
4 5 6
7 8 9
60
0 0
2 2
输出
245
说明
行走路线为 (0,0) -> (0,1) -> (1,1) -> (1,2) -> (2,2) 走了4格路，2个右转，1个左转，共耗时 60+0+60+5+60+0+60=245
"""


import sys

# 困难题（需要再研究一下）
# 根据三点坐标，确定拐弯方向
def getDirection(preX, preY, curX, curY, nextX, nextY):
    """
    :param preX: 前一个点横坐标
    :param preY: 前一个点纵坐标
    :param curX: 当前点横坐标
    :param curY: 当前点纵坐标
    :param nextX: 下一个点横坐标
    :param nextY: 下一个点纵坐标
    :return: cur到next的拐弯方向， >0 表示向左拐， ==0 表示直行（含调头）， <0 表示向右拐
    """
    # 向量 pre->cur
    dx1 = curX - preX
    dy1 = curY - preY

    # 向量 cur->next
    dx2 = nextX - curX
    dy2 = nextY - curY

    #  两个向量的叉积 >0 表示向左拐， ==0 表示直行（含调头）， <0 表示向右拐
    return dx1 * dy2 - dx2 * dy1


class Solution:
    def calcTime(self, lights, timePerRoad, rowStart, colStart, rowEnd, colEnd):
        n = len(lights)
        m = len(lights[0])

        # 到达位置(i,j)的路径有四个来源方向]
        # dist[i][j][k] 表示从来源方向k到达位置(i,j)所需要的时间，初始化INT_MAX
        dist = [[[sys.maxsize] * 4 for _ in range(m)] for _ in range(n)]

        # 小顶堆，堆中元素是数组 [前一个位置行号，前一个位置列号，当前位置行号，当前位置列号，到达当前位置需要的时间]
        # 到达当前位置的时间越小，优先级越高
        pq = []

        # 四个来源方向到达出发点位置 (rowStart, colStart) 所需时间均为 0
        for k in range(4):
            dist[rowStart][colStart][k] = 0
            # 出发点位置没有前一个位置，因此前一个位置设为(-1,-1)
            pq.append((-1, -1, rowStart, colStart, 0))

        offsets = ((-1, 0), (1, 0), (0, -1), (0, 1))

        # 每次取出最短路
        while len(pq) > 0:
            pq.sort(key=lambda x: -x[4])  # 优化
            preX, preY, curX, curY, cost = pq.pop()

            # 向四个方向探索
            for k in range(4):
                # 新位置
                newX = curX + offsets[k][0]
                newY = curY + offsets[k][1]

                # 新位置越界，则不可进入
                if newX < 0 or newX >= n or newY < 0 or newY >= m:
                    continue

                # 本题不允许掉头，因此新位置处于掉头位置的话，不可进入
                if newX == preX and newY == preY:
                    continue

                # 每走一步都要花费 timePerRoad 单位时间
                newCost = cost + timePerRoad

                # 出发的第一步，或者右拐，不需要等待红绿灯，其他情况需要等待红绿灯 lights[curX][curY] 单位时间
                if preX != -1 and preY != -1 and getDirection(preX, preY, curX, curY, newX, newY) >= 0:
                    newCost += lights[curX][curY]

                # 如果以来源方向k到达位置（newX, newY）花费的时间 newCost 并非更优，则终止对应路径探索
                if newCost >= dist[newX][newY][k]:
                    continue

                # 否则更新为更优时间
                dist[newX][newY][k] = newCost
                # 并继续探索该路径
                pq.append((curX, curY, newX, newY, newCost))

        # 最终取(rowEnd, colEnd)终点位置的四个来源方向路径中最短时间的作为题解
        return min(dist[rowEnd][colEnd])


# 实际考试时，本题为核心代码模式，即无需我们解析输入输出，因此只需要写出上面代码即可

n, m = map(int, input().split())
lights = [list(map(int, input().split())) for _ in range(n)]
timePerRoad = int(input())
rowStart, colStart = map(int, input().split())
rowEnd, colEnd = map(int, input().split())

print(Solution().calcTime(lights, timePerRoad, rowStart, colStart, rowEnd, colEnd))
