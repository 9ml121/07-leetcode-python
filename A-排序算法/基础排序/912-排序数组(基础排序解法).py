"""
给你一个整数数组 nums，请你将该数组升序排列。

示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]


提示：

1 <= nums.n <= 5 * 10^4
-5 * 10^4 <= nums[i] <= 5 * 10^4
"""

from typing import List


def selectionSort(nums):
    """1.选择排序算法:  稳定排序, 时间复杂度稳定为O(n^2), 不占用额外的内存空间, 简单直观
    1.首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
    2.再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    3.重复第二步，直到所有元素均排序完毕。
    """
    n = len(nums)
    # 1.在nums[i..n)中选出最小元素
    # todo 选择排序 循环不变量是: 区间nums[0..i)里保存了数组里最小的i个元素,并且按照升序排列
    # 这里左开右闭的好处是, i正好代表区间长度
    for i in range(n):
        minIdx = i  # 记录最小数索引
        for j in range(i + 1, n):
            if nums[j] < nums[minIdx]:
                minIdx = j
        # 2. i 不是最小数时，将 i 和最小数进行交换
        if minIdx != i:
            nums[i], nums[minIdx] = nums[minIdx], nums[i]
    return nums


def bubbleSort(nums):
    """2.冒泡排序算法: 重复走访要排序的数列，两两比较，如果顺序错误就交换过来。好像看书每次都从第一页开始往后翻。
    1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
    3.针对所有的元素重复以上的步骤，除了最后一个。
    4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
    """
    n = len(nums)
    for i in range(n - 1):
        # 注意：因为内循环是从下标1开始，跟前面一个数比较，外循环只用遍历n-1次,注意不是n!!
        # todo 小优化：如果内循环没有发生数据交换，证明数组已经有序，可以提前终止遍历
        isSorted = True
        for j in range(1, n - i):
            if nums[j - 1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                isSorted = False
        if isSorted:
            break
    return nums


def insertionSort(nums):
    """插入排序：1.插入排序作用在"接近有序"的数组上，效果是很好的；2.作用在规模较小的数组，效果较好
    1.通过构建"有序数组"，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
    - 插入排序：每一轮只需要跟前一个元素比较，有机会提前终止遍历
    - 选择排序：每一轮需"看完"剩下的还未排定的"所有元素"
    """
    # 把nums[i]插入有序数组nums[0..i-1]
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break
    return nums


def insertionSort2(nums) -> None:
    """插入排序优化：数据向后遍历时，将「逐个交换」改为「逐个赋值」，性能开销可以减小，但是时间复杂度不变
    """
    # 把nums[i]插入有序数组nums[0..i-1]
    for i in range(1, len(nums)):
        j = i
        curVal = nums[i]
        while j - 1 >= 0 and nums[j - 1] > curVal:  # 严格大于
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = curVal


def shellSort(nums) -> None:
    """希尔排序：调用分组插入排序(步长序列依次为n//2, n//4, n//8...1)
    """
    gap = len(nums) // 2  # 分组的步长序列,向下取整，保证
    while gap >= 1:
        for i in range(gap):
            gapInsertionSort(nums, i, gap)

        print(f'步长序列为:{gap}, nums: {nums}')
        gap = gap // 2


def gapInsertionSort(nums, start, gap) -> None:
    """分组插入排序, start表示开始索引,gap表示步长, 原地修改nums, 无返回值"""
    for i in range(start + gap, len(nums), gap):
        k = i
        curVal = nums[i]
        while k - gap >= 0 and nums[k - gap] > curVal:  # 严格大于
            nums[k] = nums[k - gap]
            k -= gap
        nums[k] = curVal


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # return selectionSort(nums)
        # return bubbleSort(nums)
        # return insertionSort(nums)
        # return insertionSort2(nums)
        shellSort(nums)
        return nums


if __name__ == '__main__':
    nums = [6, 2, 7, 4, 5, 8, 3, 9, 1, 0]
    print(nums)
    print(Solution().sortArray(nums))
