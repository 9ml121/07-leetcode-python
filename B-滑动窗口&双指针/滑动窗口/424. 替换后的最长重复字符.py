"""
题目描述
给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。

在执行上述操作后，返回包含相同字母的最长子字符串的长度。

示例 1：
输入：s = "ABAB", k = 2
输出：4
解释：用两个'A'替换为两个'B',反之亦然。

示例 2：
输入：s = "AABABBA", k = 1
输出：4
解释：
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子字符串 "BBBB" 有最长相同字母, 答案为 4。

提示：
1 <= s.length <= 10^5
s 仅由大写英文字母组成
1 <= k <= s.length

"""
import collections


# todo 不固定长度滑动窗口 + 计数器

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """返回s中字符被替换k次之后，包含相同字母的最长子字符串的长度"""

        # 枚举字符串中的每一个位置作为右端点，然后找到其最远的右端点的位置，满足该区间内除了出现次数最多的那一类字符之外，剩余的字符（即非最长重复字符）数量不超过 k 个
        char_cnts = collections.Counter()  # 窗口内元素出现的个数
        max_cnt = 0  # 窗口内相同元素出现最多的个数

        l = 0
        for r, c in enumerate(s):
            # 入: 每次右指针右移，如果区间仍然满足条件，那么左指针不移动，否则左指针至多右移一格，保证区间长度不减小
            char_cnts[c] += 1
            max_cnt = max(max_cnt, char_cnts[c])

            # todo 出:虽然这样的操作会导致部分区间不符合条件，即该区间内非最长重复字符超过了 k 个。但是这样的区间也同样不可能对答案产生贡献。
            if r - l + 1 > max_cnt + k:
                remove = s[l]
                char_cnts[remove] -= 1
                l += 1

        # 当我们右指针移动到尽头，左右指针对应的区间的长度必然对应一个长度最大的符合条件的区间
        ans = len(s) - l 
        return ans



if __name__ == '__main__':
    sol = Solution()
    # print(sol2.characterReplacement("ABAB", 2))
    # print(sol2.characterReplacement("AABABBA", 1))
    # print(sol2.characterReplacement("AABABBA", 2))

    print(sol.characterReplacement("AAAAA", 5))

