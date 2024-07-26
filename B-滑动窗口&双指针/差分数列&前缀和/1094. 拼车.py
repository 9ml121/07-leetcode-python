"""
车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）
给定整数 capacity 和一个数组 trips ,  trip[i] = [numPassengersi, fromi, toi]
表示第 i 次旅行有 numPassengersi 乘客，接他们和放他们的位置分别是 fromi 和 toi 。
这些位置是从汽车的初始位置向东的公里数。

当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。

示例 1：
输入：trips = [[2,1,5],[3,3,7]], capacity = 4
输出：false

示例 2：
输入：trips = [[2,1,5],[3,3,7]], capacity = 5
输出：true


提示：
1 <= trips.n <= 1000
trips[i].n == 3
1 <= numPassengersi <= 100
0 <= fromi < toi <= 1000
1 <= capacity <= 105
"""
from typing import List

'''
差分数组问题:
1.数组trips[i] = [numPassengersi, fromi, toi] 
- 接他们和放他们的位置分别是 fromi 和 toi 
- 这些位置是从汽车的初始位置向东的公里数。
- 车 只能 向一个方向行驶
翻译过来,就是上车位置和下车位置代表两个整数区间, numPassengersi就代表在这些全闭区间增加的人数

2.问题是差分数组的长度和初始值是多少?
题目给出1 <= trips.n <= 1000, 0 <= fromi < toi <= 1000
i = fromi
j = toi
[i, j]是闭区间
由于乘客可以在任意一个站点上车,在其后任意一个站点下车, 可以将站点设置为0,1,2...1000这样步长为1的递增数组,也就是原始数组nums索引
[i, j]区间增加的人数就是inc
刚开始车上是没有人的,可以将原始数组nums初始值设置为0,

3.车有capacity 个空座位, 问题是在各区间上车人数增加之后, 会不会超过空座位总数?
遍历trips, 根据diffs更新nums,最后判断nums[i]有没有大于capacity ,就是题目答案
'''


# 1.构建等差数组类
class Diff:
    def __init__(self, nums):
        # 初始化等差数组: 因为原始数组值都为0,所以这里不用更新diffs
        self.n = len(nums)
        self.diffs = [0] * self.n

    def update(self, i, j, inc):
        # 2.todo 更新diffs,[i,j]为左闭右开!!
        self.diffs[i] += inc
        if j < self.n:  # 如果将diffs长度设为n+1, 这个判断可以取消
            self.diffs[j] -= inc

    def result(self):
        # 3.根据等差数组,更新原始数组
        res = [0] * self.n
        res[0] = self.diffs[0]
        for i in range(1, self.n):
            res[i] = res[i - 1] + self.diffs[i]

        return res


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        优化:
            1 <= trips.n <= 1000, 0 <= fromi < toi <= 1000
            如果这里trips长度很小,可以考虑下面这种思路优化:
            1.原始数组不需要0,1,2..1000这么多长度, 只需要用一个集合set搜集trips中存在的所有上下车位置pos1, pos2
            2.然后set升序排列,并用一个字典dict记录各位置的索引值{pos1:index,}
            3.初始数组nums长度设为set长度大小, 初始值为0
            4.后续更新diffs时,要将pos1和pos2转换为dict对应的index

        更正: 测试发现,还是将nums设置为固定长度1001时间复杂度更低
        """
        # 原始数组:最多有 1001 个车站,车上人数初始值为0
        nums = [0] * 1001

        # 构建等差数组类
        df = Diff(nums)

        # 更新diffs:
        for inc, i, j in trips:
            # todo: 乘客在i站点上车, j站点下车.停留在车上的区间应该为[i， j-1], 或者左开右闭[i,j)
            df.update(i, j, inc)

        # 根据diffs获取原始数组
        res = df.result()

        # 检查res数组人数有没有超过capacity
        for num in res:
            if num > capacity:
                return False
        return True


if __name__ == '__main__':
    # trips = [[2, 1, 5], [3, 3, 7]]
    # capacity = 4
    trips = [[2, 1, 5], [3, 5, 7]]
    capacity = 3  # true
    cls = Solution()
    print(cls.carPooling(trips, capacity))
