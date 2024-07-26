"""
王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件，附件是从属于某个主件的，下表就是一些主件与附件的例子：
关键信息：
1。如果要买归类为附件的物品，必须先买该附件所属的主件，且每件物品只能购买一次。
2。每个主件可以有 0 个、 1 个或 2 个附件。

王强查到了每件物品的价格（都是 10 元的整数倍），而他只有 n 元的预算。
除此之外，他给每件物品规定了一个重要度，用整数 1 ~ 5 表示。
他希望在花费不超过 n 元的前提下，使自己的满意度达到最大。
请你帮助王强计算可获得的最大的满意度。

输入描述：
输入的第 1 行，为两个正整数N，m，用一个空格隔开：
（其中 n （ n<32000 ）表示总钱数， m （m <60 ）为可购买的物品的个数。）
从第 2 行到第 m+1 行，第 j 行给出了编号为 j-1 的物品的基本数据，每行有 3 个非负整数 v p q
（其中 v 表示该物品的价格（ v<10000 ）， p 表示该物品的重要度（ 1 ~ 5 ）， q 表示该物品是主件还是附件。如果 q=0 ，表示该物品为主件，如果 q>0 ，表示该物品为附件， q 是所属主件的编号）

输出描述：
 输出一个正整数，为张强可以获得的最大的满意度。

示例1
输入：
1000 5
800 2 0
400 5 1
300 5 1
400 3 0
500 2 0

输出：
2200

示例2
输入：
50 5
20 3 5
20 3 5
10 3 0
10 2 0
10 1 0

输出：
130
复制
说明：
由第1行可知总钱数N为50以及希望购买的物品个数m为5；
第2和第3行的q为5，说明它们都是编号为5的物品的附件；
第4~6行的q都为0，说明它们都是主件，它们的编号依次为3~5；
所以物品的价格与重要度乘积的总和的最大值为10*1+20*3+20*3=130
"""

# 总钱数N, 物品总数m
N, m = map(int, input().split())
# print(n)

# 主件
main = {}
# 附件
attach = {}
# 商品价格列表
v_arr = set()
for i in range(1, m + 1):
    # v 表示该物品的价格（ v<10000 ）， p 表示该物品的重要度（ 1 ~ 5 ）， q 表示该物品是主件还是附件
    v, p, q = map(int, input().split())
    v_arr.add(v)
    # 如果 q=0 ，表示该物品为主件，如果 q>0 ，表示该物品为附件， q 是所属主件的编号
    if q == 0:
        main[i] = (v, v * p)
    else:
        if q not in attach:
            attach[q] = [(v, v * p)]
        else:
            attach[q].append((v, v * p))
# print(main)
# {1: (800, 1600), 4: (400, 1200), 5: (500, 1000)}
# {3: (10, 30), 4: (10, 20), 5: (10, 10)}
# print(attach)
# {1: [(400, 2000), (300, 1500)]}
# {5: [(20, 60), (20, 60)]}
main_lst = list(main.keys())
m = len(main_lst)

# j开始索引可以从最小单价商品开始
start = min(v_arr)
# 默认价值为0, 单价都为10的倍数
dp = [[0] * (N+1) for _ in range(0, m+1)]
# for i in range(0, m + 1):
#     dp.append([0 for j in range(start, n + 1, 10)])

for i in range(1, m + 1):
    # i 对应的主商品编号为pid
    pid = main_lst[i - 1]
    v = main[pid][0]  # 商品价格
    vp = main[pid][1]  # 该商品价值
    for j in range(start, N + 1, 10):  # [10, 20, 30, 40, 50]
        # 如果商品价格比余额大，最大价值为上面的值
        if v > j:
            dp[i][j] = dp[i - 1][j]
        # 如果商品价格比N小，可以选择：1：不买主件； 2：只买主件。 3：买主件 + 附件1。 4：买主件 + 附件2。 5：买主件+ 附件1 + 附件2
        else:  # v <= j
            # 1.不买主件： dp[i-1][j]
            value1 = dp[i - 1][j]
            # 2.只买主件：# 动态转移方程式为： 购买该商品价值 + 剩下的钱可以购买上面物品的最大价值
            j1 = j - v  # 剩余金额
            value2 = vp + dp[i - 1][j1]

            # 3.买主件 + 附件1 + 附件2
            value3 = 0
            value4 = 0
            if pid in attach.keys():  # {5: [(20, 60), (20, 60)]}
                attach_lst = attach[pid]  # 附件列表
                for elem in attach_lst:  # 有1个或者2个附件
                    v1 = elem[0]  # 附件价格和价值
                    vp1 = elem[1]
                    # 3.1 购买附件1或者附件2，取价值最大的那个
                    if v1 <= j1:  # 只有附件价格不比剩余金额大，才有可能购买
                        value3 = max(vp + vp1 + dp[i - 1][j1 - v1], value3)
                # 3.2 同时购买附件1 + 附件2
                if len(attach_lst) == 2:
                    v20 = attach_lst[0][0]
                    v21 = attach_lst[1][0]
                    vp20 = attach_lst[0][1]
                    vp21 = attach_lst[1][1]
                    if v20 + v21 <= j1:
                        value4 = vp + vp20 + vp21 + dp[i - 1][j1 - v20 - v21]

            dp[i][j] = max(value1, value2, value3, value4)
# 最终可以获得的最大的满意度。
print(dp[m][N])
