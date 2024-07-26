"""
给你一个整数 n 表示数轴上的房屋数量，编号从 0 到 n - 1 。

另给你一个二维整数数组 offers ，其中 offers[i] = [starti, endi, goldi] 表示第 i 个买家想要以 goldi 枚金币的价格购买从 starti 到 endi 的所有房屋。

作为一名销售，你需要有策略地选择并销售房屋使自己的收入最大化。

返回你可以赚取的金币的最大数目。

注意 同一所房屋不能卖给不同的买家，并且允许保留一些房屋不进行出售。

 

示例 1：

输入：n = 5, offers = [[0,0,1],[0,2,2],[1,3,2]]
输出：3
解释：
有 5 所房屋，编号从 0 到 4 ，共有 3 个购买要约。
将位于 [0,0] 范围内的房屋以 1 金币的价格出售给第 1 位买家，并将位于 [1,3] 范围内的房屋以 2 金币的价格出售给第 3 位买家。
可以证明我们最多只能获得 3 枚金币。
示例 2：

输入：n = 5, offers = [[0,0,1],[0,2,10],[1,3,2]]
输出：10
解释：有 5 所房屋，编号从 0 到 4 ，共有 3 个购买要约。
将位于 [0,2] 范围内的房屋以 10 金币的价格出售给第 2 位买家。
可以证明我们最多只能获得 10 枚金币。
 

提示：

1 <= n <= 105
1 <= offers.length <= 105
offers[i].length == 3
0 <= starti <= endi <= n - 1
1 <= goldi <= 103
"""


from typing import List

# todo §6.4 不相交区间
# 类似 2008. 出租车的最大盈利.py
class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        # 为了方便遍历，可以先把所有 end 相同的数据用哈希表归类。
        groups = [[] for _ in range(n)]
        for start, end, gold in offers:
            groups[end].append((start, gold))

        # f[i]表示截止到第 i号房屋可以获取的最大金币，考虑编号为 i 的房屋卖或不卖：
        f = [0] * (n+1)
        for end, g in enumerate(groups):
            f[end + 1] = f[end]  # 不卖
            for start, gold in g:
                f[end + 1] = max(f[end + 1], f[start] + gold) # 卖

        # print(f)
        return f[n]
