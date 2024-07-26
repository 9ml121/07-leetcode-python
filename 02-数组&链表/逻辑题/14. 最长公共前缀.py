"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。


示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
 

提示：
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成
"""


from typing import List

# todo 简单的多指针指向问题

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 查找字符串数组中的最长公共前缀
        
        # 1.初始化最长公共前缀ans为数组第一个字符串
        ans = strs[0]
        
        # 2.遍历strs[1:], 更新ans
        for s in strs[1:]:
            # 查找当前字符串s和ans最长的公共前缀，i同时指向s和ans
            i = 0 
            while i < len(ans) and i < len(s) and ans[i] == s[i]:
                i += 1

            if i == 0:  # 没有公共前缀，提前返回结果''
                return ''

            # 更新ans
            ans = ans[:i]
        return ans
