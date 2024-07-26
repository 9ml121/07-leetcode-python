"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。


示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。


提示：
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

from typing import List


# todo 方法1：动态规划（记忆化搜索）  爬楼梯换皮题
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 不能偷相邻房间，问可以偷盗的最大金额
        n = len(nums)

        # todo f[i] 表示偷取到nums[i-2]个房屋能够获得的最大金额, f[2]之前的2个数字是初始化值
        f = [0] * (n+2)
        
        # 偷取第 i 个房屋时，有两种情况：
        # - 偷取第 i 个房屋的金额，即 f[i-2] + nums[i]。
        # - 不偷取第 i 个房屋的金额，即 f[i-1]。
        for i, x in enumerate(nums):
            # 选择两种情况中的较大值作为偷取第 i 个房屋时能够获得的最大金额
            f[i+2] = max(f[i], f[i+1]+x)

        # 返回 dp[-1]，即偷取到最后一个房屋能够获得的最大金额
        return f[-1]


    # todo dp状态转移只依赖前2个位置值，可以将dp空间压缩为2个常量(推荐！)
    def rob(self, nums: List[int]) -> int:
        # 不能偷相邻房间，问可以偷盗的最大金额
        f1 = 0  # 前1个房间
        f2 = 0  # 前2个房间
        for x in nums:
            # 当前房间可以获得的最大金额
            cur = max(f1, f2 + x)
            f2 = f1
            f1 = cur

        return f1


# todo 方法2：递归（记忆化递推）
# 1.dfs -> f数组
# 2.递归 -> 循环
# 3.递归边界 -> f数组初始化
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 不能偷相邻房间，问可以偷盗的最大金额
        from functools import cache
        n = len(nums)
        
        @cache
        def dfs(i:int)->int:
            if i < 0:
                return 0
            
            res = max(dfs(i-1), dfs(i-2) + nums[i])
            return res

        return dfs(n-1)