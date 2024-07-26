"""
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。


示例 1：
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。

示例 2：
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。

示例 3：
输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。


提示：
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-10^9 <= nums1[i], nums2[j] <= 10^9


进阶：你可以设计实现一个时间复杂度为 O(m + n) 的算法解决此问题吗？
"""
from typing import List

# todo 归并排序：合并2个有序数组
class Solution:
    # 正向合并：将 nums1 的前 m 个数组放到另一个数组中避免写指针写入的干扰。 这样空间复杂度就是 $O(m)$
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列
        m 和 n 分别表示 nums1 和 nums2 中的元素数目
        """
        temp = nums1[:m]
        # i指向 temp, j指向 nums2, k指向 nums1
        i, j = 0, 0
        for k in range(m + n):
            if i == m:
                # 只剩 nums2
                nums1[k] = nums2[j]
                j += 1
            elif j == n:
                # 只剩 temp
                nums1[k] = temp[i]
                i += 1
            # 比较两个数组的头元素，然后将较小的推到最终的数组中
            elif temp[i] <= nums2[j]:
                nums1[k] = temp[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1

    # todo 合并逻辑代码优化：从后往前比较，并从后往前插入，这样可避免写指针影响，同时将空间复杂度降低到 $O(1)$
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列
        m 和 n 分别表示 nums1 和 nums2 中的元素数目
        """
        # k指向合并后的结果列表最后一个元素
        k = m + n - 1
        # 从后向前生成结果数组，类似合并两个有序链表的逻辑
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[k] = nums1[m-1]
                m -= 1
            else:
                nums1[k] = nums2[n-1]
                n -= 1
            k -= 1

        # 可能其中一个数组的指针走到尽头了，而另一个还没走完
        # 因为我们本身就是在往 nums1 中放元素，所以只需考虑 nums2 是否剩元素即可
        while n > 0:
            nums1[k] = nums2[n-1]
            n -= 1
            k -= 1


