"""
给你一个字符串 s ，请你拆分该字符串，并返回拆分后唯一子字符串的最大数目。
字符串 s 拆分后可以得到若干 非空子字符串 ，这些子字符串连接后应当能够还原为原字符串。但是拆分出来的每个子字符串都必须是 唯一的 。
注意：子字符串 是字符串中的一个连续字符序列。

示例 1：
输入：s = "ababccc"
输出：5
解释：一种最大拆分方法为 ['a', 'b', 'ab', 'c', 'cc'] 。像 ['a', 'b', 'a', 'b', 'c', 'cc'] 这样拆分不满足题目要求，因为其中的 'a' 和 'b' 都出现了不止一次。

示例 2：
输入：s = "aba"
输出：2
解释：一种最大拆分方法为 ['a', 'ba'] 。

示例 3：
输入：s = "aa"
输出：1
解释：无法进一步拆分字符串。

提示：
1 <= s.length <= 16
s 仅包含小写英文字母
"""


# 方法 1：回溯 + 剪枝
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # 返回拆分s后唯一子字符串的最大数目。
        ans = 0
        n = len(s)
 
        def dfs(i=0, path=set()): # todo path用集合记录路径不重复子串
            nonlocal ans
            if i == n:
                ans = max(ans, len(path))
                print(path)
                return

            # 剪枝条件：剩余字符数 + 当前已有的唯一子字符串数 <= 当前最大的子字符串数目
            # 假设：剩余字符每1个都是一个不重复子串
            if n - i + len(path) <= ans:
                return

            for j in range(i, n):
                sub_str = s[i: j + 1]
                if sub_str in path:
                    continue

                path.add(sub_str)
                dfs(j + 1)
                path.remove(sub_str)

        dfs(0)
        return ans


if __name__ == '__main__':
    s = "wwwzfvedwfvhsww"
    s = 'ababccc'
    print(Solution().maxUniqueSplit(s))
