"""
给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。

元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现不止一次。

 

示例 1：

输入：s = "hello"
输出："holle"
示例 2：

输入：s = "leetcode"
输出："leotcede"
 

提示：

1 <= s.length <= 3 * 105
s 由 可打印的 ASCII 字符组成
"""

# 简单的左右双指针


class Solution:
    def reverseVowels(self, s: str) -> str:
        # 反转s中的元音字符
        yuan_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        chars = list(s)
        n = len(chars)
        l = 0
        r = n-1
        while l < r:
            if chars[l] not in yuan_set:
                l += 1
            elif chars[r] not in yuan_set:
                r -= 1
            else:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1

        ans = ''.join(chars)
        return ans
