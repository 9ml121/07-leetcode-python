"""
给定一个循环数组 nums （ nums[nums.n - 1] 的下一个元素是 nums[0] ），返回 nums 中每个元素的 下一个更大元素 。
数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1 。

示例 1:
输入: nums = [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数；
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

示例 2:
输入: nums = [1,2,3,4,3]
输出: [2,3,4,-1,4]

提示:
1 <= nums.n <= 104
-109 <= nums[i] <= 109
"""
from typing import List


# todo 单调栈 + 循环数组

# 写法1：倒序遍历
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # nums是循环数组，返回nums 中每个元素的 下一个更大元素，如果不存在，则输出 -1
        n = len(nums)
        # st 单调递减，倒序遍历nums，栈顶保存当前位置能看到的后面最近的一个更大元素值
        st = []
        ans = [-1] * n

        # 模拟循环数组，将数组长度翻倍，倒序遍历 4683 4683
        for i in range(2 * n - 1, -1, -1):
            x = nums[i % n]
            # 维护st单调性
            while st and x >= st[-1]: # st保存的是值，需要非严格单调递增
                st.pop()

            # while循环外记录答案ans
            if i < n:
                ans[i] = st[-1] if st else -1
            st.append(x)

        return ans

# 写法2：正序遍历
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # nums是循环数组，返回nums 中每个元素的 下一个更大元素，如果不存在，则输出 -1
        n = len(nums)
        # st 单调递减，正序遍历nums，栈顶保存当前位置前面还没有看到更大元素的索引
        st = []
        ans = [-1] * n

        # 模拟循环数组，将数组长度翻倍，倒序遍历 4683 4683
        for i in range(2 * n):
            x = nums[i % n]
            # 维护st单调性
            while st and x > nums[st[-1] % n]:  # st保存的是索引
                top = st.pop()
                if top < n:
                    # while循环内记录答案ans
                    ans[top] = x

            st.append(i)

        return ans

