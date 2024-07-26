"""
对于一棵深度小于 5 的树，可以用一组三位十进制整数来表示。对于每个整数：

百位上的数字表示这个节点的深度 d，1 <= d <= 4。
十位上的数字表示这个节点在当前层所在的位置 P， 1 <= p <= 8。位置编号与一棵满二叉树的位置编号相同。
个位上的数字表示这个节点的权值 v，0 <= v <= 9。
给定一个包含三位整数的 升序 数组 nums ，表示一棵深度小于 5 的二叉树，请你返回 从根到所有叶子结点的路径之和 。

保证 给定的数组表示一个有效的连接二叉树。



示例 1：
输入: nums = [113, 215, 221]
输出: 12
解释: 列表所表示的树如上所示。
路径和 = (3 + 5) + (3 + 1) = 12.

示例 2：
输入: nums = [113, 221]
输出: 4
解释: 列表所表示的树如上所示。
路径和 = (3 + 1) = 4.


提示:
1 <= nums.length <= 15
110 <= nums[i] <= 489
nums 表示深度小于 5 的有效二叉树
"""
from typing import List


# 错误解法：下面解法是求二叉树所有节点 val之和
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        self.tree = {}
        # 将输入的数组转换为字典
        for num in nums:
            d, p, v = num // 100, (num % 100) // 10, num % 10
            self.tree[(d, p)] = v

        print(self.tree)
        # {(1, 1): 3, (2, 1): 5, (2, 2): 1}

        return self.dfs(1, 1)

    def dfs(self, d, p):
        if (d, p) not in self.tree:
            return 0

        v = self.tree[(d, p)]
        left_child = (d + 1, p * 2 - 1)
        right_child = (d + 1, p * 2)

        if left_child not in self.tree and right_child not in self.tree:
            return v

        left_v = self.dfs(d + 1, p * 2 - 1)
        right_v = self.dfs(d + 1, p * 2)

        return v + left_v + right_v


# 正确解法
class Solution2:
    def pathSum(self, nums: List[int]) -> int:
        self.tree = {}
        # 将输入的数组转换为字典
        for num in nums:
            d, p, v = num // 100, (num // 10) % 10, num % 10
            self.tree[(d, p)] = v

        print(self.tree)
        # {(1, 1): 3, (2, 1): 5, (2, 2): 1}

        self.res = 0
        self.dfs(1, 1, 0)
        return self.res

    def dfs(self, d, p, pathSum):
        if (d, p) not in self.tree:
            return

        pathSum += self.tree[(d, p)]
        left_child = (d + 1, p * 2 - 1)
        right_child = (d + 1, p * 2)

        if left_child not in self.tree and right_child not in self.tree:
            self.res += pathSum
        else:
            self.dfs(d + 1, p * 2 - 1, pathSum)
            self.dfs(d + 1, p * 2, pathSum)


if __name__ == '__main__':
    nums = [113, 215, 221]
    print(Solution2().pathSum(nums))  # 12
