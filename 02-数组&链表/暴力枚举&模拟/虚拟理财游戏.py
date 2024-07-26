"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/134387280?csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22134387280%22%2C%22source%22%3A%22qfc_128220%22%7D

OJ用例
题解 - 虚拟理财游戏 - Hydro

题目描述
在一款虚拟游戏中生活，你必须进行投资以增强在虚拟游戏中的资产以免被淘汰出局。

现有一家Bank，它提供有若干理财产品 m 个，风险及投资回报不同，你有 N（元）进行投资，能接收的总风险值为X。

你要在可接受范围内选择最优的投资方式获得最大回报。

备注：

在虚拟游戏中，每项投资风险值相加为总风险值；
在虚拟游戏中，最多只能投资2个理财产品；
在虚拟游戏中，最小单位为整数，不能拆分为小数；
投资额*回报率=投资回报
输入描述
第一行：

产品数（取值范围[1,20]）
总投资额（整数，取值范围[1, 10000]）
可接受的总风险（整数，取值范围[1,200]）
第二行：产品投资回报率序列，输入为整数，取值范围[1,60]

第三行：产品风险值序列，输入为整数，取值范围[1, 100]

第四行：最大投资额度序列，输入为整数，取值范围[1, 10000]

输出描述
每个产品的投资额序列

用例1
输入
5 100 10
10 20 30 40 50
3 4 5 6 10
20 30 20 40 30
输出
0 30 0 40 0
说明
投资第二项30个单位，第四项40个单位，总的投资风险为两项相加为4+6=10
"""


# 输入
# 产品数m，总投资额n，可接受的总风险k
m, n, k = map(int, input().split())
# 产品投资回报率
rates = list(map(int, input().split()))
# 产品风险值
risks = list(map(int, input().split()))
# 最大投资额
limits = list(map(int, input().split()))


# 输出：每个产品的投资额序列，可以获得最大回报
ans = []  # 投资的产品id, 投资金额（最多2个）
max_p = 0  # 全局最大回报
min_risk = float('inf')  # 全局最大回报的最小风险

# 最多只能投资2个理财产品


class Invest:
    def __init__(self, idx, rate, risk, limit):
        self.idx = idx
        self.rate = rate
        self.risk = risk
        self.limit = limit

    def __repr__(self):
        return f'{self.idx}:(rate={self.rate}, risk={self.risk}, limit={self.limit})'


invests = [Invest(i, rates[i], risks[i], limits[i]) for i in range(m)]

invests.sort(key=lambda x: -x.risk)
# print(invests)


for i in range(m):
    a = invests[i]
    if a.risk > k:
        continue

    # 当前产品投资回报, n为总投资额
    a0 = min(n, a.limit)  # 当前产品投资金额
    profit = a0 * a.rate
    risk = a.risk
    cur_ans = [(a.idx, a0)]
    # 组合另外一个产品
    b0 = 0
    j = m-1
    while j > i:
        b = invests[j]
        # 2个产品总风险不超过k
        if a.risk + b.risk > k:
            break

        if b.rate > a.rate or (b.rate == a.rate and b.risk < a.risk):
            b0 = min(n, b.limit)
            a0 = min(n - b0, a.limit)
        else:
            a0 = min(n, a.limit)
            b0 = min(n - a0, b.limit)

        cur_p = b0 * b.rate + a0 * a.rate

        # 更新当前组合最大回报
        # 如果投资回报相同，取风险最小的组合
        if cur_p > profit or (cur_p == profit and a.risk + b.risk < risk):
            profit = cur_p
            risk = a.risk + b.risk
            cur_ans = [(a.idx, a0), (b.idx, b0)]

        j -= 1

    # 更新全局组合最大回报
    if profit > max_p or (profit == max_p and risk < min_risk):
        max_p = profit
        min_risk = risk
        ans = cur_ans

# print(ans)
# 输出最后需要展示的结果
res = [0] * m
for idx, p0 in ans:
    res[idx] = p0
print(' '.join(map(str, res)))
