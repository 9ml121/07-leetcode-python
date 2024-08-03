"""
有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。
这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。
如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。

求所能获得硬币的最大数量。


示例 1：
输入：nums = [3,1,5,8]
输出：167
解释：
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

示例 2：
输入：nums = [1,5]
输出：10


提示：
n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
"""
from typing import List

"""
问题等价于：
在一排气球points中，请你戳破气球0和气球n+1之间的所有气球（不包括0和n+1），
使得最终只剩下气球0和气球n+1两个气球，最多能够得到多少分?

0.在 nums 数组的两端添加两个值为 1 的元素，表示虚拟的气球，方便处理边界情况。
1.定义dp数组的含义：dp[i][j] = x表示，戳破气球i和气球j之间（开区间，不包括i和j）的所有气球，可以获得的最高分数为x
2.那么根据这个定义，题目要求的结果就是dp[0][n+1]的值
3.其实气球i和气球j之间的所有气球都可能是最后被戳破的那一个，不防假设为k
4.根据对dp数组的定义，如果最后一个戳破气球k，dp[i][j]的值应该为
    dp[i][j] = dp[i][k] + dp[k][j] + points[i]*points[k]*points[j] (i<k<j)

dp[i][j]所依赖的状态是dp[i][k]和dp[k][j]，那么我们必须保证：
    在计算dp[i][j]时，dp[i][k]和dp[k][j]已经被计算出来了（其中i < k < j）

有两种遍历方法，要么斜着遍历，要么从下到上从左到右遍历：
           1 3 1 5 8 1   n = 4
        1  0
        3    0
        1      0
        5        0
        8          0
        1            0
        
"""

# todo 区间dp困难题

# dp遍历方法1：(推荐！)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 戳破nums所有气球，可以获得的最大分数
        new_nums = [1] + nums + [1]  # 原数组前后各加一个边界
        n = len(new_nums)
       
        # todo dp[i][j]代表戳破气球i和气球j之间（开区间，不包括i和j）的所有气球，可以获得的最高分数
        # 初始化：相邻气球之间的得分为0，dp[i][i+1] = 0
        # todo ​dp[i][j] = dp[i][k] + dp[k][j] + points[i]*points[k]*points[j], (i<k<j)
        # ​也就是说dp[i][j]依赖下一行的数据，后面循环是需要i从下往上遍历
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        # 最后要求的结果是dp[0][n+1]

        # todo 先按照左端点i从下到上, 在按照右端点j从左到右遍历（只遍历对角线右上部分）
        for i in range(n-1, -1, -1):  # i 从下往上
            for j in range(i + 2, n):  # j 从左往右
                for k in range(i + 1, j):  # k枚举new_nums(i..j)最后戳破的气球
                    dp[i][j] = max(dp[i][j],
                                   dp[i][k] + new_nums[i] * new_nums[k] * new_nums[j] + dp[k][j])
            print(dp)
        return dp[0][n + 1]




# dp遍历方法2: 先按照区间间隔个数gap从小到大，在按照左端点i从左到右遍历（斜着遍历）
class Solution2:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        new_nums = [1] + nums + [1]
        # print(new_nums)  # [1, 3, 1, 5, 8, 1]

        # dp[i][j]代表戳破气球i和气球j之间（开区间，不包括i和j）的所有气球，可以获得的最高分数
        # 第一维是左边界下标，第二维是右边界下标
        # dp[0][0] = 0  dp[-1][-1] = 0
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        # 先枚举[i..j]间隔
        for gap in range(2, n + 2):
            # i 是左边界
            for i in range(n + 2 - gap):
                #  j 是 i 和 L 确定的情况下，右边界
                j = i + gap
                # 枚举每一个位置
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j],
                                   dp[i][k] + new_nums[i] * new_nums[k] * new_nums[j] + dp[k][j])
            print(dp)
        return dp[0][n + 1]


"""
1.在 nums 数组的两端添加两个值为 1 的元素，表示虚拟的气球，方便处理边界情况。
2.创建一个二维数组 dp，dp[i][j] 表示在区间 (i, j) 内戳破气球所能获得的最大分数。
3.使用动态规划的思想，从小区间开始计算 dp 数组的值，逐渐扩大区间。
4.对于区间 (i, j)，遍历其中的每个位置 k，作为最后一个戳破的气球。计算 dp[i][j] 的值：
    - 通过遍历 k 来找到最后一个戳破的气球，戳破气球 k 的得分为 nums[i] * nums[k] * nums[j]。
    - 将区间 (i, k) 和 (k, j) 视为两个子问题，分别计算其最大分数，即 dp[i][k] 和 dp[k][j]。
    - 加上戳破气球 k 的得分，得到 dp[i][j] 的值。
5.根据动态规划的思路，需要先计算较小区间的最大分数，再逐渐扩大区间，直到计算出整个数组的最大分数 dp[0][n+1]，
  其中 n 是原始数组 nums 的长度。
"""

if __name__ == '__main__':
    nums = [3, 1, 5, 8]  # 167
    print(Solution().maxCoins(nums))
    # print(Solution2().maxCoins(nums))
