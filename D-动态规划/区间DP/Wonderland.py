"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/135328637?spm=1001.2014.3001.5502

OJ用例
题解 - Wonderland - Hydro

题目描述
Wonderland是小王居住地一家很受欢迎的游乐园。Wonderland目前有4种售票方式，分别为一日票（1天）、三日票（3天）、周票（7天）和月票（30天）。

每种售票方式的价格由一个数组给出，每种票据在票面时限内可以无限制地进行游玩。例如：

小王在第10日买了一张三日票，小王可以在第10日、第11日和第12日进行无限制地游玩。

小王计划在接下来一年多次游玩该游乐园。小王计划地游玩日期将由一个数组给出。

现在，请您根据给出地售票价格数组和小王计划游玩日期数组，返回游玩计划所需要地最低消费。

输入描述
输入为2个数组：

售票价格数组为costs，costs.length = 4，默认顺序为一日票、三日票、周票和月票。
小王计划游玩日期数组为days，1 ≤ days.length ≤ 365，1 ≤ days[i] ≤ 365，默认顺序为升序。
输出描述
完成游玩计划的最低消费。

用例1
输入
5 14 30 100
1 3 5 20 21 200 202 230
输出
40
说明
根据售票价格数组和游玩日期数组给出的信息，发现每次去玩的时候买一张一日票是最省钱的，所以小王会卖8张一日票，每张5元，最低花费是40元。
"""

# todo 考察动态规划
# 输入
# 售票价格
costs = list(map(int, input().split()))
# 计划游玩日期(已升序排列)
days = list(map(int, input().split()))

# 输入：游玩计划的最低消费
# dp[i]代表在第i天的最低消费
max_day = days[-1]
dp = [0] * (max_day + 1)
idx = 0  # 代表days的索引
for i in range(days[0], max_day + 1):
    # 如果是计划游玩日
    if i == days[idx]:
        idx += 1
        # 1日票
        cost1 = costs[0] + dp[i-1]
        # 3日票
        cost3 = costs[1] + (dp[i-3] if i >= 3 else 0)
        # 7日票
        cost7 = costs[2] + (dp[i-7] if i >= 7 else 0)
        # 30日票
        cost30 = costs[3] + (dp[i-30] if i >= 30 else 0)
        dp[i] = min(cost1, cost3, cost7, cost30)
    # 不是计划游玩日
    else:
        dp[i] = dp[i-1]

# print(dp)
print(dp[-1])
