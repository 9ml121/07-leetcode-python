"""
题目来源
https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together/

题目描述
给出一个二进制数组 data，你需要通过交换位置，将数组中 任何位置 上的 1 组合到一起，并返回所有可能中所需 最少的交换次数。

示例
输入	[1,0,1,0,1]
输出	1
解释	
有三种可能的方法可以把所有的 1 组合在一起：

[1,1,1,0,0]，交换 1 次；

[0,1,1,1,0]，交换 2 次；

[0,0,1,1,1]，交换 1 次。

所以最少的交换次数为 1。

输入	[0,0,0,1,0]
输出	0
解释	由于数组中只有一个 1，所以不需要交换。

输入	[1,0,1,0,1,0,0,1,1,0,1]
输出	3
解释	交换 3 次，一种可行的只用 3 次交换的解决方案是 [0,0,0,0,0,1,1,1,1,1,1]。

提示
1 <= data.length <= 10^5
0 <= data[i] <= 1
"""


import collections

# todo 固定长度滑窗
class Solution:
    def minSwaps(self, data: list[int]) -> int:
        # 题目要求将data所有1组合在一起，最少交换次数 
        # 问题可以转换为滑动窗口大小为data中1个总个数，计算所有窗口中0的最小个数
        n = len(data)
        cnts = collections.Counter(data)
        k = cnts[1]
        if k <= 1 or k ==n:
            return 0

        # todo [l..r]窗口为固定大小k, zeros用来记录窗口中0的个数,
        # ans就是所有窗口0最少的个数
        win_zeros = 0
        ans = n

        for r, x in enumerate(data):
            # 入
            if x == 0:
                win_zeros += 1

            if r >= k-1:
                # 更新ans
                ans = min(ans, win_zeros)
                # 出
                win_zeros -= data[r-k+1] == 0

        return ans




