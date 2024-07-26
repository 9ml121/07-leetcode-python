"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。



示例 1:
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

示例 2:
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。


提示:

1 <= s.length, p.length <= 3 * 104
s 和 p 仅包含小写字母
"""
import collections
from typing import List

# todo 不固定长度滑窗 + 计数器
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引数组
        n = len(p)
        
        # todo 循环不变量: [l..r]窗口里的元素涵盖 p 所有字符，当窗口大小正好为n时，更新ans
        # 窗口需要的字符和相应个数
        need = collections.Counter(p)
        # 窗口内需要的元素 集合 个数
        need_cnt = len(need)
        ans = []
        
        l = 0
        for r, c in enumerate(s):
            # 入
            if c in need:
                need[c] -= 1
                if need[c] == 0:
                    need_cnt -= 1
                    
            while need_cnt == 0:
                # 更新ans
                if r - l + 1 == n:
                    ans.append(l)
                
                # 出
                remove = s[l]
                if remove in need:
                    need[remove] += 1
                    if need[remove] > 0:
                        need_cnt += 1
                l += 1
                
        return ans








if __name__ == '__main__':
    s = Solution()
    # print(s.findAnagrams("cbaebabacd", "abc"))
    # print(s.findAnagrams("abab", "ab"))
    print(s.findAnagrams("aabab", "ab"))
    # print(s.findAnagrams("abab", "abab"))
