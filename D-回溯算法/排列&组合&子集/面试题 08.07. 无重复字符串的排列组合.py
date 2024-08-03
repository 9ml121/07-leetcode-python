"""
无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。

示例1:
 输入：S = "qwe"
 输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]

示例2:
 输入：S = "ab"
 输出：["ab", "ba"]

提示:
字符都是英文字母。
字符串长度在[1, 9]之间。
"""
from typing import List

'''
可以直接用itertools.permutation()方法，这里亲自实现（递归+回溯）
1.刚才讲的组合/子集问题使用 start 变量保证元素 nums[start] 之后只会出现 nums[start+1..] 中的元素，
    通过固定元素的相对位置保证不出现重复的子集。
2.但排列问题本身就是让你穷举元素的位置，nums[i] 之后也可以出现 nums[i] 左边的元素，所以之前的那一套玩不转了，
    需要额外使用 used 数组来标记哪些元素还可以被选择。

延伸：
但如果题目不让你算全排列，而是让你算元素个数为 k 的排列，怎么算？
也很简单，改下 backtrack 函数的 base case，仅收集第 k 层的节点值即可
'''

# 类似： C-回溯算法\排列&组合&子集\46. 全排列.py
class Solution:
    def permutation(self, S: str) -> List[str]:
        # 返回无重复字符串s的全排列组合
        ans = []
        n = len(S)
        
        def dfs(path=[], used=[False] * n):
            if len(path) == n:
                ans.append(''.join(path))
                return

            for i, c in enumerate(S):
                if used[i]:
                    continue
                
                used[i] = True
                path.append(c)
                dfs(path, used)
                path.pop()
                used[i] = False

        dfs()
        return ans


if __name__ == '__main__':
    cls = Solution()
    S = "abc"
    print(cls.permutation(S))
