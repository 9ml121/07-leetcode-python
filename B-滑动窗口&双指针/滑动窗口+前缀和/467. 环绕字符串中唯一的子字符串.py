"""
定义字符串 base 为一个 "abcdefghijklmnopqrstuvwxyz" 无限环绕的字符串，所以 base 看起来是这样的：

"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
给你一个字符串 s ，请你统计并返回 s 中有多少 不同非空子串 也在 base 中出现。

 

示例 1：

输入：s = "a"
输出：1
解释：字符串 s 的子字符串 "a" 在 base 中出现。
示例 2：

输入：s = "cac"
输出：2
解释：字符串 s 有两个子字符串 ("a", "c") 在 base 中出现。
示例 3：

输入：s = "zab"
输出：6
解释：字符串 s 有六个子字符串 ("z", "a", "b", "za", "ab", and "zab") 在 base 中出现。
 

提示：

1 <= s.length <= 105
s 由小写英文字母组成
"""


from collections import defaultdict

# todo 滑动窗口 + 前缀和思想
# 这个思想和 1297. 子串的最大出现次数 剪枝的方法有异曲同工之妙。

# 参考：https://leetcode.cn/problems/unique-substrings-in-wraparound-string/solutions/432752/xi-fa-dai-ni-xue-suan-fa-yi-ci-gao-ding-qian-zhui-

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        # 返回 s 中有多少 不同非空子串 在 base 中出现
        
        # todo cnts字典中：key 是字母， value 是长度。 含义是以 key 结尾的 最长连续子串 的长度。
        # cnts字典可以达到去重的目的，这种算法是不重不漏的，因为最长的连续子串一定是包含了比它短的连续子串，
        cnts = defaultdict(int)
        # w 记录当前字符结尾的连续子串长度，遍历过程根据 w 的值更新 cnts
        w = 0
        
        for i, ch in enumerate(p):
            if i > 0 and (ord(ch) - ord(p[i - 1])) % 26 == 1:  # 字符之差为 1 或 -25
            # if i>0 and (ord(p[i])-ord(p[i-1]) == 1 or ord(p[i])-ord(p[i-1])) == -25:
                w += 1
            else:
                w = 1
            cnts[ch] = max(cnts[ch], w)
        
        # 返回 dp 中所有 value 的和。
        return sum(cnts.values())
