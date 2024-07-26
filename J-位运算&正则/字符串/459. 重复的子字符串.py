"""
给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。


示例 1:
输入: s = "abab"
输出: true
解释: 可由子串 "ab" 重复两次构成。

示例 2:
输入: s = "aba"
输出: false

示例 3:
输入: s = "abcabcabcabc"
输出: true
解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)
 

提示：
1 <= s.length <= 104
s 由小写英文字母组成
"""




# todo 方法二：字符串匹配(推荐！！)：直接用str自带的find方法，在s+s中查找s（效率非常高,推荐！！）
"""
结论：如果s包含一个重复的子字符串，将s后面任意n个字串转移到s前面，依然满足包含一个重复子串

例如：abcabc

移位一次：cabcab
移位两次：bcabca
移位三次：abcabc

现在字符串和原字符串匹配了，所以可以得出结论存在重复的子串
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 判断s是否可以由它一个字串重复多次构成

        # 写法1
        # for i in range(1, len(s)):
        #     if s[i:] + s[:i] == s:
        #         return True
        # return False

        # 写法2（效率远高于上面写法！）
        return (s + s).find(s, 1) != len(s)


# 方法1：暴力枚举："bab bab bab bab bab"
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 判断s是否可以由它一个字串重复多次构成
        n = len(s)

        # 1.枚举字串长度为[1..n//2]
        for sz in range(1, n//2 + 1):
            sub1 = s[:sz]  # 第一个子串
            flag = True
            for i in range(sz, n, sz):
                # 2.枚举下一个开始位置为sz, 长度为sz的字串
                sub2 = s[i:i+sz]
                if sub2 != sub1:
                    flag = False
                    break

            if flag:
                return True
        return False
    
# 方法3：kmp匹配算法（省略）