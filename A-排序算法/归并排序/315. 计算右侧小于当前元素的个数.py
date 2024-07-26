"""
给你一个整数数组 nums ，按要求返回一个新数组 counts 。
数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。


示例 1：

输入：nums = [5,2,6,1]
输出：[2,1,1,0]
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素
示例 2：

输入：nums = [-1]
输出：[0]
示例 3：

输入：nums = [-1,-1]
输出：[0,0]


提示：

1 <= nums.n <= 105
-104 <= nums[i] <= 104
"""
from typing import List

# todo 归并排序计算右侧小于当前元素的个数,分以下2种情况
'''
1. 归并左侧元素/只剩左边元素
原始数组: [1,3,5,8,2,4,6,7]
            i       j
nums: 1 2 3 4 / 2 4 6 7
temp:     5 8 /     6 7  
            m   k 
                5是当前要归并的元素: 5的右边比它小的元素个数为 (j-1)-(m+1)+1 = j-m-1 

            i           j
nums: 1 2 3 4 / 5 6 7 7
temp:       8 /     
            m         k 
                      8是当前要归并的元素: 8的右边比它小的元素个数为 (j-1)-(m+1)+1 = j-m-1 
                
2. 归并右侧元素/只剩右边元素
原始数组: [1,3,5,7,2,4,6,8]
        i   m   j
nums: 1 2 5 7 / 2 4 6 8
temp:   3 5 7 /   4 6 8
        k 
        2是当前要归并的元素, 2的右边比它小的元素个数为: 0
因为2个数组都是升序的,如果归并的是右侧元素,cnt[k] = 0
'''


# 时间复杂度都是NlogN
# 方法1：归并排序解法(会修改原始数组)
class Solution:
    def __init__(self, tmp: list = None, cnt: list = None):
        self.tmp = tmp  # 归并排序辅助数组
        self.cnt = cnt  # 记录每个元素后面比自己小的元素个数

    class Pair:
        """将数组元素和索引封装为一个pair对象, 这里换成turpe封装也可以"""

        def __init__(self, val: int, idx: int):
            # 记录数组的元素值
            self.val = val
            # 记录元素在数组中的原始索引
            self.idx = idx

    def countSmaller(self, nums: List[int]) -> List[int]:
        """计算右侧小于当前元素的个数"""
        n = len(nums)
        self.tmp = [self.Pair(0, 0) for _ in range(n)]
        self.cnt = [0] * n
        # 将数组nums元素转换为pairs对象
        arr = [self.Pair(nums[i], i) for i in range(n)]
        # 调用归并排序算法
        self.mergeSort(arr, 0, n - 1)
        return self.cnt

    def mergeSort(self, arr: List[Pair], left: int, right: int) -> None:
        """对数组arr进行归并排序,无返回值"""
        if left == right:  # 只有1个元素，就不用排序，直接返回
            return

        mid = left + (right - left) // 2  # 向上取整,避免mid+1越界

        self.mergeSort(arr, left, mid)
        self.mergeSort(arr, mid + 1, right)

        # todo 优化: 如果切分的2个数组本身就是有序,就不需要调用mergeTwoSortedArr
        if nums[mid] <= nums[mid + 1]:
            return

        # todo 二叉树后续位置
        self.mergeTwoSortedArr(arr, left, mid, right)

    def mergeTwoSortedArr(self, arr: List[Pair], left: int, mid: int, right: int) -> None:
        """合并2个有序数组nums[lo..mid] 和 nums[mid+1..hi]。无返回值。"""
        # 注意:这里arr是一个包含元素和索引对象的列表
        for i in range(left, right + 1):
            self.tmp[i] = arr[i]

        i, j = left, mid + 1
        for p in range(left, right + 1):
            if i == mid + 1:
                # 只剩右边数组
                arr[p] = self.tmp[j]
                j += 1
            elif j == right + 1:
                # 只剩左边数组
                arr[p] = self.tmp[i]
                i += 1
                # todo 更新 count 数组
                self.cnt[arr[p].idx] += j - mid - 1
            elif self.tmp[i].value <= self.tmp[j].value:  # 这里写等于是为了维护原始数组相同元素的有序性
                # 归并左边元素
                arr[p] = self.tmp[i]
                i += 1
                # todo 更新 count 数组
                self.cnt[arr[p].idx] += j - mid - 1
            else:
                # 归并右边元素
                arr[p] = self.tmp[j]
                j += 1


# todo 插入排序: 二分查找有序数组中最后一个
'''
原始数组nums:
1 8 3 6 7 4 4 2 
辅助数组temp:
2 4 4 7
当前要查找的是6: 在temp中查找第一个大于6的元素索引(右侧边界二查)
并且要将6插入到找到的元素前面
'''


# 方法2：插入排序:右侧边界二分查找(不修改原始数组)
def countSmaller2(nums: List[int]) -> List[int]:
    """计算右侧小于当前元素的个数"""
    cnt = [0] * len(nums)
    tmp = [nums[-1]]  # 用来帮助查找的辅助数组, 需要维持升序排列
    # 从后往前查找:倒数第二个元素开始
    for i in range(len(nums) - 2, -1, -1):
        num = nums[i]

        # todo 优化:
        if num <= tmp[0]:
            # 因为tmp本身有序,如果num小于等于tmp[0],说明它右边比他小的数为0;
            cnt[i] = 0
            tmp.insert(0, num)
        elif num > tmp[-1]:
            # 如果num大于tmp[-1],说明tmp所有的数都比num小
            cnt[i] = len(tmp)
            tmp.append(num)
        else:
            # todo 在temp中查找第一个大于num的元素索引(右侧边界二查), 需要优化!!!
            left, right = 0, len(tmp) - 1
            while left <= right:
                mid = (right + left) // 2  # 向下取整,保证mid+1不越界
                if tmp[mid] <= num:
                    left = mid + 1
                elif tmp[mid] > num:
                    right = mid - 1

            if left == 0:  # tmp中没有数比num小
                cnt[i] = 0
            else:
                cnt[i] = left  # 最后返回的索引是left = mid + 1,统计该索引位置元素个数，就是left
            tmp.insert(left, num)

    return cnt


if __name__ == '__main__':
    nums = [7, 6, 4, 2, 8, 5]
    # nums = [-4, 0, 7, 4, 9, -5, -1, 0, -7, -1]
    print(nums)
    print(countSmaller2(nums))
    print(Solution().countSmaller(nums))

