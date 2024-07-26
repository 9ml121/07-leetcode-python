"""
对于任何字符串，我们可以通过删除其中一些字符（也可能不删除）来构造该字符串的 子序列 。(例如，“ace” 是 “abcde” 的子序列，而 “aec” 不是)。

给定源字符串 source 和目标字符串 target，返回 源字符串 source 中能通过串联形成目标字符串 target 的 子序列 的最小数量 。
如果无法通过串联源字符串中的子序列来构造目标字符串，则返回 -1。



示例 1：
输入：source = "abc", target = "abcbc"
输出：2
解释：目标字符串 "abcbc" 可以由 "abc" 和 "bc" 形成，它们都是源字符串 "abc" 的子序列。

示例 2：
输入：source = "abc", target = "acdbc"
输出：-1
解释：由于目标字符串中包含字符 "d"，所以无法由源字符串的子序列构建目标字符串。

示例 3：
输入：source = "xyz", target = "xzyxz"
输出：3
解释：目标字符串可以按如下方式构建： "xz" + "y" + "xz"。


提示：

1 <= source.length, target.length <= 1000
source 和 target 仅包含英文小写字母。
"""

# todo 考察点：贪心 + 双指针

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # ans: 源字符串 source 中能通过串联形成目标字符串 target 的 子序列 的最小数量
        ans = 0
        # ti表示未匹配target子串的下标
        ti = 0 
        while ti < len(target):
            # pre标记target下一个匹配字符的开始位置
            pre = ti

            # 以滑动窗口的方式扫target字符串, 找source的子序列，窗口大小为source的长度
            # 每次向右移动的距离是source子序列的长度
            for c in source:
                if ti < len(target) and target[ti] == c:
                    ti += 1

            # 当一轮匹配过后，ti没有变化，说明ti的字符不存在source字符串
            if pre == ti: 
                return -1

            # 每轮匹配完，需要的子序列个数+1
            ans += 1

        return ans
