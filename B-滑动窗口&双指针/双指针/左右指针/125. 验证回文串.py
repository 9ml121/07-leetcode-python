"""
如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。

字母和数字都属于字母数字字符。

给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。

 

示例 1：
输入: s = "A man, a plan, a canal: Panama"
输出：true
解释："amanaplanacanalpanama" 是回文串。

示例 2：
输入：s = "race a car"
输出：false
解释："raceacar" 不是回文串。

示例 3：
输入：s = " "
输出：true
解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
由于空字符串正着反着读都一样，所以是回文串。
 

提示：
1 <= s.length <= 2 * 10^5
s 仅由可打印的 ASCII 字符组成
"""

# todo 方法1：正则替换字符串非字母数字字符，左右双指针判断回文串
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 将s所有大写字符转换为小写字符、并移除所有非字母数字字符之后,判断是否为回文串
        import re
        # 将s中大写字母转小写
        s = s.lower()

        # 替换s中非字母数字字符
        # s = s.replace(r'[^0-9a-z]', '') # 注意：这个写法是错的，replace方法不能用正则匹配
        s = re.sub(r'[^0-9a-z]', '', s)

        # 左右双指针判断回文串
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True


# 方法2：字符串isalnum方法过滤非字母和数字字符，字符串反转方法判断回文串
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 将s所有大写字符转换为小写字符、并移除所有非字母数字字符之后,判断是否为回文串
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]
