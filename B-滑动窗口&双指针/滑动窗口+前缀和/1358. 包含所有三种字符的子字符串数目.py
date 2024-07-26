"""
给你一个字符串 s ，它只包含三种字符 a, b 和 c 。

请你返回 a，b 和 c 都 至少 出现过一次的子字符串数目。

 

示例 1：

输入：s = "abcabc"
输出：10
解释：包含 a，b 和 c 各至少一次的子字符串为 "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" 和 "abc" (相同字符串算多次)。
示例 2：

输入：s = "aaacb"
输出：3
解释：包含 a，b 和 c 各至少一次的子字符串为 "aaacb", "aacb" 和 "acb" 。
示例 3：

输入：s = "abc"
输出：1
 

提示：

3 <= s.length <= 5 x 10^4
s 只包含字符 a，b 和 c 。
"""  

import collections


# todo 方法1：不定长滑窗 + 窗口计数问题
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # 返回3种字符至少都出现一次的子串数量
        n = len(s)
        ans = 0

        # todo [l..r]含有3种字符
        freq = collections.Counter()
        sz = 0
        l = 0
        for r, c in enumerate(s):
            # 入
            if freq[c] == 0:
                sz += 1
            freq[c] += 1

            while sz == 3:
                # 更新ans: 以当前l开头，r后面的元素个数，abcaa
                ans += n-r
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    sz -= 1
                l += 1

        return ans

# todo 方法2：不定长滑窗 + 前缀和思想
# 求a,b,c各至少出现一次的次数，可以转换为窗口元素集合最多为3个的个数 - 窗口元素集合最多为2个的个数


class Solution2:
    def numberOfSubstrings(self, s: str) -> int:
        # 返回3种字符至少都出现一次的子串数量

        def get_atMostKth_subStr(k: int) -> int:
            # 求窗口元素集合最多为k个的子数组个数
            n = len(s)
            ans = 0
            
            # todo [l..r]最多含有3种字符
            freq = collections.Counter()
            sz = 0
            l = 0
           
            for r, c in enumerate(s):
                # 入
                if freq[c] == 0:
                    sz += 1
                freq[c] += 1
                
                # 出
                while sz > k:
                    freq[s[l]] -= 1
                    if freq[s[l]] == 0:
                        sz -= 1
                    l += 1
                
                # 更新ans
                ans += r - l + 1
              
            return ans

        return get_atMostKth_subStr(3) - get_atMostKth_subStr(2)
