"""
你将得到一个整数数组 matchsticks ，其中 matchsticks[i] 是第 i 个火柴棒的长度。
你要用 所有的火柴棍 拼成一个正方形。
你 不能折断 任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须 使用一次 。

如果你能使这个正方形，则返回 true ，否则返回 false 。

示例 1:
输入: matchsticks = [1,1,2,2,2]
输出: true
解释: 能拼成一个边长为2的正方形，每边两根火柴。

示例 2:
输入: matchsticks = [3,3,3,3,4]
输出: false
解释: 不能用所有火柴拼成一个正方形。

提示:
1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 108
"""
from typing import List


"""
解题思路：
这道题可以使用回溯法来解决。我们需要尝试将火柴拼接成一个正方形，
所以可以将问题转化为在数组 nums 中找到长度为 4 的子集，使得这些子集的和都相等且等于正方形的边长。

具体步骤如下：
1.首先判断数组 nums 的长度是否小于 4，如果小于 4，则无法构成正方形，直接返回 False。
2.计算数组 nums 的总和 total，并判断 total 是否能被 4 整除，如果不能整除，则无法构成正方形，直接返回 False。
3.定义一个长度为 4 的数组 sides，用于记录正方形的边长。
4.对数组 nums 进行排序，从大到小的顺序进行回溯搜索：
    - 如果当前火柴的长度加上 sides 中任意一条边的长度不超过正方形的边长，则将当前火柴加入到 sides 中，并继续搜索下一根火柴。
    - 如果无法满足上述条件，则回溯到上一层。
5.当 sides 中的所有边都被填满时，检查 sides 中的边长是否都相等，如果相等则返回 True，否则返回 False。
"""


# todo：回溯算法
# 类似 698-划分为k个相等的子集.py
# 时间复杂度：O(4^n)，其中 n 是火柴的数目。每根火柴都可以选择放在 4 条边上，因此时间复杂度为 O(4^n)
# 空间复杂度：O(n)。递归栈需要占用 O(n) 的空间。

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # 判断用 matchsticks所有的火柴棍 能否拼成一个正方形
        # todo 问题等价于：用matchsticks所有球，能否转满4个固定容量相同的桶
        total = sum(matchsticks)
        n = len(matchsticks)
        
        # avg:正方形边长（即每个桶容量）
        avg = total // 4    
        matchsticks.sort(reverse=True)   # 降序排序，方便dfs剪枝
        
        # 排除明显不符合条件的情况
        if total % 4 != 0 or n < 4 or matchsticks[0] > avg:
            return False

        def dfs(i=0, edges=[0] * 4):
            # i代表 当前选择的matchsticks 下标,edges[i]代表正方形第 i条边的火柴棒总长度
            if i == n:
                # 如果i可以递归到n,必然满足每个桶转满了avg个数
                return True

            selected = matchsticks[i] # 当前选择的球
            
            for j in range(4):
                # 剪枝：前提是nums降序，相邻桶球数量相同，如果前面的桶尝试不能满足，后面的就不用再试了
                if j > 0 and edges[j] == edges[j-1]:
                    continue
                
                if edges[j] + selected <= avg:
                    edges[j] += selected # 先尝试转这个球
                    
                    if dfs(i+1, edges):
                        # 递归处理下一个球，如果找到一个可行解，马上返回True
                        return True
                    
                    edges[j] -= selected  # 没有找到可行解，再回溯
            return False

        return dfs()


if __name__ == '__main__':
    # matchsticks = [1, 1, 2, 2, 2]  # True
    matchsticks = [3, 3, 3, 3, 4]  # False
    print(Solution().makesquare(matchsticks))
