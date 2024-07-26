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

'''
1.归并排序的过程可以在逻辑上抽象成一棵二叉树，树上的每个节点的值可以认为是 nums[lo..hi]，叶子节点的值就是数组中的单个元素：
         3241
        /   \
       32   41
      / \   / \
     3   2  4  1

2.然后，在每个节点的后序位置（左右子节点已经被排好序）的时候执行 merge 函数，合并两个子节点上的子数组：
      merge
      1 23 4
      /    \
     23    14

3.后续遍历二叉树: sort函数
        7
      /   \
     3     6
    / \   / \  
   1  2   4  5

4. 结合上述基本分析，我们把 nums[lo..hi] 理解成二叉树的节点，sort 函数理解成二叉树的遍历函数，整个归并排序的执行过程  
'''


# todo 归并排序算法：mergeSort
# 归并排序就是先把左半边数组排好序，再把右半边数组排好序，然后把两半数组合并。
# 分解问题的思路（ 分治算法）

# 归并算法的复杂度计算，就是子问题个数 * 解决一个子问题的复杂度
# 执行的次数是二叉树节点的个数，每次执行的复杂度就是每个节点代表的子数组的长度，所以总的时间复杂度就是整棵树中「数组元素」的个数。
# 所以从整体上看，这个二叉树的高度是 logN，其中每一层的元素个数就是原数组的长度 n，所以总的时间复杂度就是 O(NlogN)。

class Solution:
    """方法1: 归并排序算法:O(NlogN),非稳定排序版本"""

    def __init__(self, tmp: list = None):
        #  todo 优化 1：归并排序的辅助数组，用来记录归并前的原始数组元素
        self.tmp = tmp

    def sortArray(self, nums: List[int]) -> List[int]:
        """主函数入口: 调用排序算法"""
        n = len(nums)
        self.tmp = [0] * n
        self.mergeSort(nums, 0, n - 1)
        return nums

    def mergeSort(self, nums, left, right) -> None:
        """归并排序算法总入口: 将原始数组等分为2份,调用归并排序算法,直接修改原数组,无返回值"""
        if left == right:  # 只有1个元素，就不用排序，直接返回
            return

        mid = (right + left) // 2  # 向下取整，可以保证mid+1不越界

        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid + 1, right)

        # todo 二叉树后续位置
        # todo 优化2：如果等分的2个数组,连接起来就是有序的,可以直接返回
        if nums[mid] <= nums[mid + 1]:
            return
        else:
            self.mergeTwoSortedArr(nums, left, mid, right)

    def mergeTwoSortedArr(self, nums, left, mid, right) -> None:
        """归并2个有序数组"""
        for i in range(left, right + 1):
            self.tmp[i] = nums[i]

        i, j = left, mid + 1
        for k in range(left, right + 1):
            if i == mid + 1:
                # 只剩右边数组
                nums[k] = self.tmp[j]
                j += 1
            elif j == right + 1:
                # 只剩左边数组
                nums[k] = self.tmp[i]
                i += 1
            # 下面2步是让原始数组nums[k]每次存储等分数组值更小的那个
            # 这里写等于，可以保障排序数组的稳定性
            elif self.tmp[i] <= self.tmp[j]:
                nums[k] = self.tmp[i]
                i += 1
            else:
                nums[k] = self.tmp[j]
                j += 1


if __name__ == '__main__':
    nums = [7, 6, 4, 2, 8, 5]
    # nums = [1,4,5,8,2,3,6,7]
    Solution().sortArray(nums)
    print(nums)
