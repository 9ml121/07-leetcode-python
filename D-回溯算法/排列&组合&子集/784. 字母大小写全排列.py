"""
给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。
返回 所有可能得到的字符串集合 。以 任意顺序 返回输出。

示例 1：
输入：s = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]

示例 2:
输入: s = "3z4"
输出: ["3z4","3Z4"]

提示:
1 <= s.length <= 12
s 由小写英文字母、大写英文字母和数字组成
"""
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # 将字符串 s 中的每个字母转变大小写，返回 所有可能得到的字符串集合
        ans = []
        n = len(s)
        def dfs(i=0, path=''):
            if i == n:
                ans.append(path)
                return

            c = s[i]
            if c.isdigit():
                dfs(i + 1, path + c)
            else:
                # 字母，可以选择小写，也可以选择大写
                dfs(i + 1, path + c.lower())
                dfs(i + 1, path + c.upper())

       
        dfs()
        return ans
