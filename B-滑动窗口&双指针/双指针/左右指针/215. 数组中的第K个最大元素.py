"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1:
输入: [3,2,1,5,6,4], k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4


提示：
1 <= k <= nums.n <= 10^5
-10^4 <= nums[i] <= 10^4
"""
from typing import List
import random


# todo 使用快速排序的partition方法（O(N)） 最优解！！
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """查找数组中第 K个最大元素, 时间复杂度为 O(n) 的算法"""
        n = len(nums)
        l = 0
        r = n - 1

        # 第k大元素在升序数组下标为n - k
        target = n - k

        while l <= r:
            i = self.partition(nums, l, r)
            if i == target:
                return nums[i]
            elif i > target:
                # 下一轮搜索区间：[l..pivot_idx-1]
                r = i - 1
            else:
                # pivot_idx < target: 下一轮搜索区间[pivot_idx + 1..right]
                l = i + 1

    # todo 循环不变量定义 1：把等于切分元素的所有元素分到了数组的同一侧。（测试用例大量重复元素会超时）
    def partition(self, nums:list, l:int, r:int) -> int:
        """在nums[l..r]中随机选一个数pivot，通过双路快排，找到它在有序数组第几位
        """
        # 基准值选中间值（或者随机）
        # pivot_idx = random.randint(l, r)
        pivot_idx = (l+r) >> 1
        nums[l], nums[pivot_idx] = nums[pivot_idx], nums[l]
        pivot = nums[l]

        # 定义 pivot = nums[left] ，剩下的区间[left + 1..right] 被变量 le 分成2个部分：
        # [l..le] <= pivot
        # (le..r] > pivot
        le = l
        for i in range(l+1, r+1):
            if nums[i] <= pivot:
                le += 1
                nums[le], nums[i] = nums[i], nums[le]
        
        # 不要忘了交换nums[l],也就是pivot        
        nums[l], nums[le] = nums[le], nums[l]        
        return le

    # todo 循环不变量定义 2：把等于切分元素的所有元素 等概率 地分到了数组的两侧，避免了递归树倾斜，递归树相对平衡。
    def partition2(self, nums: list, l: int, r: int) -> int:
        """在nums[l..r]中随机选一个数pivot，通过双路快排，找到它在有序数组第几位
        """
        # 基准值选中间值（或者随机）
        # pivot_idx = random.randint(l, r)
        pivot_idx = (l+r) >> 1
        nums[l], nums[pivot_idx] = nums[pivot_idx], nums[l]
        pivot = nums[l]

        # 定义 pivot = nums[left] ，剩下的区间[left + 1..right] 被变量 le, ge 分成2个部分：
        # [l..le) <= pivot
        # (ge..r] >= pivot
        # [ge..le]是程序没有看到的 
        le = l+1
        ge = r
        while True:
            while le <= ge and nums[le] < pivot:
                le += 1
            while le <= ge and nums[ge] > pivot:
                ge -= 1
            if le > ge:
                break
            
            nums[le], nums[ge] = nums[ge], nums[le]
            le += 1
            ge -= 1
            
        # 不要忘了交换nums[l],也就是pivot，注意这里是ge
        nums[l], nums[ge] = nums[ge], nums[l]
        return ge

    # 循环不变量定义 3：把等于切分元素的所有元素挤到了数组的中间，在有很多元素和切分元素相等的情况下，递归区间大大减少。
    # 这一版代码稍显麻烦，大家了解即可
    
if __name__ == '__main__':
    s = Solution()
    nums = [5, 1, 5, 7, 6, 5, 4]
    k = 2
    print(s.findKthLargest(nums, k))
    # print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
