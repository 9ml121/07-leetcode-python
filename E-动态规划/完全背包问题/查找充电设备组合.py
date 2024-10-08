"""
题目描述
某个充电站，可提供 n 个充电设备，每个充电设备均有对应的输出功率。
任意个充电设备组合的输出功率总和，均构成功率集合 P 的 1 个元素。
功率集合 P 的最优元素，表示最接近充电站最大输出功率 p_max 的元素。


输入描述
输入为三行：
第一行为充电设备个数 n。
第二行为每个充电设备的输出功率。
第三行为充电站最大输出功率 p_max。

输出描述
功率集合 P 的最优元素


备注
充电设备个数 n>0
最优元素必须小于或等于充电站最大输出功率 p_max。
充电站内的某一台设备都有自身的功率，功率不一定相同.
如果不存在这样的组，比如当所有设备的功率均大于maxP时，不存在这样的组，返回0
找到任意一种组合指的是不限定组内的设备数量，即一组内的设备数量为1到n都可以

示例一
输入
4
50 20 20 60
90

输出
90

说明
当充电设备输出功率 50、20、20 组合时，其输出功率总和为 90，最接近充电站最大充电输出功率，因此最优元素为 90。
"""
n = 5
P = [1, 2, 5, 5, 7]
maxP = 15
res = 0
# 最优元素必须小于或等于充电站最大输出功率 p_max。
# 问题其实就是找一个集合子元素之和最接近目标值

# 当所有设备的功率均大于maxP时，不存在这样的组，返回0
# if min(P) > maxP:
#     res = 0

# 动态规划
P.sort()
dp = [[0] * (maxP + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(0, maxP + 1):
        if j < P[i - 1]:
            # 如果超过了最大功率，就只能取上一个元素的值
            dp[i][j] = dp[i - 1][j]
        else:
            # 如果没有超过最大功率，有2中选择：1是用这个元素，再加上maxp减去这个元素之前的值；2是不用这个元素，取上一个元素的值
            dp[i][j] = max(dp[i - 1][j], P[i - 1] + dp[i-1][j - P[i - 1]])
# 最后结果
res = dp[n][maxP]
# res = max(dp[n])

# print(len(dp), len(dp[0]))
# print(dp)
print(res)
