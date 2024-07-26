"""
nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。
给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。
对于每个 0 <= i < nums1.n ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。
如果不存在下一个更大元素，那么本次查询的答案是 -1 。
返回一个长度为 nums1.n 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。


示例 1：

输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
输出：[-1,3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
- 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。
- 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
示例 2：

输入：nums1 = [2,4], nums2 = [1,2,3,4].
输出：[3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 2 ，用加粗斜体标识，nums2 = [1,2,3,4]。下一个更大元素是 3 。
- 4 ，用加粗斜体标识，nums2 = [1,2,3,4]。不存在下一个更大元素，所以答案是 -1 。


提示：

1 <= nums1.n <= nums2.n <= 1000
0 <= nums1[i], nums2[i] <= 10^4
nums1和nums2中所有整数 互不相同
nums1 中的所有整数同样出现在 nums2 中


进阶：你可以设计一个时间复杂度为 O(nums1.n + nums2.n) 的解决方案吗？
"""
from typing import List
import collections

# 暴力解法：双循环 O(n1*n2)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 题目条件：
        # 1. nums1和nums2中所有整数 互不相同
        # 2. nums1的元素一定在nums2

        n1, n2 = len(nums1), len(nums2)
        # 返回一个长度为 n1 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。不存在是-1
        ans = [-1] * n1
        for i, x in enumerate(nums1):
            j = nums2.index(x)
            for j in range(j + 1, n2):
                if nums2[j] > x:
                    ans[i] = nums2[j]
                    break

        return ans


# todo 单调栈 + 字典 O(n)
# 类似：04-栈&队列\单调栈(队列)\739. 每日温度.py
# 写法1
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 题目条件：
        # 1. nums1和nums2中所有整数 互不相同
        # 2. nums1的元素一定在nums2

        # dic存放nums2所有数字对应的下一个最大元素
        dic = {}
        # st 单调递减，正序遍历nums2，栈顶保存当前位置还没有找到下一个更大元素的元素
        st = []
        for i, x in enumerate(nums2):  # 这里正序遍历，或者倒序遍历都可以解答
            while st and x > st[-1]:
                top = st.pop()
                dic[top] = x
                
            st.append(x)

        # 返回一个长度为 len(nums1) 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。不存在是-1
        ans = []
        for x in nums1:
            if x in dic:
                ans.append(dic[x])
            else:
                ans.append(-1)
        return ans

# 写法2
class Solution2:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # dic存放nums2所有数字对应的下一个最大元素
        dic = {}
        # st 单调递减，倒序遍历nums2，栈顶保存当前位置能看到的后面最近的更大元素
        st = []
        
        for x in reversed(nums2):
            while st and x >= st[-1]:
                st.pop()
                
            dic[x] = st[-1] if st else -1
            st.append(x)

        # 查找nums1中元素
        ans = [dic[val] for val in nums1]
        return ans
    
    
if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    # [-1, 3, -1]
    print(nextGreaterElement(nums1, nums2))
