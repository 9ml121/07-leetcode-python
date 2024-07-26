from typing import List


def bubbleSort(nums: List[int]) -> List[int]:
    """2.冒泡排序算法: 重复走访要排序的数列，两两比较，如果顺序错误就交换过来。好像看书每次都从第一页开始往后翻。
    1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
    3.针对所有的元素重复以上的步骤，除了最后一个。
    4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
    """
    n = len(nums)
    for i in range(n - 1):
        # 注意：因为内循环是从下标1开始，跟前面一个数比较，外循环只用遍历n-1次,注意不是n!!
        isSorted = True
        # 确定最后的元素是[0..n-i]最大数
        for j in range(1, n - i):
            if nums[j - 1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                isSorted = False
        # todo 小优化：如果内循环没有发生数据交换，证明数组已经有序，可以提前终止遍历
        if isSorted:
            break
        # 调试
        print(f'第{i}轮排序的结果：{nums}')
    return nums


if __name__ == '__main__':
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(bubbleSort(nums))
