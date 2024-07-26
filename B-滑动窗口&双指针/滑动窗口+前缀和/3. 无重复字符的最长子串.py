"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。


示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
"""
import collections

# todo 不固定长度滑动窗口

# todo 方法3：滑窗 + 计数器
# 时间复杂度：O(N)
# 空间复杂度：O(set(s))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 返回无重复字符的最长子串长度
        ans = 0
        # todo 循环不变量：nums[l..r] 不包含重复字符
        # todo cnt字典记录窗口nums[l..r]内每个字符出现次数
        char_cnts = collections.Counter()

        l = 0
        for r, c in enumerate(s):
            # 入
            char_cnts[c] += 1
            
            # 出
            while char_cnts[c] > 1:
                # 注意：这里循环条件是s[r]出现次数大于1, 才需要窗口左移
                char_cnts[s[l]] -= 1
                l += 1

            # 更新ans
            ans = max(ans, r-l+1)

        return ans
    
# 方法2：不固定长度滑动窗口 + 集合
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 返回无重复字符的最长子串长度
        ans = 0
        # todo window用一个集合记录窗口不重复元素
        window = set()
        
        l = 0
        for r, c in enumerate(s):
            if c in window:
                # todo 如果c在窗口出现过，l应该左移到上一个相同字符的下一个位置，并且window要移除窗口左移丢掉的字符
                while s[l] != c:
                    window.remove(s[l])
                    l += 1
                # 经过while循环，l来到窗口重复字符索引，然后跳到下一位，保证nums[l..r]没有重复字符
                l += 1
            else:
                window.add(s[r])
                ans = max(ans, r - l + 1)
        return ans



        
# 方法1--暴力解法: 缺点：每次遍历s[i]都需要检查s[i]是否在数组前面出现过
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 返回s无重复字符的最长子串长度
        ans = 0
        start = 0
        for i in range(len(s)):
            # 第二层遍历是为了保证s[start, i]内的元素都不重复
            for j in range(start, i):
                if s[j] == s[i]:
                    start = j + 1
                    break
            ans = max(ans, i - start + 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
