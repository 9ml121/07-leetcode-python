"""
给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。

换句话说，s1 的排列之一是 s2 的 子串 。



示例 1：

输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
示例 2：

输入：s1= "ab" s2 = "eidboaoo"
输出：false


提示：

1 <= s1.length, s2.length <= 104
s1 和 s2 仅包含小写字母
"""
import collections

# todo 不定长滑动窗口 + 计数器
# 类似：A-滑动窗口&双指针\滑动窗口\438. 找到字符串中所有字母异位词.py

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """判断 s2 是否包含 s1 的排列"""
        if len(s1) > len(s2):
            return False
        
        # todo 循环不变量：s2[l..r]窗口包含s1所有元素，且个数相同
        need_dict = collections.Counter(s1) 
        need_sz = len(need_dict)

        l = 0
        for r, c in enumerate(s2):
            # 1.入
            if c in need_dict:
                need_dict[c] -= 1
                if need_dict[c] == 0:
                    need_sz -= 1

            while need_sz == 0:
                if r - l + 1 == len(s1):
                    # 3.更新ans
                    return True
                
                # 2.出
                remove = s2[l]
                if remove in need_dict:
                    need_dict[remove] += 1
                    if need_dict[remove] > 0:
                        need_sz += 1
                l += 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.checkInclusion("ab", "eidbaooo"))
    print(s.checkInclusion("ab", "eidboaoo"))
