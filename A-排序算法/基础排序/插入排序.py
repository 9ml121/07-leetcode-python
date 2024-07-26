from typing import List


# 插入排序：逐个交换的写法
# 第 1 版实现：逐个交换到前面合适的位置
def insertionSort(nums: List[int]) -> List[int]:
    """插入排序：1.插入排序作用在"接近有序"的数组上，效果是很好的；2.作用在规模较小的数组，效果较好
    1.通过构建"有序数组"，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
    - 插入排序：每一轮只需要跟前一个元素比较，有机会提前终止遍历
    - 选择排序：每一轮需"看完"剩下的还未排定的"所有元素"
    """
    # 把nums[i]插入有序数组nums[0..i-1]
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            # 注意：前面的数严格大于后面的数才交换
            if nums[j - 1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            # 注意：「插入排序」可以提前终止内层循环，体现在 nums[j - 1] > temp 不满足时。
            else:
                break
    return nums


# 插入排序：逐个赋值的写法
# 第 2 版实现：先暂存当前变量，然后将前面的若干个元素逐个向后赋值
def insertionSort2(nums: List[int]) -> List[int]:
    """插入排序优化：数据向后遍历时，将「逐个交换」改为「逐个赋值」，性能开销可以减小，但是时间复杂度不变
    """
    # 循环不变量：将 nums[i] 插入到区间 [0..i) 使之成为有序数组
    for i in range(1, len(nums)):
        j = i
        # 先暂存这个元素，然后之前元素逐个后移，留出空位
        temp = nums[i]
        # 注意边界 j-1 >= 0
        while j - 1 >= 0 and nums[j - 1] > temp:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = temp
    return nums


if __name__ == '__main__':
    nums = [1, 4, 3, 2, 5, 6, 7, 8, 9, 10]
    print(insertionSort(nums))
    print(insertionSort2(nums))
