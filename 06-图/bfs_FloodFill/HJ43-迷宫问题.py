"""
描述
定义一个二维数组 n*M ，如 5 × 5 数组下所示：

int maze[5][5] = {
0, 1, 0, 0, 0,
0, 1, 1, 1, 0,
0, 0, 0, 0, 0,
0, 1, 1, 1, 0,
0, 0, 0, 1, 0,
};

它表示一个迷宫，其中的1表示墙壁，0表示可以走的路，只能横着走或竖着走，不能斜着走，要求编程序找出从左上角到右下角的路线。
入口点为[0,0],既第一格是可以走的路。


数据范围： 2≤n,m≤10  ， 输入的内容只包含 0≤value≤1

输入描述：
输入两个整数，分别表示二维数组的行数，列数。再输入相应的数组，其中的1表示墙壁，0表示可以走的路。
数据保证有唯一解,不考虑有多解的情况，即迷宫只有一条通道。

输出描述：
左上角到右下角的最短路径，格式如样例所示。

示例1
输入：
5 5
0 1 0 0 0
0 1 1 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0

输出：
(0,0)
(1,0)
(2,0)
(2,1)
(2,2)
(2,3)
(2,4)
(3,4)
(4,4)

示例2
输入：
5 5
0 1 0 0 0
0 1 0 1 0
0 0 0 0 1
0 1 1 1 0
0 0 0 0 0

输出：
(0,0)
(1,0)
(2,0)
(3,0)
(4,0)
(4,1)
(4,2)
(4,3)
(4,4)

说明：
注意：不能斜着走！！
"""

# 本题有两种解题思路：
# 广度优先搜索
# 深度优先搜索

# 方法1：dfs
def getResult(maze: list, route: list):
    visited = [[False] * col for _ in range(row)]
    # 第一步已走过
    visited[0][0] = True
    # 四种可能走的方向
    offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(i, j):
        # 递归终止条件: 到达终点
        if i == row - 1 and j == col - 1:
            for pos in route:
                print(f"({pos[0]},{pos[1]})")
            return

        for a, b in offsets:
            # x,y 表示当前点(i,j)的邻接点
            x = i + a
            y = j + b
            if 0 <= x < row and 0 <= y < col and maze[x][y] == 0 and not visited[x][y]:
                route.append((x, y))
                visited[x][y] = True
                dfs(x, y)
                # 如果dfs() 深入到最后仍未进入终止条件得以return, 则意味着此路不通, 下面则在回溯途中依次消除该路节点
                route.pop()

    # 调用函数
    dfs(0, 0)


# 方法2:bfs(记录路径)
# 输入获取
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(n)]


class Pos:
    def __init__(self, x, y, pre):
        self.x = x  # 当前点的横坐标
        self.y = y  # 当前点的纵坐标
        self.pre = pre  # 当前点的上一个点（此属性用于形成路径链）


def printPath(cur):
    # 这里采用递归打印，保证打印顺序是起点到终点
    if cur.pre:
        # 递归的作用是优先打印pre点，pre点打印完，回溯打印cur点
        printPath(cur.pre)

    print(f"({cur.x},{cur.y})")


# 算法入口
def getResult():
    # 广搜队列
    queue = []

    # 将（0，0）位置标记为“走过状态”，即将元素值设为2
    matrix[0][0] = 2
    # 将走过的点加入队列
    queue.append(Pos(0, 0, None))

    # 上下左右偏移量
    offsets = ((-1, 0), (1, 0), (0, -1), (0, 1))

    # 广搜
    while len(queue) > 0:
        # 当前点
        cur = queue.pop(0)

        # 遍历当前点的上、下、左、右方向的新点
        for offsetX, offsetY in offsets:
            # 新点的坐标
            newX = cur.x + offsetX
            newY = cur.y + offsetY

            # 如果新点不越界，且未被访问过，且不是墙， 则新点可以访问
            if n > newX >= 0 and m > newY >= 0 and matrix[newX][newY] == 0:
                # 将新点状态设为走过
                matrix[newX][newY] = 2
                # 将新点和上一个点关联，形成路径链
                nxt = Pos(newX, newY, cur)
                queue.append(nxt)

                # 如果新点就是终点，那么则说明找到了起点到终点的路径
                if newX == n - 1 and newY == m - 1:
                    # 打印路径
                    printPath(nxt)
                    # 结束查找
                    return


# 算法调用
getResult()
if __name__ == '__main__':
    # 1.获取输入
    # row, col = map(int, input().split())
    # maze = []
    # for i in range(row):
    #     maze.append(list(map(int, input().split())))
    route = [(0, 0)]
    row, col = 5, 5
    maze = \
        [[0, 1, 0, 0, 0],
         [0, 1, 0, 1, 0],
         [0, 0, 0, 0, 1],
         [0, 1, 1, 1, 0],
         [0, 0, 0, 0, 0]]
    getResult(maze, route)
