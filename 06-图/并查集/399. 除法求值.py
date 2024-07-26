"""
给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，
其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。
每个 Ai 或 Bi 是一个表示单个变量的字符串。

另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，
请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。

返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。
如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。

注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。
注意：未在等式列表中出现的变量是未定义的，因此无法确定它们的答案。



示例 1：
输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0],
     queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
条件：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
注意：x 是未定义的 => -1.0

示例 2：
输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0],
     queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
输出：[3.75000,0.40000,5.00000,0.20000]

示例 3：
输入：equations = [["a","b"]], values = [0.5],
     queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
输出：[0.50000,2.00000,-1.00000,-1.00000]


提示：
1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj 由小写英文字母与数字组成
"""
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent = dict()
        weight = dict()

        def find(x):
            if x not in parent:
                parent[x] = x
                weight[x] = 1
            else:
                if parent[x] != x:
                    original = parent[x]
                    parent[x] = find(parent[x])
                    # todo 先更新较浅层结点的权值，较深层结点的权值需要根据较浅层结点的权值进行更新
                    weight[x] *= weight[original]

            return parent[x]

        def union(x, y, val):
            px, py = find(x), find(y)
            parent[px] = py
            # 需要列方程计算
            weight[px] = weight[y] * val / weight[x]

        def isConnected(x, y):
            if (x not in parent) or (y not in parent):
                return False
            return find(x) == find(y)

        n = len(equations)
        for i in range(n):
            x, y = equations[i]
            val = values[i]
            union(x, y, val)

        # print(parent)
        # print(weight)
        res = []
        for x, y in queries:
            ans = -1.0
            if isConnected(x, y):
                ans = weight[x] / weight[y]

            res.append(ans)

        return res


if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    # [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
