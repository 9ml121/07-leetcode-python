"""
有一个书店老板，他的书店开了 n 分钟。每分钟都有一些顾客进入这家商店。给定一个长度为 n 的整数数组 customers ，其中 customers[i] 是在第 i 分钟开始时进入商店的顾客数量，所有这些顾客在第 i 分钟结束后离开。

在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。

当书店老板生气时，那一分钟的顾客就会不满意，若老板不生气则顾客是满意的。

书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 minutes 分钟不生气，但却只能使用一次。

请你返回 这一天营业下来，最多有多少客户能够感到满意 。
 

示例 1：

输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
输出：16
解释：书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
示例 2：

输入：customers = [1], grumpy = [0], minutes = 1
输出：1
 

提示：

n == customers.length == grumpy.length
1 <= minutes <= n <= 2 * 104
0 <= customers[i] <= 1000
grumpy[i] == 0 or 1
"""


# todo 简单的固定长度滑动窗口
# 原始满意度 + 窗口增量满意度
class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        # 返回这一天营业下来，最多有多少客户能够感到满意
        # minutes代表可以让自己持续minutes分钟不生气
        # 找minutes长度的滑窗，其中不满意的客户总数最多
        n = len(customers)
        # 0代表不生气，1代表生气, orig_cnt代表不生气的时候总的客户满意度
        orig_cnt = sum([customers[i] for i in range(n) if grumpy[i] == 0])
        
        # win_inc代表长度为minutes的滑窗内生气的客户总数
        # 第一个滑窗
        win_inc = sum([customers[i] for i in range(minutes) if grumpy[i] == 1])
        max_inc = win_inc   # 所有滑窗生气客户数的最大数

        # 后续滑窗
        for r in range(minutes, n):
            # 入
            if grumpy[r] == 1:
                win_inc += customers[r]

            # 出
            if grumpy[r-minutes] == 1:
                win_inc -= customers[r-minutes]

            # 更新max_cnt
            max_inc = max(max_inc, win_inc)

        # 计算总满意客户
        return orig_cnt + max_inc

