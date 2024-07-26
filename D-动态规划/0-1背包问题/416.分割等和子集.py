"""
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。

示例 2：
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。


提示：
1 <= nums.n <= 200
1 <= nums[i] <= 100
"""
from typing import List

"""
# 是否可以将这个数组分割成两个子集，使得两个子集的元素和相等?
# 问题等价于从数组取部分元素，是否可以满足其和==sum(nums)//2？
# todo 装换为01背包问题就是：
# 给一个可装载重量为 sum / 2 的背包和 n 个物品，每个物品的重量为 nums[i]。
# 现在让你装物品，是否存在一种装法，能够恰好将背包装满？
"""


# 方法1：dp用二维数组
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumV = sum(nums)
        # 如果sumv是奇数，无解
        if sumV % 2 != 0:
            return False
        # 1 <= nums[i] <= 100

        w = sumV // 2  # 需要恰好装满的重量
        n = len(nums)  # 物品数量
        # todo dp[i][j]代表前i个物品，能不能装满容量为j的背包
        dp = [[False] * (w + 1) for _ in range(n)]

        # base case:背包重量=0  不用装背包已经满了
        for i in range(n):
            dp[i][0] = True
        # 这里写成 dp[0][0] = true 也可以

        # 将物品nums[i]依次取出
        for i in range(n):
            for j in range(1, w + 1):
                # 1. 不选：把上一行照抄下来
                dp[i][j] = dp[i - 1][j]
                # 2. 选：二者之中有一个为 true 即可
                if nums[i] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]

        # print(dp)
        return dp[-1][-1]


# 优化1：注意到状态转移的特殊性，如果某一行最后一列为 true，最后一行最后一列一定为 true，可以提前终止程序。
class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        sumV = sum(nums)
        if sumV % 2 != 0:
            return False

        target = sumV // 2  # 需要恰好装满的重量
        n = len(nums)  # 物品数量
        # todo dp[i][j]代表前i个物品，能不能装满容量为w的背包
        dp = [[False] * (target + 1) for _ in range(n)]

        # base case:背包重量=0  不用装背包已经满了!!!
        for i in range(n):
            dp[i][0] = True

        # 将物品nums[i]依次取出
        for i in range(n):
            for j in range(1, target + 1):
                # 1. 不选：把上一行照抄下来
                dp[i][j] = dp[i - 1][j]
                # 2. 选：二者之中有一个为 true 即可
                if nums[i] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]

                # 如果某一行最后一列为 true，最后一行最后一列一定为 true，提前终止程序
                if dp[i][target]:
                    return True

        return dp[-1][-1]


# 优化2：空间压缩优化：dp[i][j] 都是通过上一行 dp[i-1][..] 转移过来的，之前的数据都不会再使用了。
# 根据「0-1 背包」问题表格复用的优化方法，我们可以采用「逆序填表」的方式将空间复杂度优化到 O(target)。
class Solution3:
    def canPartition(self, nums: List[int]) -> bool:
        sumV = sum(nums)
        if sumV % 2 != 0:
            return False
        n = len(nums)
        target = sumV // 2
        dp = [False] * (target + 1)

        # base case
        dp[0] = True
        for i in range(n):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]

                if dp[target]:
                    return True

        return dp[target]


if __name__ == '__main__':
    # nums = [1, 5, 11, 5]
    nums = [1, 2, 3, 6]
    print(Solution().canPartition(nums))
    print(Solution2().canPartition(nums))

'''
        0       1     2     3     4       5       6       7       8      9    10     11
0   [[True, False, False, False, False, False, False, False, False, False, False, False], 
1    [True, True, False, False, False, False, False, False, False, False, False, False], 
5    [True, True, False, False, False, True, True, False, False, False, False, False], 
11   [True, True, False, False, False, True, True, False, False, False, False, True], 
5    [True, True, False, False, False, True, True, False, False, False, True, True]]

        0   1       2       3       4       5   6
0   [[True, False, False, False, False, False, False], 
1    [True, True, False, False, False, False, False], 
2    [True, True, True, True, False, False, False], 
3    [True, True, True, True, True, True, True], 
6    [True, True, True, True, True, True, True]]

'''
