"""
leetcode912题：排序数组
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


# 非负整数的桶排序代码实现
class BucketSort:
    def sort(self, nums):
        max_num = 0
        # 第 1 步：找到数组中的最大值，以确定计数数组的长度
        for num in nums:
            if num < 0:
                raise ValueError("该数组不适合使用计数排序")
            max_num = max(max_num, num)

        # 第 2 步：计算出最大的数字有几位，这个数值决定了桶的个数
        max_len = self.get_max_len(max_num)
        # 步长
        step = 1000
        # 决定设置几个桶
        if max_len < 5:
            # 如果最大数小于 10000
            # 3 位数就设置 100 个桶
            # 2 位数就设置 10 个桶
            step = 10 ** (max_len - 1)
        # 桶的个数
        bucket_len = max_num // step + 1
        # 因为不能确定每个桶存放的数据量，因此每个桶的长度都设置为 len
        temp = [[] for _ in range(bucket_len)]
        # next 数组记录的是每个桶下一次放入元素的下标（索引）。
        next_index = [0 for _ in range(bucket_len)]

        # 第 3 步：分桶
        for num in nums:
            # 找到所在的桶的索引
            bucket_index = num // step
            # 在该桶中放入元素
            temp[bucket_index].append(num)
            # 该桶存放的元素个数 + 1
            next_index[bucket_index] += 1

        # 第 4 步：对于每个桶执行插入排序
        for i in range(bucket_len):
            self.insertion_sort(temp[i], next_index[i] - 1)

        # 第 5 步：从桶里依次取出来
        index = 0
        for i in range(bucket_len):
            cur_len = next_index[i]
            for j in range(cur_len):
                nums[index] = temp[i][j]
                index += 1
        return nums

    def insertion_sort(self, arr, end_index):
        for i in range(1, end_index + 1):
            temp = arr[i]
            j = i
            while j > 0 and arr[j - 1] > temp:
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = temp

    # 获取一个整数的最大位数
    def get_max_len(self, num):
        max_len = 0
        while num > 0:
            num //= 10
            max_len += 1
        return max_len


# 桶排序，考虑到负数
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.bucketSort(nums)

    def bucketSort(self, nums):
        # 获取最大值和最小值
        max_val = max(nums)
        min_val = min(nums)
        # 计算桶的数量,这里可以自由确定
        bucket_size = (max_val - min_val) // len(nums) + 1
        # 创建桶
        buckets = [[] for _ in range(bucket_size)]
        # 将元素放入对应的桶中
        for num in nums:
            index = (num - min_val) // len(nums)
            buckets[index].append(num)
        # 对每个桶进行排序
        for bucket in buckets:
            bucket.sort()
        # 合并所有桶的元素
        sorted_nums = []
        for bucket in buckets:
            sorted_nums.extend(bucket)
        return sorted_nums


# 桶排序：考虑负数,考虑小数
# 「力扣」上不会单独考「计数排序」、「基数排序」、「桶排序」，但有一些问题是基于「桶」的思想得以解决的。
class Solution2:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.bucket_sort(nums)

    # 桶排序算法
    def bucket_sort(self, arr):
        # 1.得到数列的最大值和最小值，算出差值d
        max_val = max(arr)
        min_val = min(arr)
        diff = max_val - min_val

        # 2.初始化桶（确定桶的数量）
        bucketNum = len(arr)  # 桶的数量为数组长度，这里可以自由确定
        bucketList = [[] for _ in range(bucketNum)]  # bucketList[i]表示第i个桶内元素集合

        # 3.遍历原始数组，将元素放入桶中（涉及到double和int的转换）
        for num in arr:
            step = diff / (bucketNum - 1)  # 每个桶的范围（步长），注意最后一个桶是[max,max]
            idx = int((num - min_val) / step)  # 确定元素在第几个桶（桶排序的难点，主要是画图明白桶的个数及范围）
            bucketList[idx].append(num)  # 将元素添加到对应桶里

        # 4.桶内部的元素进行排序（桶排序算法是否稳定取决于这里的排序算法）
        for i in range(bucketNum):
            bucketList[i].sort()  # python采用归并排序，时间复杂度O(nlogn)空间复杂度O(n)

        # 5.输出全部元素并返回排序后的新数组（不是基于交换，而是重新赋值到一个新的数组）
        sortedArr = []  # 不是基于交换的排序
        for sublist in bucketList:  # 集合最简单的遍历方式
            for element in sublist:
                sortedArr.append(element)

        return sortedArr


if __name__ == '__main__':
    solution = Solution()
    # 测试示例
    nums = [9, 0, 15, 12, 3, -1, 5, -2]
    sorted_nums = solution.bucketSort(nums)
    print("排序结果：", sorted_nums)

    arr = [12, 45, 345, 22]
    print("排序结果：", BucketSort().sort(arr))
