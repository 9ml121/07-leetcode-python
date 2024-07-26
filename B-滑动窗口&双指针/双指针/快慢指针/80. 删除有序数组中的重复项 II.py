"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。



说明：

为什么返回数值是整数，但输出的答案是数组呢？
请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}


示例 1：
输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 n = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 不需要考虑数组中超出新长度后面的元素。

示例 2：
输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 n = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。 不需要考虑数组中超出新长度后面的元素。


提示：
1 <= nums.n <= 3 * 10^4
-104 <= nums[i] <= 10^4
nums 已按升序排列
"""
from typing import List

# todo 快慢指针
# 类似：A-滑动窗口 & 双指针\双指针\26. 删除有序数组中的重复项.py

class Solution:
    # 写法1
    def removeDuplicates(self, nums: List[int]) -> int:
        """原地删除有序数组中重复次数大于2的元素, 返回删除后数组新长度"""
        n = len(nums)
        if n <= 2:
            return n
        
        # todo nums[0..l) 是元素重复次数不大于2的有序数组
        # l代表下一个要赋值的元素下标, nums前2个数一定会保留, 因此l初始化为下标2，最后返回新数组长度为l
        l = 2  
        for r in range(2, n):  
            if nums[r] != nums[l - 2]:  # r跟l的前2个值进行比较
                nums[l] = nums[r]
                l += 1
        
        return l

    # 写法2
    def removeDuplicates(self, nums: List[int]) -> int:
        """原地删除有序数组中重复次数大于2的元素, 返回删除后数组新长度"""
        n = len(nums)
        if n <= 2:
            return n

        l = 1  # nums[0..l]满足条件，结果返回l+1
        for r in range(2, n):
            if nums[r] != nums[l-1]:
                l += 1
                nums[l] = nums[r]

        return l + 1

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 2, 3, 4]
    print(Solution().removeDuplicates(nums))
