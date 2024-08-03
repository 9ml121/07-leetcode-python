"""
给你一个整数数组，返回它的某个 非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。
换句话说，你可以从原数组中选出一个子数组，并可以决定要不要从中删除一个元素（只能删一次哦），（删除后）子数组中至少应当有一个元素，然后该子数组（剩下）的元素总和是所有子数组之中最大的。

注意，删除一个元素后，子数组 不能为空。

 
示例 1：
输入：arr = [1,-2,0,3]
输出：4
解释：我们可以选出 [1, -2, 0, 3]，然后删掉 -2，这样得到 [1, 0, 3]，和最大。

示例 2：
输入：arr = [1,-2,-2,3]
输出：3
解释：我们直接选出 [3]，这就是最大和。

示例 3：
输入：arr = [-1,-1,-1,-1]
输出：-1
解释：最后得到的子数组不能为空，所以我们不能选择 [-1] 并从中删去 -1 来得到 0。
     我们应该直接选择 [-1]，或者选择 [-1, -1] 再从中删去一个 -1。
 

提示：
1 <= arr.length <= 10^5
-10^4 <= arr[i] <= 10^4
"""



from functools import cache
from math import inf
from typing import List

# todo 方法1：前后缀分解  （推荐！）
class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        # 返回arr的某个 非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和
        n = len(arr)
        # 1.预处理: 数组 arr 以每个元素结尾和开头的最大子数组和，分别存入数组 left 和 right 中。
        left = [0] * n
        right = [0] * n
        s = 0
        for i, x in enumerate(arr):
            s = max(s, 0) + x
            left[i] = s
            
        s = 0
        for i in range(n - 1, -1, -1):
            s = max(s, 0) + arr[i]
            right[i] = s
        
        # 2.如果我们不删除任何元素，那么最大子数组和就是 left[i] 或 right[i] 中的最大值；
        # 如果我们删除一个元素，我们可以枚举[1..n−2] 中的每个位置 i，计算 left[i−1]+right[i+1] 的值，取最大值即可。
        ans = max(left)
        for i in range(1, n - 1):
            ans = max(ans, left[i - 1] + right[i + 1])
        return ans

# todo 方法2: dfs ==> 状态机dp
# https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/solutions/2321829/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-hzz6
# 
# 递归 + 记录返回值 = 记忆化搜索
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # 返回arr的某个 非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和
        
        # todo dfs(i,j) 表示子数组的右端点是 arr[i]，不能(j=0)/必须删除(j=1)数字的两种情况下，子数组元素和的最大值。
        @cache  # 记忆化搜索
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return -inf  # 子数组至少要有一个数，不合法
            
            if j == 0:
                # 不能删除数字
                return max(dfs(i - 1, 0), 0) + arr[i]
            else:
                # j==1: 必须删除一个数字
                return max(dfs(i - 1, 1) + arr[i], dfs(i - 1, 0))
        
        # 枚举arr每个位置作为子数组的右端点，统计所有位置可以得到的最大元素和
        return max(max(dfs(i, 0), dfs(i, 1)) for i in range(len(arr)))

# 1:1 翻译成递推(状态dp)
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # 返回arr的某个 非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和
        
        # todo f[i]代表以arr[i-1]作为子数组的右端点，不能(j=0)/必须删除(j=1)数字的两种情况下，子数组元素和的最大值。
        f = [[-inf] * 2] + [[0, 0] for _ in arr]
        for i, x in enumerate(arr):
            # 不能删除数字
            f[i + 1][0] = max(f[i][0], 0) + x
            # 必须删除1个数字
            f[i + 1][1] = max(f[i][1] + x, f[i][0])
        
        # 最后结果取dp数组中两种状态的最大值
        return max(max(r) for r in f)

# dp空间优化
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # 返回arr的某个 非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和
        
        # todo dp数组状态转移只依赖前一个位置结果，因此可以压缩为2个常量
        # f0和f1分别代表以前一个位置作为右端点，不能(j=0)/必须删除(j=1)数字的两种情况下，子数组元素和的最大值。
        ans = f0 = f1 = -inf
        
        for x in arr:
            # 注意：f1和f0赋值顺序不能改变
            f1 = max(f1 + x, f0)  
            f0 = max(f0, 0) + x
            ans = max(ans, f0, f1)
            
        return ans


