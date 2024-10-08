"""
给你一个下标从 0 开始的二进制字符串 s ，表示一个列车车厢序列。s[i] = '0' 表示第 i 节车厢 不 含违禁货物，而 s[i] = '1' 表示第 i 节车厢含违禁货物。

作为列车长，你需要清理掉所有载有违禁货物的车厢。你可以不限次数执行下述三种操作中的任意一个：

从列车 左 端移除一节车厢（即移除 s[0]），用去 1 单位时间。
从列车 右 端移除一节车厢（即移除 s[s.length - 1]），用去 1 单位时间。
从列车车厢序列的 任意位置 移除一节车厢，用去 2 单位时间。
返回移除所有载有违禁货物车厢所需要的 最少 单位时间数。

注意，空的列车车厢序列视为没有车厢含违禁货物。

 

示例 1：

输入：s = "1100101"
输出：5
解释：
一种从序列中移除所有载有违禁货物的车厢的方法是：
- 从左端移除一节车厢 2 次。所用时间是 2 * 1 = 2 。
- 从右端移除一节车厢 1 次。所用时间是 1 。
- 移除序列中间位置载有违禁货物的车厢。所用时间是 2 。
总时间是 2 + 1 + 2 = 5 。

一种替代方法是：
- 从左端移除一节车厢 2 次。所用时间是 2 * 1 = 2 。
- 从右端移除一节车厢 3 次。所用时间是 3 * 1 = 3 。
总时间也是 2 + 3 = 5 。

5 是移除所有载有违禁货物的车厢所需要的最少单位时间数。
没有其他方法能够用更少的时间移除这些车厢。
示例 2：

输入：s = "0010"
输出：2
解释：
一种从序列中移除所有载有违禁货物的车厢的方法是：
- 从左端移除一节车厢 3 次。所用时间是 3 * 1 = 3 。
总时间是 3.

另一种从序列中移除所有载有违禁货物的车厢的方法是：
- 移除序列中间位置载有违禁货物的车厢。所用时间是 2 。
总时间是 2.

另一种从序列中移除所有载有违禁货物的车厢的方法是：
- 从右端移除一节车厢 2 次。所用时间是 2 * 1 = 2 。
总时间是 2.

2 是移除所有载有违禁货物的车厢所需要的最少单位时间数。
没有其他方法能够用更少的时间移除这些车厢。
 

提示：

1 <= s.length <= 2 * 10^5
s[i] 为 '0' 或 '1'
"""

# 解法一：前后缀分解


class Solution:
    # todo 前后缀分解，三次遍历：考虑将列车分成左右两部分，枚举分割线，分别计算这两部分的最少时间。
    def minimumTime(self, s: str) -> int:
        n = len(s)
        #  pre[i] 表示移除 s[i]之前 的所有违禁货物车厢所花费的最少时间。
        pre = [0] * (n+1)
        for i, c in enumerate(s):
            if c == '0':
                # 无需移除车厢
                pre[i+1] = pre[i]
            else:
                # 可以单独移除第 i 节车厢，也可以移除前 i 个车厢，二者取最小值
                pre[i+1] = min(pre[i-1]+2, i+1)

        #  suf[i] 表示移除s[i]和 s[i]之后的所有违禁货物车厢所花费的最少时间
        suf = [0] * (n+1)
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                suf[i] = suf[i+1]
            else:
                suf[i] = min(suf[i+1] + 2, n-i)

        # 枚举分割线，计算所有 pre[i]+suf[i] 的最小值，
        ans = n
        for i in range(n+1):
            ans = min(ans, pre[i] + suf[i])

        return ans


class Solution:
    # todo 前后缀分解，两次遍历
    def minimumTime(self, s: str) -> int:
        n = len(s)
        # 优化 1：可以先计算 suf，然后在枚举分割线的同时计算 pre。
        suf = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1] if s[i] == '0' else min(suf[i + 1] + 2, n - i)
        ans = suf[0]

        # 优化 2：由于计算 pre 的转移时当前状态只和上一个状态有关，因此可以使用滚动数组优化，即用一个变量来表示 pre。
        pre = 0

        # 优化 3：由于 s[i]=0 时，pre[i] 和 suf[i] 的值均不会变化，因此仅需要考虑 s[i]=1 时的 pre[i]+suf[i+1] 的最小值。
        for i, ch in enumerate(s):
            if ch == '1':
                pre = min(pre + 2, i + 1)
                ans = min(ans, pre + suf[i + 1])
        return ans


# 解法二：进一步优化，一次遍历
# 由于我们计算的是「移除前缀 + 移除分割线左侧某些车厢 + (分割线) + 移除分割线右侧某些车厢 + 移除后缀」的最少花费，
# 其中「移除分割线左侧某些车厢 + 移除分割线右侧某些车厢」都是在移除中间的某些车厢，因此这是可以合并的，
# 不妨合并到分割线左侧，即计算「移除前缀 + 移除分割线左侧某些车厢 + (分割线) + 移除后缀」的最少花费。
class Solution:
    def minimumTime(self, s: str) -> int:
        ans = n = len(s)
        pre = 0
        for i, ch in enumerate(s):
            if ch == '1':
                pre = min(pre + 2, i + 1)
            ans = min(ans, pre + n - 1 - i)
        return ans
