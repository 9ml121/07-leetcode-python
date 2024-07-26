"""
给定一个整数数组  nums，处理以下类型的多个查询:
计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right

实现 NumArray 类：
NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 中索引 left 和 right 之间的元素的 总和 ，
包含 left 和 right 两点（也就是 nums[left] + nums[left + 1] + ... + nums[right] )


示例 1：
输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]

解释：
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))


提示：
1 <= nums.n <= 104
-105 <= nums[i] <= 105
0 <= i <= j < nums.n
最多调用 104 次 sumRange 方法!!!
"""
from typing import List

# todo 前缀和主要适用的场景是原始数组不会被修改的情况下，频繁查询某个区间的累加和。
'''
prefix[i] 就代表着 nums[0..i-1] 所有元素的累加和，
如果我们想求区间 nums[i..j] 的累加和，
只要计算 prefix[j+1] - prefix[i] 即可，而不需要遍历整个区间求和。
'''


class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        # 前缀和数组:
        # 1. preSum[i]代表nums[0..i)的累加和，这里累加和不包括nums[i]
        # 2. 一般前缀和数组长度比nums长度多一位，初始化preSum[0] = 0，代表nums第一位前缀和为0
        self.preSum = [0] * (n + 1)
        
        for i in range(1, n + 1):
            #  3. preSum
            self.preSum[i] = nums[i - 1] + self.preSum[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        # 查询闭区间 [left, right] 的累加和
        res = self.preSum[right + 1] - self.preSum[left]
        return res




# 求数组累加和写法1：
def preSum1(nums:list):
    preSum = [0]
    for i, x in enumerate(nums):
        preSum.append(preSum[i] + x)
    print(preSum)




# 求数组累加和写法2：
def preSum2(nums):
    n = len(nums)
    preSum = [0] * (n + 1)
    for i in range(1, n + 1):
        preSum[i] = nums[i - 1] + preSum[i - 1]
    print(preSum)

