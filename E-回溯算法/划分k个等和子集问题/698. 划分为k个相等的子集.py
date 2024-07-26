"""
题目描述
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

示例
输入	nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出	true
说明	有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
输入	nums = [1,2,3,4], k = 3
输出	false
说明	无

提示
1 <= k <= len(nums) <= 16
0 < nums[i] < 10000
每个元素的频率在 [1,4] 范围内
"""
from typing import List

'''
题目解析:本题其实是一道子集问题，可以利用回溯法求解。
1.首先，我们可以求出nums数组的所有元素之和sum，如果sum % k 不为0的话，说明每一份子集的和不是整数，
但是题目说了nums数组中的元素都是整数，因此每一个子集的和也应该是整数，因此如果sum % k 不为0的话，则返回false。

2.如果sum % k 为0，则我们假设subSum = sum / k，即每一个子集的和为subSum，那么subSum应该大于等于nums数组的最大值，
因为nums数组的每一个子集至少有一个元素组成，因此subSum应该大于或等于每一个nums元素，即至少不小于nums数组的最大值。

3.当面两个条件都符合后，还不能说明nums可以被分为k个和相等的子集，比如nums=[2,2,2,2,3,4,5] ，且k=4。
nums数组的和sum = 20，k=4，因此subSum = 5,而subSum >= max(nums[i]) = 5，因此符合上面两个条件，但是nums数组却无法分为4个等和子集。

4.因此，我们需要一种算法来判断一个数组是否可以划分k个和相等的子集，此时我们就需要借助回溯算法。
我们可以想象划分子集问题，可以看成向k个桶中放球，每个桶的承重为subSum，
而现在nums中存放着重量不一的多个球，如果nums中的球都能放到k个桶中，则可以划分子集成功。
比如nums = [4, 3, 2, 3, 5, 2, 1], k = 4，对应的subSum=5
    1.首先，nums的重量5的球可以独占一个桶，我们可以减少考虑一个桶的处理
    2.接下来，我们需要将球按照降序排序，然后依次放入桶中 [4,3,3,2,2,1]
    3.由于 4 + 3 > 5，因此球3需要放到下一个桶中
    4.同理处理下面的球
这里我们对nums进行了降序排序，而不是升序排序，因为升序排序可能会产生非常复杂的放置行为，这将不利于我们理解。 
'''

# todo 回溯：划分k个等和子集
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 是否有可能把nums数组分成 k 个非空子集，其总和都相等
        nums.sort(reverse=True)  # nums降序，为了后面dfs剪枝
        n = len(nums)

        # avg：每个桶容量限制
        total = sum(nums)
        avg = total // k

        # 排除明显不符合的情况
        if total % k != 0 or k > n or nums[0] > avg:
            return False

        def dfs(i=0, buckets=[0] * k):
            """
            nums = [5,4,3,3,2,2,1],k = 4, avg = 5
            以桶选择球的视角，依次往k个桶放球，直到每个桶都能放满avg个球，结果返回是否可以装下所有nums所有球
            @i: 第 i 个球开始做选择
            @buckets[i]: 代表第i个桶的已经使用的容量
            """
            if i == n:
                # 如果i可以递归到n, 必然满足每个桶容量是avg
                return True

            # 当前选择的球
            selected = nums[i] 
            for j in range(k):
                # 剪枝：前提是nums降序，相邻桶球数量相同，如果前面的桶尝试不能满足，后面的就不用再试了
                if j > 0 and buckets[j] == buckets[j - 1]:
                    continue

                if buckets[j] + selected <= avg:
                    buckets[j] += selected  # 先放进去试试
                    if dfs(i + 1, buckets):
                        # 递归处理下一个球，如果找到一个可行解，马上返回True
                        return True

                    buckets[j] -= selected  # 没有找到可行解，再回溯

            # 尝试所有可能都没找到一个可行解
            return False

        return dfs()
   
    


if __name__ == '__main__':
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    cls = Solution()
    print(cls.canPartitionKSubsets(nums, k))
