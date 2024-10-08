"""
有一份由 n 个问题组成的调查问卷，每个问题的答案要么是 0（no，否），要么是 1（yes，是）。

这份调查问卷被分发给 m 名学生和 m 名导师，学生和导师的编号都是从 0 到 m - 1 。学生的答案用一个二维整数数组 students 表示，其中 students[i] 是一个整数数组，包含第 i 名学生对调查问卷给出的答案（下标从 0 开始）。导师的答案用一个二维整数数组 mentors 表示，其中 mentors[j] 是一个整数数组，包含第 j 名导师对调查问卷给出的答案（下标从 0 开始）。

每个学生都会被分配给 一名 导师，而每位导师也会分配到 一名 学生。配对的学生与导师之间的兼容性评分等于学生和导师答案相同的次数。

例如，学生答案为[1, 0, 1] 而导师答案为 [0, 0, 1] ，那么他们的兼容性评分为 2 ，因为只有第二个和第三个答案相同。
请你找出最优的学生与导师的配对方案，以 最大程度上 提高 兼容性评分和 。

给你 students 和 mentors ，返回可以得到的 最大兼容性评分和 。

 

示例 1：

输入：students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]
输出：8
解释：按下述方式分配学生和导师：
- 学生 0 分配给导师 2 ，兼容性评分为 3 。
- 学生 1 分配给导师 0 ，兼容性评分为 2 。
- 学生 2 分配给导师 1 ，兼容性评分为 3 。
最大兼容性评分和为 3 + 2 + 3 = 8 。
示例 2：

输入：students = [[0,0],[0,0],[0,0]], mentors = [[1,1],[1,1],[1,1]]
输出：0
解释：任意学生与导师配对的兼容性评分都是 0 。
 

提示：

m == students.length == mentors.length
n == students[i].length == mentors[j].length
1 <= m, n <= 8
students[i][k] 为 0 或 1
mentors[j][k] 为 0 或 1
"""


from typing import List


# 常规解法：暴力枚举，回溯
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:

        m = len(students)
        n = len(students[0])

        # 计算 某个学生和老师的兼容性评分
        def get_score(i: int, j: int) -> int:
            res = 0
            for k in range(n):
                res += (students[i][k] == mentors[j][k])
            return res

        # 回溯算法
        ans = 0
        used = [False] * m

        def dfs(i: int, path: int):
            if i == m:
                nonlocal ans
                ans = max(ans, path)
                return

            for j in range(m):
                if not used[j]:
                    used[j] = True
                    dfs(i+1, path + get_score(i, j))
                    used[j] = False

        dfs(0, 0)
        return ans

# todo 进阶方法：状态压缩 + 动态规划
# E-动态规划/状态DP/526. 优美的排列.py
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)
        n = len(students[0])
        # 预处理：计算 m个学生和 m个导师所有配对情况下的兼容性评分
        g = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                for k in range(n):
                    g[i][j] += int(students[i][k] == mentors[j][k])

        # 状态压缩：用一个长度为 m 的二进制数 mask 表示每一名老师是否被分配了学生。
        # 如果 mask 的第 i 位为 1，那么第 i 位老师被分配到了学生，否则就没有被分配到学生
        f = [0] * (1 << m)
        for mask in range(1, 1 << m):
            cnt = mask.bit_count()
            for i in range(m):
                # 判断 mask 的第 i 位是否为 1,也可以写成 mask >> i & 1
                if mask & (1 << i):
                    # mask ^ (1 << (j-1)) 将 mask 第 j 位设置为 0，
                    f[mask] = max(f[mask], f[mask ^ (1 << i)] + g[cnt - 1][i])

        return f[(1 << m) - 1]
