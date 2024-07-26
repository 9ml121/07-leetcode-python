from sorting.examples import GenerateRandomArrayStrategy
from sorting.sorting_util import SortingUtil


# 归并排序第一版
class MergeSort:

    def __str__(self):
        return "归并排序"

    def __merge_of_two_sorted_array(self, arr, left, mid, right):
        # Python 中切片即复制，复制到一个临时数组中
        nums_for_compare = arr[left:right + 1]
        i = 0
        j = mid - left + 1
        # 通过 nums_for_compare 数组中设置两个指针 i、j 分别表示两个有序数组的开始
        # 覆盖原始数组
        for k in range(left, right + 1):
            if i > mid - left:
                arr[k] = nums_for_compare[j]
                j += 1
            elif j > right - left:
                arr[k] = nums_for_compare[i]
                i += 1
            elif nums_for_compare[i] <= nums_for_compare[j]:
                # 注意：这里使用 <= 是为了保证归并排序算法的稳定性
                arr[k] = nums_for_compare[i]
                i += 1
            else:
                assert nums_for_compare[i] >= nums_for_compare[j]
                arr[k] = nums_for_compare[j]
                j += 1

    def __merge_sort(self, arr, left, right):
        if left >= right:
            return
        # 这是一个陷阱，如果 left 和 right 都很大的话，left + right 容易越界
        # Python 中整除使用 // 2
        mid = (left + right) // 2
        self.__merge_sort(arr, left, mid)
        self.__merge_sort(arr, mid + 1, right)
        self.__merge_of_two_sorted_array(arr, left, mid, right)

    @SortingUtil.cal_time
    def sort(self, arr):
        """
        归并排序的入口函数
        """
        size = len(arr)
        self.__merge_sort(arr, 0, size - 1)


# 归并排序优化
class Solution:
    # 列表大小等于或小于该大小，将优先于 mergeSort 使用插入排序
    INSERTION_SORT_THRESHOLD = 7

    def sortArray(self, nums):
        # global temp
        temp = [0] * len(nums)
        self.mergeSort(nums, 0, len(nums) - 1, temp)
        return nums

    def mergeSort(self, nums, left, right, temp):
        # 小区间使用插入排序
        if right - left <= Solution.INSERTION_SORT_THRESHOLD:
            self.insertionSort(nums, left, right)
            return
        mid = left + (right - left) // 2
        self.mergeSort(nums, left, mid, temp)
        self.mergeSort(nums, mid + 1, right, temp)
        # 如果数组的这个子区间本身有序，无需合并
        if nums[mid] <= nums[mid + 1]:
            return
        self.mergeOfTwoSortedArray(nums, left, mid, right, temp)

    def insertionSort(self, nums, left, right):
        # 对数组 nums 的子区间 [left..right] 使用插入排序
        for i in range(left + 1, right + 1):
            temp = nums[i]
            j = i
            while j > left and nums[j - 1] > temp:
                nums[j] = nums[j - 1]
                j -= 1
            nums[j] = temp

    def mergeOfTwoSortedArray(self, nums, left, mid, right, temp):
        # 合并两个有序数组：先把值复制到临时数组，再合并回去
        for i in range(left, right + 1):
            temp[i] = nums[i]
        i = left
        j = mid + 1
        for k in range(left, right + 1):
            if i == mid + 1:
                nums[k] = temp[j]
                j += 1
            elif j == right + 1:
                nums[k] = temp[i]
                i += 1
            elif temp[i] <= temp[j]:
                # 注意写成 < 就丢失了稳定性（相同元素原来靠前的排序以后依然靠前）
                nums[k] = temp[i]
                i += 1
            else:
                # temp[i] > temp[j]
                nums[k] = temp[j]
                j += 1
