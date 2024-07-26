"""
现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。
给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。

例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。

返回你为了学完所有课程所安排的学习顺序。
可能会有多个正确的顺序，你只要返回 任意一种 就可以了。
如果不可能完成所有课程，返回 一个空数组 。


示例 1：
输入：numCourses = 2, prerequisites = [[1,0]]
输出：[0,1]
解释：总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。

示例 2：
输入：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
输出：[0,2,1,3]
解释：总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。

示例 3：
输入：numCourses = 1, prerequisites = []
输出：[0]


提示：
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
所有[ai, bi] 互不相同
"""
import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 特判
        if len(prerequisites) == 0:
            # 没有先选课程，任意顺序返回都可以
            return list(range(numCourses))

        # 入度(数组或者字典表示)
        in_degrees = [0] * numCourses
        # 出度（数组或者字典表示）
        out_degrees = [set() for _ in range(numCourses)]  

        # 初始化入度和出度
        for second, first in prerequisites:
            in_degrees[second] += 1
            out_degrees[first].add(second)

        # 先将入度为 0的课程加入 dq， 表示需要先选
        dq = collections.deque()
        for course in range(numCourses):
            if in_degrees[course] == 0:
                dq.append(course)

        # bfs遍历 dq, 入度值为 0，代表需要先选，将出列的课程依次加入ans, 并统计已选课程数cnt
        ans = []
        cnt = 0
        while dq:
            cur_course = dq.popleft()
            cnt += 1
            ans.append(cur_course)

            for next_course in out_degrees[cur_course]:
                in_degrees[next_course] -= 1
                if in_degrees[next_course] == 0:  # 入度值降为 0，证明当前需要先选，加入队列
                    dq.append(next_course)

        return ans if cnt == numCourses else []


if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]  # [0, 1, 2, 3]
    print(Solution().findOrder(numCourses, prerequisites))
