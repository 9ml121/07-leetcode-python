"""
如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为 摆动序列 。第一个差（如果存在的话）可能是正数或负数。仅有一个元素或者含两个不等元素的序列也视作摆动序列。

例如， [1, 7, 4, 9, 2, 5] 是一个 摆动序列 ，因为差值 (6, -3, 5, -7, 3) 是正负交替出现的。

相反，[1, 4, 7, 2, 5] 和 [1, 7, 4, 5, 5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
子序列 可以通过从原始序列中删除一些（也可以不删除）元素来获得，剩下的元素保持其原始顺序。

给你一个整数数组 nums ，返回 nums 中作为 摆动序列 的 最长子序列的长度 。



示例 1：

输入：nums = [1,7,4,9,2,5]
输出：6
解释：整个序列均为摆动序列，各元素之间的差值为 (6, -3, 5, -7, 3) 。
示例 2：

输入：nums = [1,17,5,10,13,15,10,5,16,8]
输出：7
解释：这个序列包含几个长度为 7 摆动序列。
其中一个是 [1, 17, 10, 13, 10, 16, 8] ，各元素之间的差值为 (16, -7, 3, -3, 6, -8) 。
示例 3：

输入：nums = [1,2,3,4,5,6,7,8,9]
输出：2


提示：

1 <= nums.length <= 1000
0 <= nums[i] <= 1000


进阶：你能否用 O(n) 时间复杂度完成此题?
"""
from typing import List

"""
解题思路：
这道题可以使用动态规划（DP）来解决。
1.定义两个变量 up 和 down，分别表示最后两个元素构成的上升摆动序列和下降摆动序列的长度。
    初始时，将 up 和 down 都设为 1。

2.遍历数组 nums，对于每个元素 nums[i]，比较其与前一个元素 nums[i-1] 的大小关系，分为以下三种情况：
    - 如果 nums[i] > nums[i-1]，说明当前元素与前一个元素构成了上升摆动序列，更新 up = down + 1，因为在上升摆动序列后增加一个较大的元素会形成更长的摆动序列。同时保持 down 不变。
    - 如果 nums[i] < nums[i-1]，说明当前元素与前一个元素构成了下降摆动序列，更新 down = up + 1，因为在下降摆动序列后增加一个较小的元素会形成更长的摆动序列。同时保持 up 不变。
    - 如果 nums[i] == nums[i-1]，当前元素与前一个元素相等，不会对摆动序列的长度产生影响，保持 up 和 down 不变。

3.最终，最长的摆动子序列的长度就是 max(up, down)。
"""


# 方法 1：动态规划
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        up = [1] + [0] * (n - 1)
        down = [1] + [0] * (n - 1)
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = max(up[i - 1], down[i - 1] + 1)
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                up[i] = up[i - 1]
                down[i] = max(up[i - 1] + 1, down[i - 1])
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]

        return max(up[n - 1], down[n - 1])


# 方法 1 的另外一种写法
class Solution1:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        dp_up_down = [[0, 0] for _ in range(n)]
        # dp[i][0] 表示：以区间 [0..i] 个元素中的 某一个 为结尾的最长的上升的「摆动序列」的长度；
        # dp[i][1] 表示：以区间 [0..i] 个元素中的 某一个 为结尾的最长的下降的「摆动序列」的长度。
        dp_up_down[0][0] = 1
        dp_up_down[0][1] = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                # 情况 1：上升
                # 接在原来下降的部分后面形成更长的子序列
                dp_up_down[i][0] = dp_up_down[i - 1][1] + 1
                # 保持不变，相当于 nums[i] 不选
                dp_up_down[i][1] = dp_up_down[i - 1][1]
            elif nums[i] < nums[i - 1]:
                # 保持不变，相当于 nums[i] 不选
                dp_up_down[i][0] = dp_up_down[i - 1][0]
                # 情况 2：下降
                # 接在原来上升的部分后面形成更长的子序列
                dp_up_down[i][1] = dp_up_down[i - 1][0] + 1
            else:
                # 情况 3：nums[i - 1] == nums[i]，可以认为 nums[i] 没有出现过一样
                dp_up_down[i][0] = dp_up_down[i - 1][0]
                dp_up_down[i][1] = dp_up_down[i - 1][1]

        return max(dp_up_down[-1])


# 方法 2：dp优化空间的解法：注意到方法一中，我们仅需要前一个状态来进行转移，所以我们维护两个变量即可。
class Solution2:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up = down = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1

        # print(f'{up}, {down}')
        return max(up, down)


# 方法 3：贪心算法：统计变化次数
# 只需要关注上面「折线图」中上升和下降的转折点，把它们单独拿出来，就构成了原始输入数组的一个长度最长的「摆动序列」。
class Solution3:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        pre_direction = 0
        res = 1  # res代表转折点个数，也是就要求的长度最长的「摆动序列」

        for i in range(1, n):
            cur_direction = nums[i] - nums[i - 1]
            if (cur_direction > 0 and pre_direction <= 0) or (cur_direction < 0 and pre_direction >= 0):
                res += 1
                pre_direction = cur_direction
        return res


"""
本题总结：
- 动态规划问题须要考虑 所有的 情况，并使用状态表格记录求解过程中需要计算的所有状态；
- 贪心算法每一步决策的时候只关注当前阶段相关变量的值，不同于动态规划，历史的变量的值不需要保存。
"""