"""
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

示例 1：

输入: s = "leetcode"
输出: false 
示例 2：

输入: s = "abc"
输出: true
限制：

0 <= len(s) <= 100 
s[i]仅包含小写字母
如果你不使用额外的数据结构，会很加分。
"""

# 集合
class Solution2:
    def isUnique(self, astr: str) -> bool:
        seen = set()
        for c in astr:
            if c in seen:
                return False
            seen.add(c)

        return True

# todo 集合==》状态压缩/位掩码
# 参考： https://github.com/azl397985856/leetcode/issues/432
class Solution:
    def isUnique(self, astr: str) -> bool:
        # 相当于 set
        mask = 0

        for c in astr:
            # todo 相当于判断 c 是否在 set 中
            # in 操作符，判断一个数字是否在集合中：如果是 0 表示不在 picked 中，如果是 1 表示在 picked 中
            x = ord(c) - ord('a')
            # 下面 2 种写法都可以
            # if mask >> x & 1 == 1:
            if mask & 1 << x != 0:
                return False
            
            # todo 相当于将 c 加入到 set
            # add(n) 函数， 用于将一个数加入到集合
            mask |= 1 << x
            print(bin(mask))
            
        return True


if __name__ == '__main__':
    s = "leetcode"
    Solution().isUnique(s)
