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
import random
from typing import List

'''
# 基础的快排代码逻辑如下
1. 选择一个基准值，一般选择序列的第一个元素、最后一个元素或者中间的元素作为基准值。 
2. 将序列按照基准值分成两个子序列，小于基准值的元素放在左边，大于基准值的元素放在右边，相等的元素可以放在任意一侧。 
3. 对左右两个子序列分别进行递归排序，直到子序列的长度为1或0。 
4. 因为都是在原数组上进行数值大小比较和位置交换，因此不占用额外的内存空间

nums原始数组为：[5, 4, 7, 0, 9, 6]
# 第一轮：观察partition函数交换基准值左右元素逻辑
基准值选择第一个元素 pivot = 5
l          r
5  4 7 0 9 6
j  i 
① i = 1: 4 < 5  j+=1 4和4进行交换 

5  4 7 0 9 6   
     j i  
② i = 3: 0 < 5 j+=1  7和0进行交换
   
5  4 0 7 9 6   
     j     i  
     
③ 循环结束， 5和0交换
0  4 5 7 9 6   
     j     i  

5左边是0,4 右边是7,9,6
# all in nums[left + 1..j] <= pivot
# all in nums(j..i) > pivot
partition函数最后返回j,即索引2

# 第二轮：观察递归函数
递归对j左右2边数组[0,4]和[7,9,6]执行分区排序逻辑
j左边为[0,4] 基准值为0, partition之后，数组还是[0,4],返回j=0
    j左边没有元素了， 调用递归代码出现left>right (0,-1), 不用进行partiton分区排序了
    j右边只有1个元素4，调用递归代码出现left=right (1,1), 也不用进行partiton分区排序了
    此时数组前3个： 0 4 5 已经有序

j右边为[7,9,6] 基准值为7, partition之后, partition之后数组为[6,7,9], 返回j=1
    j左右各一个元素，按照上面逻辑，都不用再partition，
    此时数组前3个： 0 4 5 有序， 后3个：6 7 9有序
    整个数组已经全部有序了！！！
'''


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        快排的简单写法，pivot选择中间值
        """
        if len(nums) <= 1:
            return nums

        pivot = nums[len(nums)//2]
        smaller = [num for num in nums if num < pivot]
        equal_lst = [num for num in nums if num == pivot]
        bigger = [num for num in nums if num > pivot]

        # 递归，返回排序后的数组
        return self.sortArray(smaller) + equal_lst + self.sortArray(bigger)


# 测试
nums = [5, 4, 7, 0, 9, 6]
print(Solution().sortArray(nums))


class Solution2:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    i = 0

    def quickSort(self, nums, left, right) -> None:
        """根据partition函数返回的基准值索引，对基准值左半边和右半边递归进行排序。
        left,right代表要处理的数组索引边界为：[left..right]
        无返回值
        """
        if left >= right:
            return

        self.i += 1

        # print(f'\ni = {self.i}, quickSort=> {left, right}')

        pivotIdx = self.partition(nums, left, right)
        self.quickSort(nums, left, pivotIdx - 1)
        self.quickSort(nums, pivotIdx + 1, right)

    def partition(self, nums, left, right) -> int:
        """基准值选择数组第一个元素。原地交换数组元素。将不大于基准值的元素排在左边，大于的排在右边
        left,right代表要处理的数组索引边界为：[left..right]
        return：数组排好序之后，基准值所在位置索引j
        """
        pivot = nums[left]
        j = left
        # all in nums[left + 1..j] <= pivot
        # all in nums(j..i) > pivot
        for i in range(left + 1, right + 1):
            if nums[i] <= pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[j] = nums[j], nums[left]

        print(f'返回pivotIdx = {j} nums = {nums[left: right + 1]}')

        return j


'''
上面代码对本来就比较有序的数组，时间复杂度会到O(n^2)，最后时间超限
比如对于数组：
nums = [0, 1, 2, 3, 4, 5], len = 6

i = 1, quickSort=> (0, 5)
返回pivotIdx = 0 nums = [0, 1, 2, 3, 4, 5]

i = 2, quickSort=> (1, 5)
返回pivotIdx = 1 nums = [1, 2, 3, 4, 5]

i = 3, quickSort=> (2, 5)
返回pivotIdx = 2 nums = [2, 3, 4, 5]

i = 4, quickSort=> (3, 5)
返回pivotIdx = 3 nums = [3, 4, 5]

i = 5, quickSort=> (4, 5)
返回pivotIdx = 4 nums = [4, 5]

这个跟归并排序正好相反，也就是说快速排序对越乱序的数组，排序效率就越高。
效率底的原因在于基准值固定选择数组第一位
优化方向：基准值改为选择数组中随机数
'''

if __name__ == '__main__':
    # repeat = [random.randint(0, 6) for _ in range(7)]
    # print(f'repeat = {repeat}')

    nonRepeat = random.sample(range(10), 6)  # 从0到9中随机选择10个数，保证不重复
    print(f'nonRepeat = {nonRepeat}, len = {len(nonRepeat)}')
    Solution().sortArray(nonRepeat)

    # nums = list(range(6))
    # print(f'nums = {nums}, len = {len(nums)}')
    # Solution().sortArray(nums)

    # my_list = [1, 2, 3, 4, 5]
    # random_number = random.choice(my_list)
    # print(random_number)

    print(nonRepeat)
