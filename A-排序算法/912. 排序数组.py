"""
给你一个整数数组 nums，请你将该数组升序排列。

 

示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
 

提示：

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""


from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 方法1：快排（分治递归，非原地排序写法）
        def quick_sort(nums):
            # 1.递归返回条件
            if len(nums) <= 1:
                return nums

            # 2.确定基准值，递归排序小于基准值和大于基准值的数组，返回升序排序数组
            pivot = nums[len(nums)//2]
            left = [x for x in nums if x < pivot]
            mid = [x for x in nums if x == pivot]
            right = [x for x in nums if x > pivot]

            return quick_sort(left) + mid + quick_sort(right)

        # 方法2：归并排序（分治递归，非原地排序写法）
        def merge(left: list, right: list):
            # 合并2个有序数组
            merged = []
            l_idx, r_idx = 0, 0
            # 1.同时遍历2个有序数组，取当前较小值添加到合并数组merged
            while l_idx < len(left) and r_idx < len(right):
                if left[l_idx] <= right[r_idx]:
                    merged.append(left[l_idx])
                    l_idx += 1
                else:
                    merged.append(right[r_idx])
                    r_idx += 1

            # 2.再将2个数组剩余元素添加到merged
            merged.extend(left[l_idx:])
            merged.extend(right[r_idx:])

            return merged

        def merge_sort(nums):
            # 1. 递归返回条件
            if len(nums) <= 1:
                return nums

            # 2. 递归将数组从中间一分为二，返回合并2个有序数组之后的数组
            mid = len(nums)//2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            return merge(left, right)

        # 方法3：插入排序（原地排序，适用于接近有序数组排序）
        def insert_sort(nums):
            # 通过构建有序数列，对于未排序的数列，在已排序的数列中从后向前扫描，找到相应位置并插入
            for i in range(1, len(nums)):
                # 1.循环不变量：nums[0..i]是升序数组
                # 2.在nums[0..i-1]中找到插入nums[i]的位置下标(基于元素交换和赋值2种方法实现)
                for j in range(i, 0, -1):
                    if nums[j] < nums[j-1]:
                        nums[j], nums[j-1] = nums[j-1], nums[j]
                    else:
                        break

            return nums

        # 方法4：选择排序(原地排序，最直观, 时间复杂度也最高)
        def select_sort(nums):
            # 不断选择剩余元素中的最小元素，放到已排序序列的末尾
            for i in range(len(nums)):
                min_idx = i
                for j in range(i+1, len(nums)):
                    if nums[j] < nums[min_idx]:
                        min_idx = j
                # 交换i, min_idx对应的元素
                nums[i], nums[min_idx] = nums[min_idx], nums[i]
            return nums

     

        # 方法5：冒泡排序(适用于接近有序的数组排序)
        def bubble_sort(nums):
            # 重复遍历要排序的数列，一次比较2个元素。如果他们顺序错误就交换位置，直到没有再需要交换的元素
            n = len(nums)
            for i in range(n):
                swap = False
                # 循环不变量：nums[n-1-i..n)是有序的
                for j in range(n-1-i):
                    if nums[j] > nums[j+1]:
                        swap = True
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                if not swap:
                    break
            return nums

        # return bubble_sort(nums)
