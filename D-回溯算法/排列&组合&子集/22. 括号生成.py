"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"]

提示：
1 <= n <= 8
"""
from typing import List


# 方法 1:dfs（做加法）
# 注意：由于字符串的特殊性，产生一次拼接都生成新的对象，因此无需回溯！！！
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(path='', l=0, r=0):
            # 递归返回条件：左右括号都已经使用了n个
            if len(path) == n * 2:
                res.append(path)
                return

            # 1.添加左括号方式：使用的左括号个数没有超过n个
            if l < n:
                dfs(path + '(', l + 1, r)

            # 2.添加右括号方式：使用的左括号数量大于右括号，才能添加右括号
            if l > r:
                dfs(path + ')', l, r + 1)

        dfs()
        return res


# 方法 2：做减法
class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(path='', l=n, r=n):
            # 递归返回条件：左右括号都剩余0个
            if l == 0 and r == 0:
                res.append(path)
                return

            # 1.添加左括号条件：还有剩余左括号
            if l > 0:
                dfs(path + '(', l - 1, r)
            # 2.添加右括号条件：剩余左括号个数小于右括号
            if l < r:
                dfs(path + ')', l, r - 1)

        dfs()
        return res


if __name__ == '__main__':
    n = 3
    print(Solution2().generateParenthesis(n))
