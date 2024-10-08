"""
给你一个下标从 0 开始的二进制字符串 s ，它表示一条街沿途的建筑类型，其中：

s[i] = '0' 表示第 i 栋建筑是一栋办公楼，
s[i] = '1' 表示第 i 栋建筑是一间餐厅。
作为市政厅的官员，你需要随机 选择 3 栋建筑。然而，为了确保多样性，选出来的 3 栋建筑 相邻 的两栋不能是同一类型。

比方说，给你 s = "001101" ，我们不能选择第 1 ，3 和 5 栋建筑，因为得到的子序列是 "011" ，有相邻两栋建筑是同一类型，所以 不合 题意。
请你返回可以选择 3 栋建筑的 有效方案数 。

 

示例 1：

输入：s = "001101"
输出：6
解释：
以下下标集合是合法的：
- [0,2,4] ，从 "001101" 得到 "010"
- [0,3,4] ，从 "001101" 得到 "010"
- [1,2,4] ，从 "001101" 得到 "010"
- [1,3,4] ，从 "001101" 得到 "010"
- [2,4,5] ，从 "001101" 得到 "101"
- [3,4,5] ，从 "001101" 得到 "101"
没有别的合法选择，所以总共有 6 种方法。
示例 2：

输入：s = "11100"
输出：0
解释：没有任何符合题意的选择。
 

提示：

3 <= s.length <= 105
s[i] 要么是 '0' ，要么是 '1' 。
"""

# todo 前缀和思想
class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        cnt0 = s.count('0')
        cnt1 = n - cnt0

        # 101：统计位置为0，前后为1的个数
        # 010: 统计位置为1，前后为0的个数
        ans = 0
        pre0 = 0
        pre1 = 0
        for c in s:
            if c == "0":
                suf1 = cnt1 - pre1
                ans += pre1 * suf1
                pre0 += 1
            else:
                suf0 = cnt0 - pre0
                ans += pre0 * suf0
                pre1 += 1

        return ans
