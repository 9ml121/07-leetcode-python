from typing import List


def selectionSort(nums: List[int]) -> List[int]:
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

        # 调试
        # print(nums)
    return nums


if __name__ == '__main__':
    nums = [2, 3, 1, 4, 6, 5, 7, 8, 9, 10]
    print(selectionSort(nums))
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
