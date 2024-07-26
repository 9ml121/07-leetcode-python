"""
给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value ，使得将数组中所有大于 value 的值变成 value 后，数组的和最接近  target （最接近表示两者之差的绝对值最小）。

如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。

请注意，答案不一定是 arr 中的数字。



示例 1：

输入：arr = [4,9,3], target = 10
输出：3
解释：当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。
示例 2：

输入：arr = [2,3,5], target = 10
输出：5
示例 3：

输入：arr = [60864,25176,27249,21296,20204], target = 56803
输出：11361


提示：

1 <= arr.length <= 10^4
1 <= arr[i], target <= 10^5
"""
from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        """转变数组后最接近目标值的数组和
        如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。
        """

        # 注意，答案不一定是 arr 中的数字。所以这个最小值应该设置为0，而不是min(arr)
        # 也就是说可能解在[0..max(arr)]
        lo, hi = 0, max(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            # mid越小，sumArr越小
            sumArr = self.getSum(arr, mid)
            # 计算第 1 个使得转变后数组的和大于等于 target 的阈值 threshold
            if sumArr < target:
                # 严格小于的一定不是解
                lo = mid + 1
            else:
                hi = mid

        # 比较阈值线分别定在 l0 - 1 和 lo 的时候与 target 的接近程度
        sum1 = self.getSum(arr, lo)
        sum2 = self.getSum(arr, lo - 1)
        if target - sum2 <= sum1 - target:
            return lo - 1
        return lo

    def getSum(self, arr, val) -> int:
        """返回数组arr中所有大于 value 的值变成 value 后，数组的和"""
        return sum(min(elem, val) for elem in arr)
