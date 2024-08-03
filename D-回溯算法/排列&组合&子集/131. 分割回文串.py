"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。
返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。

示例 1：
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]

示例 2：
输入：s = "a"
输出：[["a"]]

提示：
1 <= s.length <= 16
s 仅由小写英文字母组成
"""
from typing import List

"""
回溯思路：
1.在回溯搜索的过程中，从当前索引 i 开始遍历到字符串 s 的末尾。
2.对于每个索引 j，我们判断s[i..j]是否是回文串。
    如果是回文串，则将该子串加入到当前回文串分割方案中，并继续搜索下一个索引 j+1；
    如果不是回文串，则回溯到上一层。
3.当遍历完整个字符串 s 后，将当前回文串分割方案加入到结果列表 result 中。
"""
# 类似：C-回溯算法\排列&组合&子集\78. 子集(不重复).py

# 回溯写法 1：
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 将 s 分割成一些子串，使每个子串都是 回文串, 返回所有分割结果
        ans = []
        n = len(s)
        
        def dfs(i=0, path=[]):
            if i == n:
                ans.append(path[:])  # 需要拷贝path
                return

            # 枚举下一个位置，只能在i后面，避免产生重复结果
            for j in range(i, n):
                t = s[i:j+1]
                # 判断回文串
                if t == t[::-1]:
                    path.append(s[i:j + 1])
                    dfs(j + 1, path)
                    path.pop()

        dfs()
        return ans


# 回溯写法 2
class Solution2:
    def partition(self, s: str) -> List[List[str]]:
        # 将 s 分割成一些子串，使每个子串都是 回文串, 返回所有分割结果
        ans = []
        n = len(s)
        
        def dfs(i=0, path=[]):
            if i == n:
                ans.append(path)  # 注意：path参数在递归过程中创建了新对象，所以这里不用拷贝
                return

            # 枚举下一个位置，只能在i后面，避免产生重复结果
            for j in range(i, n):
                t = s[i:j+1]
                # 判断回文串
                if t == t[::-1]:
                    # 直接创建新的 path 变量，后面不用写回溯语句
                    dfs(j + 1, path + [s[i:j + 1]])

        dfs()
        return ans


if __name__ == '__main__':
    s = 'abaa'
    print(Solution().partition(s))
    print(Solution2().partition(s))
