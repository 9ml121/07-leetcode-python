"""
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案。

示例 1：
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

示例 2：
输入：n = 1, k = 1
输出：[[1]]


提示：
1 <= n <= 20
1 <= k <= n
"""
import itertools
from typing import List

# todo 组合和子集是一样的：大小为 k 的组合就是大小为 k 的子集。
'''
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
问题等价于：给你输入一个数组 nums = [1,2..,n] 和一个正整数 k，请你生成所有大小为 k 的子集。

以 nums = [1,2,3] 为例，全排列是把所有节点的值都收集起来；
现在你只需要把第 2 层（根节点视为第 0 层）的节点收集起来，就是大小为 2 的所有组合：
反映到代码上，只需要稍改 base case，控制算法仅仅收集第 k 层节点的值即可
'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 返回范围 [1, n] 中所有可能的 k 个数的组合
        ans = []
        
        def dfs(k, i=1, path=[]):
            if k == 0:
                # 遍历到了第 k 层，收集当前节点的值
                ans.append(path.copy())
                return
           
            for j in range(i, n + 1):
                path.append(j)
                dfs(k-1, j+1, path)  # 通过 j 参数控制树枝的遍历，避免产生重复的子集
                path.pop()
                
        dfs(k)
        return ans


# 方法2：用itertools.combination函数
def get_result():
    lst = [1, 2, 3, 4]
    res = [list(elem) for elem in itertools.combinations(lst, 2)]
    print(res)  # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]


if __name__ == '__main__':
    cls = Solution()
    n = 4
    k = 2
    print(cls.combine(n, k))
    get_result()
