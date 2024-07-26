"""
有 n 个筹码。第 i 个筹码的位置是 position[i] 。

我们需要把所有筹码移到同一个位置。在一步中，我们可以将第 i 个筹码的位置从 position[i] 改变为:

position[i] + 2 或 position[i] - 2 ，此时 cost = 0
position[i] + 1 或 position[i] - 1 ，此时 cost = 1
返回将所有筹码移动到同一位置上所需要的 最小代价 。



示例 1：



输入：position = [1,2,3]
输出：1
解释：第一步:将位置3的筹码移动到位置1，成本为0。
第二步:将位置2的筹码移动到位置1，成本= 1。
总成本是1。
示例 2：



输入：position = [2,2,2,3,3]
输出：2
解释：我们可以把位置3的两个筹码移到位置2。每一步的成本为1。总成本= 2。
示例 3:

输入：position = [1,1000000000]
输出：1


提示：

1 <= position.length <= 100
1 <= position[i] <= 10^9
"""
from typing import List

"""
贪心算法的直觉：
1.既然「不限操作次数」，且「将第 i 个筹码向左或者右移动 2 个单位，代价为 0」，
  我们可以就可以尽量多地使用这种操作，将 所有的 筹码放在 相邻的 两个位置上；
2.然后我们再使用「将第 i 个筹码向左或者右移动 1 个单位，代价为 1」 操作，将其中一个位置上的所有筹码移动到另一个位置上。
  为了使得代价最少，我们将数量较少的筹码堆的所有筹码移动到数量较多的筹码堆，代码就是两堆筹码数量的较少者。
"""

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # 统计输入数组里奇/偶数的个数
        odd, even = 0, 0
        for pos in position:
            if pos % 2 == 0:
                odd += 1
            else:
                even += 1

        return min(odd, even)
