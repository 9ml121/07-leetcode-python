"""
有一棵特殊的苹果树，一连 n 天，每天都可以长出若干个苹果。在第 i 天，树上会长出 apples[i] 个苹果，这些苹果将会在 days[i] 天后（也就是说，第 i + days[i] 天时）腐烂，变得无法食用。也可能有那么几天，树上不会长出新的苹果，此时用 apples[i] == 0 且 days[i] == 0 表示。

你打算每天 最多 吃一个苹果来保证营养均衡。注意，你可以在这 n 天之后继续吃苹果。

给你两个长度为 n 的整数数组 days 和 apples ，返回你可以吃掉的苹果的最大数目。

 

示例 1：
输入：apples = [1,2,3,5,2], days = [3,2,1,4,2]
输出：7
解释：你可以吃掉 7 个苹果：
- 第一天，你吃掉第一天长出来的苹果。
- 第二天，你吃掉一个第二天长出来的苹果。
- 第三天，你吃掉一个第二天长出来的苹果。过了这一天，第三天长出来的苹果就已经腐烂了。
- 第四天到第七天，你吃的都是第四天长出来的苹果。

示例 2：
输入：apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
输出：5
解释：你可以吃掉 5 个苹果：
- 第一天到第三天，你吃的都是第一天长出来的苹果。
- 第四天和第五天不吃苹果。
- 第六天和第七天，你吃的都是第六天长出来的苹果。
 

提示：

apples.length == n
days.length == n
1 <= n <= 2 * 104
0 <= apples[i], days[i] <= 2 * 104
只有在 apples[i] = 0 时，days[i] = 0 才成立
"""

# todo 最小堆实现贪心后悔效果
"""
https://blog.csdn.net/qfc_128220/article/details/127695013?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522170134830016800192256289%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&request_id=170134830016800192256289&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-127695013-null-null.nonecase&utm_term=%E8%8B%B9%E6%9E%9C&spm=1018.2226.3001.4450
本题的解题思路其实就是贪心思维。

比如你手上有两包临期薯片A和B，假设A薯片明天过期，B薯片后天过期，你一天只能吃一包，那么你如何吃才能吃的多，且不会吃到过期薯片呢？

答案很简单，先吃快要过期。

即今天吃A薯片，明天吃B薯片，这样的话，就都赶在每包薯片过期前吃完了。

如果你今天吃B薯片，则明天你就不能吃A薯片了，因为明天时，A薯片就过期了。

本题比上面的情况要复杂一点，那就是每天都有新的临期薯片加入，因此每当有新的临期薯片加入时，我们就需要重新将薯片按照过期时间由近到远进行排序，先吃快要过期的。

这就是本题的解题思路
"""
# 类似题：07-优先队列&堆/贪心+堆/630. 课程表 III.py
import heapq
from typing import List

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        # 最小堆保存[苹果腐烂日期，剩余苹果数量]
        minHeap = []
        # 吃掉的苹果最大数
        ans = 0
        
        # i其实就代表当前日期
        for i in range(len(apples)):
            apple = apples[i]
            day = days[i]
            end_day = i + day  # 腐烂
            
            # 1.先判断截止到日期i, 清除掉pq中已经腐烂的苹果
            while minHeap and minHeap[0][0] == i:
                heapq.heappop(minHeap)

            # 2.如果当前有长出新苹果，先存入堆
            if apple > 0:
                heapq.heappush(minHeap, [end_day, apple])

            # 3.吃掉最快过期的苹果，并更新堆顶元素的苹果数-1
            if minHeap:
                minHeap[0][1] -= 1
                if minHeap[0][1] == 0:
                    heapq.heappop(minHeap)
                ans += 1
           

        # 4.如果遍历完apples,pq中还有元素，继续之前的逻辑
        cur_day = len(apples)
        while minHeap:
            # 先判断截止到日期cur_day, 清除掉pq中已经腐烂的苹果
            if minHeap[0][0] == cur_day:
                heapq.heappop(minHeap)
            else:
                # 吃掉最快过期的苹果，并更新堆顶元素的苹果数-1
                ans += 1
                cur_day += 1
                minHeap[0][1] -= 1
                if minHeap[0][1] == 0:
                    heapq.heappop(minHeap)
        return ans


if __name__ == '__main__':
    apples = [1, 2, 3, 5, 2]
    days = [3, 2, 1, 4, 2]
    print(Solution().eatenApples(apples, days))
