"""
题目解析和算法源码
华为OD机试 - 欢乐的周末（Java & JS & Python & C & C++）_伏城之外的博客-CSDN博客

OJ用例
题解 - 欢乐的周末 - Hydro

题目描述
小华和小为是很要好的朋友，他们约定周末一起吃饭。

通过手机交流，他们在地图上选择了多个聚餐地点（由于自然地形等原因，部分聚餐地点不可达），求小华和小为都能到达的聚餐地点有多少个？

输入描述
第一行输入m和n，m代表地图的长度，n代表地图的宽度。

第二行开始具体输入地图信息，地图信息包含：

0 为通畅的道路

1 为障碍物（且仅1为障碍物）

2 为小华或者小为，地图中必定有且仅有2个 （非障碍物）

3 为被选中的聚餐地点（非障碍物）

输出描述
可以被两方都到达的聚餐地点数量，行末无空格。

用例1
输入
4 4
2 1 0 3
0 1 2 1
0 3 0 0
0 0 0 0
输出
2
说明
第一行输入地图的长宽为3和4。

第二行开始为具体的地图，其中：3代表小华和小明选择的聚餐地点；2代表小华或者小明（确保有2个）；0代表可以通行的位置；1代表不可以通行的位置。

此时两者能都能到达的聚餐位置有2处。

用例2
输入
4 4
2 1 2 3
0 1 0 0
0 1 0 0
0 1 0 0
输出
0
说明
第一行输入地图的长宽为4和4。

第二行开始为具体的地图，其中：3代表小华和小明选择的聚餐地点；2代表小华或者小明（确保有2个）；0代表可以通行的位置；1代表不可以通行的位置。

由于图中小华和小为之间有个阻隔，此时，没有两人都能到达的聚餐地址，故而返回0。
"""


# 获取输入
# 第一行输入m和n，m代表地图的长度(根据测试用例代表行数)，n代表地图的宽度(根据测试用例代表列数)
# R, C = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(R)]
# print(grid)

# 测试用例
R, C = 4, 4
grid = [[2, 1, 0, 3], [0, 1, 2, 1], [0, 3, 0, 0], [0, 0, 0, 0]]


# 方法1: dfs(总是有3个测试用例Runtime Error！！)
rest_cnt = 0  # 可以到达的餐厅个数
people_cnt = 0 # 是否可以到达另外一个人地点
offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def main2():
    # 3 为被选中的聚餐地点, 1 为障碍物,0 为通畅的道路,2 为小华或者小为
    global people_cnt, rest_cnt
    for i in range(R):
        for j in range(C):
            # todo grid中一旦找到一个人的位置,就dfs或者bfs遍历找另外一个人和可以到达的餐厅
            if grid[i][j] == 2:
                vis = [[False] * C for _ in range(R)]
                vis[i][j] = True
                dfs(i, j, vis)
                if people_cnt == 0:
                    return 0
                else:
                    return rest_cnt
    return 0

def dfs(x, y, vis):
    global people_cnt, rest_cnt
    for ox, oy in offsets:
        new_x = x+ox
        new_y = y+oy
        # 越界，遇到障碍点或者已经访问过的点，跳过
        if not (0 <= new_x < R and 0 <= new_y < C):
            continue
        # 1 为障碍物（且仅1为障碍物）
        if vis[new_x][new_y] or grid[new_x][new_y] == 1:
            continue
        # 3 为被选中的聚餐地点（非障碍物）
        if grid[new_x][new_y] == 3:
            rest_cnt += 1
        # 2 为小华或者小为，地图中必定有且仅有2个
        elif grid[new_x][new_y] == 2:
            people_cnt += 1
        vis[new_x][new_y] = True
        dfs(new_x, new_y, vis)


# print(main2())


# 方法2: 并查集（推荐！！）
# 1. 判断2个人在并查集中的父节点fa[hua]是否一样：
# 如果不一样，代表2人无法相遇，就不可能到达同一个餐厅
# 如果一样，再找出餐厅节点的父节点=fa[hua],可以同时到达的餐厅+1
class Ufs:
    def __init__(self, n) -> None:
        self.fa = list(range(n))

    def find(self,x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]
    
    def union(self, x, y):
        fa_x = self.find(x)
        fa_y = self.find(y)
        if fa_x != fa_y:
            self.fa[fa_y] = fa_x
    

def main():
    ufs = Ufs(R*C)  # 二维列表转换为一维
    offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    huawei = []
    restaurants = []
    for i in range(R):
        for j in range(C):
            num = grid[i][j]
            # 1 为障碍物（且仅1为障碍物）
            if num != 1:
                # todo 二维列表坐标转换为一维
                idx = i * C + j
                # 2代表小华或者小明（确保有2个）
                if num == 2:
                    huawei.append(idx)
                # 3代表小华和小明选择的聚餐地点
                elif num == 3:
                    restaurants.append(idx)
                
                # union(可以通行的位置0, 小华或者小明2,聚餐地点3)
                for ox, oy in offsets:
                    new_x = i+ox
                    new_y = j+oy
                    # 越界，遇到障碍点1跳过
                    if not (0 <= new_x < R and 0 <= new_y < C):
                        continue
                    
                    if grid[new_x][new_y] == 1:
                        continue  
                    
                    idx2 = new_x * C + new_y
                    if ufs.find(idx) != ufs.find(idx2):
                        ufs.union(idx, idx2)   

    # 判断小华和小为的父节点
    fa_hua = ufs.find(huawei[0])
    fa_wei = ufs.find(huawei[1])
    if fa_hua != fa_wei:
        return 0
    # 判断餐厅的父节点
    cnt = 0
    for rest in restaurants:
        fa_rest = ufs.find(rest)
        if fa_rest == fa_hua:
            cnt += 1
    return cnt

print(main())