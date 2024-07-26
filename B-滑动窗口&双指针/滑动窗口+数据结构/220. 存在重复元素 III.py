"""
给你一个整数数组 nums 和两个整数 indexDiff 和 valueDiff 。

找出满足下述条件的下标对 (i, j)：
1. i != j,
2. abs(i - j) <= indexDiff
3. abs(nums[i] - nums[j]) <= valueDiff

如果存在，返回 true ；否则，返回 false 。


示例 1：
输入：nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
输出：true
解释：可以找出 (i, j) = (0, 3) 。
满足下述 3 个条件：
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0

示例 2：
输入：nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
输出：false
解释：尝试所有可能的下标对 (i, j) ，均无法满足这 3 个条件，因此返回 false 。

"""
from typing import List

"""
一个朴素的想法是每次遍历到任意位置 i 的时候，往后检查 k 个元素，但这样做的复杂度是 O(nk) 的，会超时。
显然我们需要优化「检查后面 k 个元素」这一过程。
我们希望使用一个「有序集合」去维护长度为 k 的滑动窗口内的数，该数据结构最好支持高效「查询」与「插入/删除」操作：
1.查询：能够在「有序集合」中应用「二分查找」，快速找到「小于等于 u 的最大值」和「大于等于 u 的最小值」
  （即「有序集合」中的最接近 u 的数）。
2.插入/删除：在往「有序集合」添加或删除元素时，能够在低于线性的复杂度内完成（维持有序特性）。
"""


# 方法 1：暴力解法，时间复杂度 O(N^2), 超时
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # 判断nums是否可以找到2个不同下标，满足下标绝对差值<=indexDiff, 下标元素绝对差值<=valueDiff
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, i + indexDiff + 1):
                if j > n - 1:
                    break
                if abs(nums[j] - nums[i]) <= valueDiff:
                    return True
        return False


# todo 方法 2：不定长滑窗 + 有序集合 sortedcontainers.SortedList() 红黑树 + 二分查找  O(NlogK)
# 我们需要在大小为 indexDiff 的滑动窗口所在的「有序集合」中找到与 num 接近的数。
# 当「查询」动作和「插入/删除」动作频率相当时，更好的选择是使用「红黑树」
# TreeSet 基于红黑树，查找和插入都是 O(logk) 复杂度, python语言是 sortedList
class Solution2:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        import sortedcontainers
        # 判断nums是否可以找到2个不同下标，满足下标绝对差值<=indexDiff, 下标元素绝对差值<=valueDiff
        # todo 有序列表SortedList用来维护窗口元素有序，方便O(log(N))时间查找某个元素
        window = sortedcontainers.SortedList()  # 红黑树, len(window) <= indexDiff

        for i, num in enumerate(nums):
            # 1.出：如果有序集合的大小超过了 indexDiff，移除窗口最左边的元素
            if i >= indexDiff + 1:
                window.remove(nums[i-indexDiff-1])  # 红黑树删除

            # 2.入
            window.add(num)  # 红黑树插入
            idx = window.bisect_left(num)  # 红黑树查找：从有序集合中找到第一个大于等于 num 的元素

            # 3.验证num在有序列表中左右 2 个元素的差值
            if idx > 0 and abs(window[idx] - window[idx - 1]) <= valueDiff:
                return True
            if idx < len(window) - 1 and abs(window[idx + 1] - window[idx]) <= valueDiff:
                return True

        return False


"""
除了使用有序集合（如SortedSet）之外，还有一种性能更好的解法可以解决这个问题，即使用桶排序（Bucket Sort）的思想。

解题思路如下：
1.将每个元素按照大小范围分配到不同的桶中。
    - 每个桶的大小为valueDiff + 1，即将nums[i]映射到桶的索引为nums[i] // (valueDiff +1)。
    - 为什么桶 size 要 + 1? 目的是为了确保差值小于等于 valueDiff 的数能够落到一个桶中。 
    - 比如 nums = [0,1,2,3] valueDiff = 3, 显然四个数都应该落在同一个桶， 如果不加 1， num = 3 会落在第二个桶
    - 数组被分割成： 0 1 2 3 | 4 5 6 7 | 8 9 10 11 | 12 13 14 15 | …
    - 注意：如果 nums元素为负数，python语言对于负数整除是向下取整，上面公式也是满足的。
    --比如 nums = [-1,-2,-3,-4] valueDiff = 3,  -1//4=-1, -4//4==-1
2.维护一个大小为 indexDiff 的滑动窗口，检查当前元素所属的桶以及相邻的桶中是否存在满足条件的元素。
3.如果满足条件，返回True；如果遍历完数组后仍未找到满足条件的元素，返回False。

这种方法的时间复杂度为O(n)，其中n为数组的长度。
"""


# 方法 3：桶排序
class Solution3:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {}
        bucket_size = valueDiff + 1

        for i, num in enumerate(nums):
            # 计算当前元素所属的桶索引
            bucket_idx = num // bucket_size

            # 检查当前桶中是否存在元素满足条件
            if bucket_idx in buckets:
                return True

            # 检查相邻桶中是否存在元素满足条件
            left, right = bucket_idx - 1, bucket_idx + 1
            if left in buckets and abs(num - buckets[left]) <= valueDiff:
                return True
            if right in buckets and abs(num - buckets[right]) <= valueDiff:
                return True

            # 将当前元素添加到桶中
            buckets[bucket_idx] = num

            # 移除窗口最左边的元素
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // bucket_size]

        return False
