"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。



示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9


提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List


# 方法 1：用了sort函数，时间复杂度超时 O(N)
# 先对nums排序，在判断相邻2数字
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return n

        nums.sort()  # 1,2,3,3,4,7,8
        cnt = 1
        ans = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                cnt += 1
                ans = max(ans, cnt)
            elif nums[i] == nums[i - 1]:
                continue
            else:
                cnt = 1

        return ans


# 方法2：哈希集合，时间复杂度O(N)
class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_seq = 0
        for num in num_set:
            if num - 1 not in num_set:
                cur_num = num
                cur_seq = 1

                while cur_num + 1 in num_set:
                    cur_seq += 1
                    cur_num += 1

                max_seq = max(cur_seq, max_seq)

        return max_seq


# 方法3：哈希字典记录右边界
# 这种方法其实也是思路2的变种，用于减少遍历次数。
# 做法是建立一个哈希表，记录每个元素num能够连续到达的右边界，这样在内层循环遍历到一个新元素时，
# 无需经过多次+1「遍历+判断」才能到达右边界，直接取值即可。
class Solution3:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_dict = dict()
        for num in nums:
            num_dict[num] = num

        max_seq = 0
        for num in nums:
            if num - 1 not in num_dict:
                right = num_dict[num]
                while right + 1 in num_dict:
                    right = num_dict[right + 1]

                # 更新右边界
                num_dict[num] = right
                #  更新答案
                max_seq = max(max_seq, right - num + 1)

        return max_seq


# 方法 4：并查集
class Solution4:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 特判
        n = len(nums)
        if n == 0 or n == 1:
            return n

        parent = dict()  # 记录每个节点的父节点
        count = dict()  # 记录节点所在连通分量的节点个数

        # 初始化父节点为自身
        for num in nums:
            parent[num] = num
            count[num] = 1

        # 寻找x的父节点，实际上也就是x的最远连续右边界
        def find(x):
            if x not in parent:
                return None

            # 完全压缩
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        # 合并两个连通分量，用来将num并入到num+1的连续区间中
        # 返回值为x所在连通分量的节点个数
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return count[px]

            parent[px] = py
            count[py] += count[px]
            return count[py]

        max_seq = 1
        for num in nums:
            if num + 1 in parent:
                cur_seq = union(num, num + 1)
                max_seq = max(max_seq, cur_seq)

        return max_seq
