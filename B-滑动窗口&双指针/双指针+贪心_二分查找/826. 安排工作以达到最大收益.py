"""
你有 n 个工作和 m 个工人。给定三个数组： difficulty, profit 和 worker ，其中:

difficulty[i] 表示第 i 个工作的难度，profit[i] 表示第 i 个工作的收益。
worker[i] 是第 i 个工人的能力，即该工人只能完成难度小于等于 worker[i] 的工作。
每个工人 最多 只能安排 一个 工作，但是一个工作可以 完成多次 。

举个例子，如果 3 个工人都尝试完成一份报酬为 $1 的同样工作，那么总收益为 $3 。如果一个工人不能完成任何工作，他的收益为 $0 。
返回 在把工人分配到工作岗位后，我们所能获得的最大利润 。

 

示例 1：

输入: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
输出: 100 
解释: 工人被分配的工作难度是 [4,4,6,6] ，分别获得 [20,20,30,30] 的收益。
示例 2:

输入: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
输出: 0
 

提示:

n == difficulty.length
n == profit.length
m == worker.length
1 <= n, m <= 10^4
1 <= difficulty[i], profit[i], worker[i] <= 105
"""



from typing import List

# todo 方法1： 排序 + 双指针 + 贪心
# 时间复杂度：O(Nlog⁡N+Qlog⁡Q)，其中 N 是任务个数，Q 是工人数量

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # 返回 在把工人分配到工作岗位后，我们所能获得的最大利润 。
        # 1. 工人只能完成难度小于等于 worker[i] 的工作
        # 2. 每个工人 最多 只能安排 一个 工作，但是一个工作可以 完成多次
        ans = 0
        jobs = list(zip(difficulty, profit))
        jobs.sort()    # 按照工作难度升序
        worker.sort()  # 按照工人能力大小升序

        i = 0    # i指向jobs, 代表当前工人不能完成的工作下标
        best = 0  # best代表当前工人可以完成的工作中，可以获得的最大收益
        for x in worker:
            while i < len(jobs) and x >= jobs[i][0]:
                # 在当前工人可以完成的工作中，更新收益最大值
                best = max(best, jobs[i][1])
                # 因为jobs难度升序，i最终指向当前工人不能完成的job下标
                i += 1

            # 将当前工人可以获得的最大收益best累加到ans
            ans += best

        return ans

# 方法2：排序 + 单调栈 + 贪心
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # 返回 在把工人分配到工作岗位后，我们所能获得的最大利润 。
        # 1. 工人只能完成难度小于等于 worker[i] 的工作
        # 2. 每个工人 最多 只能安排 一个 工作，但是一个工作可以 完成多次
        ans = 0
        # jobs按照工作难度升序排列
        jobs = sorted(zip(difficulty, profit), key=lambda x: x[0])
        # worker按照工作能力降序排列
        worker.sort(reverse=True)
        
        # todo ​st：按照job收益单调递增，栈顶是当前收益最大的工作，且工作难度是当前个人可以完成的
        st = [] 
        for job in jobs:
            if not st or job[1] > st[-1][1]:
                st.append(job)
                
        for w in worker:
            while st and st[-1][0] > w:
                st.pop()
                
            if not st:
                break
            
            ans += st[-1][1]

        return ans


