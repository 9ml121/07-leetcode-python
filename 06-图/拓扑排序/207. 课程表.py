"""
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，
其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。

请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

示例 1：
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。

示例 2：
输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。

提示：
1 <= numCourses <= 2000
0 <= prerequisites.n <= 5000
prerequisites[i].n == 2
0 <= ai, bi < numCourses
prerequisites[i] 中的所有课程对 互不相同
"""
import collections
from typing import List

"""
示例：n = 6，先决条件表：[[3, 0], [3, 1], [4, 1], [4, 2], [5, 3], [5, 4]]
0
  \  
    3
  /  \
1      5
  \  /
    4
  /
2
"""


#  todo 拓扑排序，bfs, 贪心算法
# 本题和 210. 课程表 II 是几乎一样的题目
class Solution:
    # 思想：该方法的每一步总是输出当前无前趋（即入度为零）的顶点
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        :type numCourses: int 课程门数
        :type prerequisites: List[List[int]] 课程与课程之间的关系
        :rtype: bool
        """
        # 课程的长度
        clen = len(prerequisites)
        if clen == 0:
            # 没有课程，当然可以完成课程的学习
            return True

        # todo 步骤1：统计每个顶点的入度和出度（一般可以用数组或者字典2种数据结构表示）
        # in_degrees统计每门课程的入度节点个数
        in_degrees = [0] * numCourses
        # out_degrees统计每门课程的出度节点集合
        out_degrees = [set() for _ in range(numCourses)]

        # 初始化入度和出度表
        for second, first in prerequisites:
            in_degrees[second] += 1
            out_degrees[first].add(second)

        # todo 步骤2：拓扑排序开始之前，先把所有入度为 0 的结点加入到一个队列中
        dq = collections.deque()
        for i in range(numCourses):
            if in_degrees[i] == 0:
                dq.append(i)

        # todo 步骤3：bfs实现拓扑排序，cnt统计入度节点变为0的节点个数
        cnt = 0
        while dq:
            u = dq.popleft()  
            cnt += 1  # 已选课 +1
            # 把这个结点的所有后继结点的入度减去 1，如果发现入度为 0 ，就马上添加到队列中
            for v in out_degrees[u]:  
                in_degrees[v] -= 1     
                if in_degrees[v] == 0:  
                    dq.append(v)

        # 已选课等于所有课， 返回true，否则false
        return cnt == numCourses


if __name__ == '__main__':
    n = 6
    prerequisites = [[3, 0], [3, 1], [4, 1], [4, 2], [5, 3], [5, 4]]  # True
    print(Solution().canFinish(n, prerequisites))
