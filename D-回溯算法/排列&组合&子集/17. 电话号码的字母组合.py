"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2：
输入：digits = ""
输出：[]

示例 3：
输入：digits = "2"
输出：["a","b","c"]


提示：
0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。
"""

from typing import List

# todo 回溯算法

MAPPING = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
# 写法1
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 给定一个仅包含数字 2-9 的字符串digits，返回所有它能表示的字母组合, digits='23'
        n = len(digits)
        if n == 0:
            return []
        
        # 时间复杂度 O(n*4^n), 一个数字最多对应4个字母
        ans = []
        def dfs(i=0, path=''):   # todo 这里path定义为字符串，可以避免后面写回溯语句
            if i == n:
                # 由于字符串的特殊性，path 每次都是新的，因此无需再创建拷贝
                ans.append(path)
                return

            for c in MAPPING[int(digits[i])]:
                # 注意：path + c 生成新的字符串，无需状态重置
                dfs(i + 1, path + c)

        dfs()
        return ans

# 写法2
class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        # 给定一个仅包含数字 2-9 的字符串digits，返回所有它能表示的字母组合, digits='23'
        n = len(digits)
        if n == 0:
            return []

        ans = []
        def dfs(i=0, path=[''] * n): # todo 这里path定义为固定长度数组，也可以避免后面写回溯语句
            if i == n:
                # 创建了新的字符串，所以这里path无需拷贝
                ans.append(''.join(path))
                return

            for c in MAPPING[int(digits[i])]:
                # 下次递归会直接覆盖掉path[i]元素，所以这里不用显式写回溯语句
                path[i] = c
                dfs(i + 1, path)

        dfs()
        return ans

# 写法3
class Solution3:
    def letterCombinations(self, digits: str) -> List[str]:
        # 给定一个仅包含数字 2-9 的字符串digits，返回所有它能表示的字母组合, digits='23'
        n = len(digits)
        if n == 0:
            return []

        ans = []

        def dfs(i=0, path=[]): # todo 这里path定义为空数组，后面递归就要写回溯语句
            if i == n:
                # 创建了新的字符串，所以这里path无需拷贝
                ans.append(''.join(path))
                return

            for c in MAPPING[int(digits[i])]:
                # 下次递归会直接覆盖掉path[i]元素，所以这里不用显式写回溯语句
                path.append(c)
                dfs(i + 1, path)
                path.pop()

        dfs()
        return ans

if __name__ == '__main__':
    digits = "23"
    print(Solution2().letterCombinations(digits))
