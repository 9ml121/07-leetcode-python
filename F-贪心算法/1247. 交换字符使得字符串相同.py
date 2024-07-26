"""
有两个长度相同的字符串 s1 和 s2，且它们其中 只含有 字符 "x" 和 "y"，你需要通过「交换字符」的方式使这两个字符串相同。

每次「交换字符」的时候，你都可以在两个字符串中各选一个字符进行交换。

交换只能发生在两个不同的字符串之间，绝对不能发生在同一个字符串内部。也就是说，我们可以交换 s1[i] 和 s2[j]，但不能交换 s1[i] 和 s1[j]。

最后，请你返回使 s1 和 s2 相同的最小交换次数，如果没有方法能够使得这两个字符串相同，则返回 -1 。



示例 1：
输入：s1 = "xx", s2 = "yy"
输出：1
解释：
交换 s1[0] 和 s2[1]，得到 s1 = "yx"，s2 = "yx"。

示例 2：
输入：s1 = "xy", s2 = "yx"
输出：2
解释：
交换 s1[0] 和 s2[0]，得到 s1 = "yy"，s2 = "xx" 。
交换 s1[0] 和 s2[1]，得到 s1 = "xy"，s2 = "xy" 。
注意，你不能交换 s1[0] 和 s1[1] 使得 s1 变成 "yx"，因为我们只能交换属于两个不同字符串的字符。

示例 3：
输入：s1 = "xx", s2 = "xy"
输出：-1


提示：

1 <= s1.length, s2.length <= 1000
s1.length == s2.length
s1, s2 只包含 'x' 或 'y'。
"""

"""
「贪心算法」的直觉：
只需要关注对应位置的字符不相等的情况。
1. 根据示例 1：s1 = "xx", s2 = "yy"，如果字符串中含有这样的片段，最少需要交换一次才能使得对应位置上的字符相等；
2. 根据示例 2：s1 = "xy", s2 = "yx"，如果字符串中含有这样的片段，交换一次以后转换成示例 1 的情况，
  因此最少需要交换两次才能使得对应位置上的字符相等。
3. 还需要注意的一点是：相同位置对应字符不相等的情况应该成对出现，否则无论交换多少次，都不能使得两个字符串相等。其它细节请见「参考代码」
"""


# 贪心算法：写法 1
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        n = len(s1)
        # 在 s1 是 x，在 s2 是 y 的情况
        x2y = 0
        # 在 s2 是 y，在 s2 是 x 的情况
        y2x = 0

        for i in range(n):
            if s1[i] == 'x' and s2[i] == 'y':
                x2y += 1
            if s1[i] == 'y' and s2[i] == 'x':
                y2x += 1

        # 1.如果 x2y 和 y2x是一奇一偶，无法配对
        # 比如示例 3：xx, xy
        if (x2y % 2 + y2x % 2) == 1:
            return -1

        # 2.如果 x2y 和 y2x都是偶数，
        # 比如示例 1：xx, yy
        res = x2y // 2 + y2x // 2

        # 3.如果x2y 和 y2x都是奇数
        # 比如示例 2：xy, yx
        if (x2y % 2 + y2x % 2) == 2:
            res += 2

        return res


# 写法 2
class Solution2:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # 1.先排除掉对应位置字符一样的元素
        n = len(s1)
        new_s1 = ''
        new_s2 = ''
        for i in range(n):
            if s1[i] == s2[i]:
                continue
            new_s1 += s1[i]
            new_s2 += s2[i]

        # 2.归纳最后配对结果需要的最少交换次数
        if len(new_s1) % 2 == 1:
            return -1

        cnt_x, cnt_y = 0, 0
        for c in new_s1:
            if c == 'x':
                cnt_x += 1
            else:
                cnt_y += 1
        res = cnt_x // 2 + cnt_x % 2 + cnt_y // 2 + cnt_y % 2
        return res
