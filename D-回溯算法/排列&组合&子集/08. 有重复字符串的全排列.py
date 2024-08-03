"""
有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。
 输入：S = "qqe"
 输出：["eqq","qeq","qqe"]
 输入：S = "ab"
 输出：["ab", "ba"]

提示:
字符都是英文字母。
字符串长度在[1, 9]之间。
"""
import itertools
from typing import List


# 解法1：利用python迭代函数itertools.permutations
class Solution:
    def permutation(self, S: str) -> List[str]:
        ans = []
        for elem in set(itertools.permutations(list(S), len(S))):
            ans.append(''.join(elem))
        return ans


# 解法2：递归 + 回溯,亲自实现itertools.permutations功能
# 在07的基础上，对于重复元素，递归函数加了数组排序和剪枝的功能

class Solution2:
    def permutation(self, S: str) -> List[str]:

        # 写法1(效率高)：1.采用数组切片的方式，对原字符串s有动态修改。  2.叶子节点是判断原字符床s为''
        # 这段代码和07的代码几乎相同，就是添加了排序和剪枝的逻辑。
        def helper(s: str, path: list, res: list):
            if s == '':
                res.append(''.join(path))
                return

            for i in range(len(s)):
                # 剪枝：数组是有序的，相同元素会排在一起
                if i > 0 and s[i] == s[i - 1]:
                    continue

                path.append(s[i])
                helper(s[:i] + s[i + 1:], path, res)
                path.pop()

        # 写法2(通用性强):1。用 used 数组标记已经在路径上的元素避免重复选择，对原数组没有修改。 2。叶子节点是判断path长度等于len(s)
        def backtrack(s, path, res, used):
            """
            你对比一下之前的标准全排列解法代码，这段解法代码只有两处不同：
            1、对 nums 进行了排序。
            2、添加了一句额外的剪枝逻辑。
            类比输入包含重复元素的子集/组合问题，你大概应该理解这么做是为了防止出现重复结果。
            但是注意排列问题的剪枝逻辑，和子集/组合问题的剪枝逻辑略有不同：新增了 !used[i - 1] 的逻辑判断。

            标准全排列算法之所以出现重复，是因为把相同元素形成的排列序列视为不同的序列，但实际上它们应该是相同的；
            而如果固定相同元素形成的序列顺序，当然就避免了重复。

            当出现重复元素时，比如输入 nums = [1,2,2',2'']，2' 只有在 2 已经被使用的情况下才会被选择，
            同理，2'' 只有在 2' 已经被使用的情况下才会被选择，这就保证了相同元素在排列中的相对位置保证固定
            """
            if len(path) == len(s):
                res.append(''.join(path.copy()))  # 注意要创建为新数组
                return

            for i in range(len(s)):
                # 已经存在 path 中的元素，不能重复选择
                if used[i]:
                    continue
                # 剪枝：新添加的剪枝逻辑，固定相同的元素在排列中的相对位置
                if i > 0 and s[i] == s[i - 1] and not used[i - 1]:
                    # 如果前面的相邻相等元素没有用过，则跳过
                    continue
                # 确认
                path.append(s[i])
                used[i] = True
                backtrack(s, path, res, used)
                path.pop()
                used[i] = False

            # 写法3：
            def backtrack2(nums: List[int], track: List[int]):
                # add type annotation on function params and reserve comments
                # 初始化
                # used 存储已经选择过的下标 i，避免重复选择
                # res 用于存储结果
                used = set()
                res = []

                # 递归回溯函数定义
                def dfs():
                    # 到达叶子结点后，记录并返回
                    if len(track) == len(nums):
                        # 注意要加[:]
                        res.append(track[:])
                        return

                    # 记录之前树枝上元素的值
                    # 题目说 -10 <= nums[i] <= 10，所以初始化为特殊值
                    prev_num = -666
                    for i in range(len(nums)):
                        # 排除不合法的选择
                        if i in used or nums[i] == prev_num:
                            continue

                        # 做出选择
                        track.append(nums[i])
                        used.add(i)
                        # 记录这条树枝上的值
                        prev_num = nums[i]

                        # 进入下一层决策树
                        dfs()

                        # 取消选择
                        track.pop()
                        used.remove(i)

                # 驱动函数
                dfs()

                return res

        # 关键：因为有重复元素，为了避免重复遍历，需要先对数组排序，目的是将重复元素排在相邻位置！！
        s = ''.join(sorted(S))
        res = []  # 全局变量：最终返回结果
        path = []  # 用于存储路径
        # helper(s, path, res)
        used = [False] * len(S)  # 记录元素是否使用过
        backtrack(s, path, res, used)
        return sorted(res)


if __name__ == '__main__':
    cls = Solution2()
    s = 'qqe'
    print(cls.permutation(s))
