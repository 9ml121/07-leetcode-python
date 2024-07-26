"""
给你一个整数数组 nums 。玩家 1 和玩家 2 基于这个数组设计了一个游戏。
1.玩家 1 和玩家 2 轮流进行自己的回合，玩家 1 先手。
2.开始时，两个玩家的初始分值都是 0 。
3.每一回合，玩家从数组的任意一端取一个数字（即，nums[0] 或 nums[nums.length - 1]），取到的数字将会从数组中移除（数组长度减 1 ）。
  玩家选中的数字将会加到他的得分上。
4.当数组中没有剩余数字可取时，游戏结束。

如果玩家 1 能成为赢家，返回 true 。如果两个玩家得分相等，同样认为玩家 1 是游戏的赢家，也返回 true 。
你可以假设每个玩家的玩法都会使他的分数最大化。

示例 1：
输入：nums = [1,5,2]
输出：false
解释：一开始，玩家 1 可以从 1 和 2 中进行选择。
如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2 ）可选。
所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。
因此，玩家 1 永远不会成为赢家，返回 false 。

示例 2：
输入：nums = [1,5,233,7]
输出：true
解释：玩家 1 一开始选择 1 。然后玩家 2 必须从 5 和 7 中进行选择。无论玩家 2 选择了哪个，玩家 1 都可以选择 233 。
最终，玩家 1（234 分）比玩家 2（12 分）获得更多的分数，所以返回 true，表示玩家 1 可以成为赢家。


提示：
1 <= nums.length <= 20
0 <= nums[i] <= 10^7
"""
from typing import List

"""
解题思路：
这是一个博弈论的问题，可以使用动态规划的思想来解决。下面给出该问题的动态规划解法的思路：
1.创建一个二维数组 dp，其中 dp[i][j] 表示在数组的区间 [i, j] 内，玩家1能够获得比玩家2更高的分数的最大差值。
2.使用动态规划的思想，从最小的子问题开始，逐步增加问题的规模，直到解决整个问题。
3.对于任意的子问题 dp[i][j]，玩家1可以选择从数组的开头 nums[i] 或末尾 nums[j] 取数，取到的数累加到自己的分数上。
  玩家2也会选择最优策略取数，因此玩家1的选择会受到玩家2的影响。
  玩家1的选择有两种情况：
    1) 如果玩家1选择取 nums[i]，则玩家1的分数为 nums[i]，玩家2在区间 [i+1, j] 内的得分最大差值为 dp[i+1][j]，
       因此玩家1能够获得的分数差值为 nums[i] - dp[i+1][j]。
    2) 如果玩家1选择取 nums[j]，则玩家1的分数为 nums[j]，玩家2在区间 [i, j-1] 内的得分最大差值为 dp[i][j-1]，
       因此玩家1能够获得的分数差值为 nums[j] - dp[i][j-1]。
    3) 玩家1会选择两种情况中的较大值，即 dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])。
4.最终，dp[0][n-1] 表示在整个数组范围内，玩家1能够获得比玩家2更高的分数的最大差值。
  如果 dp[0][n-1] >= 0，则玩家1能够保证获胜；否则，玩家1无法保证获胜。
"""


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        # todo dp[i][j] 表示在数组的区间 [i, j] 内，先手可以获得的相对分数。
        dp = [[0] * n for _ in range(n)]
        # todo 初始化dp[i][i]=nums[i]， 最后要判断dp[0][n-1]正负

        # 3.状态转移：dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])。
        # 先要得到dp[i][j]正下方，正左方的结果=> i从下往上，j从左往右
        for i in range(n - 1, -1, -1):
            dp[i][i] = nums[i]
            for j in range(i + 1, n):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
            print(f'遍历第 {i} 行 => {dp[i]}')

        return dp[0][n - 1] >= 0


if __name__ == '__main__':
    # nums = [1, 5, 2]
    # nums = [1, 5, 233, 7]
    nums = [1, 5, 2, 4, 6]
    print(Solution().predictTheWinner(nums))

"""
[1, 5, 233, 7]
  
[[0, 5, 228, 227], 
 [0, 0, 233, -226], 
 [0, 0, 0,   233], 
 [0, 0, 0,   0]]
"""
