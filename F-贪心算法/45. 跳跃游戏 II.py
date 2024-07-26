"""
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
    0 <= j <= nums[i]
    i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。


示例 1:
输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

示例 2:
输入: nums = [2,3,0,1,4]
输出: 2


提示:
1 <= nums.n <= 10^4
0 <= nums[i] <= 1000
题目保证可以到达 nums[n-1]
"""
import collections
from typing import List

# 方法 1：贪心算法(最优解)
"""
「贪心算法」的直觉
如果我们想达到下标 2，一定只会选择跳 1 次（从下标 0 跳到下标 2，图中黑色箭头），而不会选择跳 2 次
（从下标 0 跳到下标 1，再从下标 1 跳到下标 2，图中黑色箭头加红色箭头）

我们除了关心「当前步骤可以跳到的最远的位置」以外，还需要关心「下一步跳跃可以到达的最远的位置」（这一点是可以「贪心选择性质」）。
如果比较难理解，可以再对照上图，虚拟出来的灰色结点 5，想一想为什么从起点位置（下标 0）到灰色结点 5，最少需要跳 3 次。
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        """返回到达 nums[n - 1] 的最小跳跃次数
        nums = [2, 3, 1, 1, 4, 5]
        idx  =  0  1  2  3  4  5
        """
        # 最终结果：需要的最少跳跃次数
        ans = 0
        # 当前能跳跃到的最远下标
        cur_cover = 0
        # 下一步跳跃的最远下标
        next_cover = 0
        
        # 注意：如果len(nums) == 1, 所需最小步骤为0，所以nums最后一个位置不用看
        for i in range(len(nums) - 1):
            next_cover = max(i + nums[i], next_cover)
            # 1.判断：如果在当前跳跃范围内，就能跳跃到最后，直接退出循环，跳跃次数 + 1
            if i + nums[i] >= len(nums) - 1:
                ans += 1
                return ans
            
            # 2.判断：如果走到当前能跳跃的最远下标，还不能跳跃到最后，就要进入下一步能跳跃的最远边界遍历。跳跃次数+1
            if i == cur_cover:
                # 遇到这一步可以到达的最远边界，就更新为下一步可以达到的最远边界，并且最少步数加一
                ans += 1
                cur_cover = next_cover

        return ans


# 方法 2：BFS ,时间复杂度 0(N^2):超时！！
class Solution2:
    def jump(self, nums: List[int]) -> int:
        """返回到达 nums[n - 1] 的最小跳跃次数
        nums = [2, 3, 1, 1, 4, 5]
        idx  =  0  1  2  3  4  5
        """
        n = len(nums)
        if n == 1:
            return 0

        # dq记录可以调到的位置索引idx + 跳到该位置需要的最小步骤minStep
        dq = collections.deque([(0, 1)])
        # vis数组标记该位置是否已经跳到，防止重复访问
        vis = [False] * n  
        
        while dq:
            idx, minStep = dq.popleft()
            # maxReachedIdx：当前位置可以调到的最远位置索引
            maxReachedIdx = idx + nums[idx]
            
            if maxReachedIdx >= n - 1:
                # 当前位置可以调到最后位置，立即返回结果
                return minStep

            for i in range(idx + 1, maxReachedIdx + 1):
                # dq添加当前位置可以跳到的所有位置索引 + 所需步骤
                if not vis[i]:
                    vis[i] = True
                    dq.append((i, minStep + 1))


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4, 5]
    print(Solution2().jump(nums))
