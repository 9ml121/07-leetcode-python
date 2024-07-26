"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/134454058?csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22134454058%22%2C%22source%22%3A%22qfc_128220%22%7D

OJ用例
https://hydro.ac/d/HWOD2023/p/OD353/solution

题目描述
机器人搬砖，一共有 N 堆砖存放在 N 个不同的仓库中，第 i 堆砖中有 bricks[i] 块砖头，要求在 8 小时内搬完。

机器人每小时能搬砖的数量取决于有多少能量格，机器人一个小时中只能在一个仓库中搬砖，机器人的能量格只在这一个小时有效，为使得机器人损耗最小化，应尽量减小每次补充的能量格数。

为了保障在 8 小时内能完成搬砖任务，请计算每小时给机器人充能的最小能量格数。

无需考虑机器人补充能力格的耗时；
无需考虑机器人搬砖的耗时；
机器人每小时补充能量格只在这一个小时中有效；
输入描述
第一行为一行数字，空格分隔

输出描述
机器人每小时最少需要充的能量格，若无法完成任务，输出 -1

用例1
输入
30 12 25 8 19
输出
15
用例2
输入
10 12 25 8 19 8 6 4 17 19 20 30
输出
-1
说明
砖的堆数为12堆存放在12个仓库中，机器人一个小时内只能在一个仓库搬砖，不可能完成任务。
"""


import math

# 获取输入
bricks = list(map(int, input().split()))
# print(bricks)

# 为了保障在 8 小时内能完成搬砖任务，请计算每小时给机器人充能的最小能量格数。


def check(mid):
    cost = 0
    for b in bricks:
        cost += math.ceil(b/mid)
    return cost <= 8


def main():
    n = len(bricks)
    # 机器人一个小时中只能在一个仓库中搬砖
    if n > 8:
        return -1

    # 最大能量格
    hi = max(bricks)
    lo = 1
    ans = hi
    while lo <= hi:
        mid = (lo+hi) >> 1
        # 计算能量格为mid时，可不可以在8小时内完成
        if check(mid):
            ans = mid
            hi = mid-1
        else:
            lo = mid+1

    return ans


print(main())
