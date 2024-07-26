"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/134383665

OJ用例
https://hydro.ac/d/HWOD2023/p/OD350/solution

题目描述
从前有个村庄，村民们喜欢在各种田地上插上小旗子，旗子上标识了各种不同的数字。

某天集体村民决定将覆盖相同数字的最小矩阵形的土地分配给村里做出巨大贡献的村民，请问此次分配土地，做出贡献的村民种最大会分配多大面积?

输入描述
第一行输入 m 和 n，

m 代表村子的土地的长
n 代表土地的宽
第二行开始输入地图上的具体标识

输出描述
此次分配土地，做出贡献的村民种最大会分配多大面积

备注
旗子上的数字为1~500，土地边长不超过500
未插旗子的土地用0标识
用例1
输入
3 3
1 0 1
0 0 0
0 1 0
输出
9
说明
土地上的旗子为1，其坐标分别为(0,0)，(2,1)以及(0,2)，为了覆盖所有旗子，矩阵需要覆盖的横坐标为0和2，纵坐标为0和2，所以面积为9，即（2-0+1）*（2-0+1）= 9

用例2
输入
3 3
1 0 2
0 0 0
0 3 4
输出
1
说明
由于不存在成对的小旗子，故而返回1，即一块土地的面积。
"""

import collections

# 获取输入
# 第一行输入 m 和 n，根据测试用例推测代表行和列
R, C = map(int, input().split())
# 第二行开始输入地图上的具体标识
grid = [list(map(int, input().split())) for _ in range(R)]

# 找覆盖相同数字的最小矩阵形的土地的最大面积


class Area:
    def __init__(self):
        # 分别代表分配土地的左右，上下边界坐标
        self.l = R
        self.r = -1
        self.u = C
        self.d = -1
        # 分配的土地面积，默认是1
        self.sz = 1

    def add(self, x, y):
        # 横坐标决定上下边界
        if x < self.u:
            self.u = x
        if x > self.d:
            self.d = x
        # 纵坐标决定左右边界
        if y < self.l:
            self.l = y
        if y > self.r:
            self.r = y

        # 每添加一个坐标，更新一次土地面积
        self.sz = (self.r - self.l + 1) * (self.d - self.u + 1)

    # def __gt__(self, other):
    #     return self.sz > other.sz


cnts = collections.defaultdict(Area)
for i in range(R):
    for j in range(C):
        num = grid[i][j]
        if num == 0:
            continue
        cnts[num].add(i, j)

# 注意max函数关键字参数key, 代表比较大小的方法
ans = max(cnts.values(), key=lambda x: x.sz)
print(ans.sz)
