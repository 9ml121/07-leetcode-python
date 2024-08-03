"""
一个魔法师有许多不同的咒语。

给你一个数组 power ，其中每个元素表示一个咒语的伤害值，可能会有多个咒语有相同的伤害值。

已知魔法师使用伤害值为 power[i] 的咒语时，他们就 不能 使用伤害为 power[i] - 2 ，power[i] - 1 ，power[i] + 1 或者 power[i] + 2 的咒语。

每个咒语最多只能被使用 一次 。

请你返回这个魔法师可以达到的伤害值之和的 最大值 。

 

示例 1：

输入：power = [1,1,3,4]

输出：6

解释：

可以使用咒语 0，1，3，伤害值分别为 1，1，4，总伤害值为 6 。

示例 2：

输入：power = [7,1,6,6]

输出：13

解释：

可以使用咒语 1，2，3，伤害值分别为 1，6，6，总伤害值为 13 。

 

提示：

1 <= power.length <= 105
1 <= power[i] <= 109
"""


from functools import cache
from typing import Counter, List

# 本题和 740. 删除并获得点数 几乎一样，都是在值域上的 198. 打家劫舍。

# 动态规划解法：
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        a = sorted(cnt.keys())
        f = [0] * (len(a) + 1)
        j = 0
        for i, x in enumerate(a):
            while a[j] < x - 2:
                j += 1
            f[i + 1] = max(f[i], f[j] + x * cnt[x])
        return f[-1]


# 递归解法
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        a = sorted(cnt.keys())

        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            x = a[i]
            j = i
            while j and a[j - 1] >= x - 2:
                j -= 1
            return max(dfs(i - 1), dfs(j - 1) + x * cnt[x])
        return dfs(len(a) - 1)
