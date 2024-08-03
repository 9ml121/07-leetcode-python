"""
给你两个正整数 x 和 y 。

一次操作中，你可以执行以下四种操作之一：

如果 x 是 11 的倍数，将 x 除以 11 。
如果 x 是 5 的倍数，将 x 除以 5 。
将 x 减 1 。
将 x 加 1 。
请你返回让 x 和 y 相等的 最少 操作次数。

示例 1：

输入：x = 26, y = 1
输出：3
解释：我们可以通过以下操作将 26 变为 1 ：
1. 将 x 减 1
2. 将 x 除以 5
3. 将 x 除以 5
将 26 变为 1 最少需要 3 次操作。
示例 2：

输入：x = 54, y = 2
输出：4
解释：我们可以通过以下操作将 54 变为 2 ：
1. 将 x 加 1
2. 将 x 除以 11
3. 将 x 除以 5
4. 将 x 加 1
将 54 变为 2 最少需要 4 次操作。
示例 3：

输入：x = 25, y = 30
输出：5
解释：我们可以通过以下操作将 25 变为 30 ：
1. 将 x 加 1
2. 将 x 加 1
3. 将 x 加 1
4. 将 x 加 1
5. 将 x 加 1
将 25 变为 30 最少需要 5 次操作。
提示：

1 <= x, y <= 104
"""
from functools import cache


# todo 方法一：BFS   类似 2059. 转化数字的最小运算数.py
# 每个操作都可以理解成：从 x 向操作后的数连边。
# 在这张图上跑 BFS，求出从 x 到 y 的最短路，即为答案。
class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        # 1.如果 x<y 那么只能用加一操作，此时可以直接算出操作次数
        if x <= y:
            return y - x

        # 2.采用双数组实现 BFS
        ans = x - y  # 总操作次数不会超过 x-y
        vis = [False] * (x + ans + 1)  # +1 操作至多执行 x-y 次
        q = []
        step = 0

        def add(v: int) -> None:
            if v < y:
                nonlocal ans
                ans = min(ans, step + 1 + y - v)  # 只能执行 +1 操作
            elif not vis[v]:
                vis[v] = True
                q.append(v)

        add(x)
        while True:
            tmp = q
            q = []
            for v in tmp:
                if v == y:
                    return min(ans, step)
                if v % 11 == 0:
                    add(v // 11)
                if v % 5 == 0:
                    add(v // 5)
                add(v - 1)
                add(v + 1)
            step += 1


# todo 方法二：记忆化搜索
class Solution2:
    @cache
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        # 从 x 到 y 有哪些方式？
        # 1.如果 x=y，无需操作。如果 x<y，只能用加一操作。
        if x <= y:
            return y - x

        # 2.如果 x>y：
        # 2.1 可以只用减一操作到达 y
        # 2.2 通过+1操作到达 x′=x−x%11，此时 x′是 11 的倍数
        # 2.3 通过-1操作到达 x′=x+x%11，此时 x′是 11 的倍数
        # 2.4 通过-1操作到达 x′=x+x%5，此时 x′是 5 的倍数
        # 2.5 通过+1操作到达 x′=x+x%5，此时 x′是 5 的倍数
        # 上述方式取最小值。
        return min(x - y,
                   self.minimumOperationsToMakeEqual(x // 11, y) + x % 11 + 1,
                   self.minimumOperationsToMakeEqual(x // 11 + 1, y) + 11 - x % 11 + 1,
                   self.minimumOperationsToMakeEqual(x // 5, y) + x % 5 + 1,
                   self.minimumOperationsToMakeEqual(x // 5 + 1, y) + 5 - x % 5 + 1)
