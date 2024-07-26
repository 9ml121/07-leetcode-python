"""
给定一个整数数组 arr ，返回 arr 的 最大湍流子数组的长度 。

如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是 湍流子数组 。

更正式地来说，当 arr 的子数组 A[i], A[i+1], ..., A[j] 满足仅满足下列条件时，我们称其为湍流子数组：

若 i <= k < j ：
当 k 为奇数时， A[k] > A[k+1]，且
当 k 为偶数时，A[k] < A[k+1]；
或 若 i <= k < j ：
当 k 为偶数时，A[k] > A[k+1] ，且
当 k 为奇数时， A[k] < A[k+1]。
 

示例 1：

输入：arr = [9,4,2,10,7,8,8,1,9]
输出：5
解释：arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
示例 2：

输入：arr = [4,8,12,16]
输出：2
示例 3：

输入：arr = [100]
输出：1
 

提示：

1 <= arr.length <= 4 * 104
0 <= arr[i] <= 109
"""

# todo 方法1：无固定长度滑窗
class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        # 返回arr最长最大湍流子数组的长度
        n = len(arr)
        if n <= 1:
            return n
        ans = 1

        # [l..r]符合湍流子数组性质
        # pre = True: 表示arr[i-1] > arr[i]
        pre = True
        l = 0
        for r in range(1, n):
            cur = arr[r-1] > arr[r]
            if cur == pre:
                # [l..r]严格单调递增或递减，需要重置l在r前一位
                l = r-1
            if arr[r-1] == arr[r]:
                # 相邻元素相同，需要重置l在r当前位置
                l = r

            # 更新ans和pre
            ans = max(ans, r-l+1)
            pre = cur

        return ans

# todo 方法2：动态规划，多状态dp
class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        # 返回arr的最大湍流子数组长度
        ans = 0
        n = len(arr)
        if n <= 1:
            return n

        # 以 arr[i] 结尾，并且 arr[i - 1] < arr[i] 的湍流子数组的长度
        dp_inc = [0] * n
        # 以 arr[i] 结尾，并且 arr[i - 1] > arr[i] 的湍流子数组的长度
        dp_dec = [0] * n

        # 初始化
        dp_inc[0] = dp_dec[0] = 1
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                dp_dec[i] = dp_inc[i-1] + 1
                dp_inc[i] = 1
            elif arr[i-1] < arr[i]:
                dp_inc[i] = dp_dec[i-1] + 1
                dp_dec[i] = 1
            else:
                dp_inc[i] = 1
                dp_dec[i] = 1

            ans = max(ans, max(dp_dec[i], dp_inc[i]))

        return ans
