"""
这里有 n 个航班，它们分别从 1 到 n 进行编号。
有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi]
意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。

请你返回一个长度为 n 的数组 answer，里面的元素是每个航班预定的座位总数。

示例 1：
输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
输出：[10,55,45,25,25]
解释：
航班编号        1   2   3   4   5
预订记录 1 ：   10  10
预订记录 2 ：       20  20
预订记录 3 ：       25  25  25  25
总座位数：      10  55  45  25  25
因此，answer = [10,55,45,25,25]

示例 2：
输入：bookings = [[1,2,10],[2,2,15]], n = 2
输出：[10,25]
解释：
航班编号        1   2
预订记录 1 ：   10  10
预订记录 2 ：       15
总座位数：      10  25
因此，answer = [10,25]


提示：

1 <= n <= 2 * 10^4
1 <= bookings.n <= 2 * 10^4
bookings[i].n == 3
1 <= firsti <= lasti <= n
1 <= seatsi <= 10^4
"""
from typing import List

# todo 前缀和思想

# 方法1：暴力解法（代码复杂度太高，无法通过全部的测试用例）
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # 返回一个长度为 n 的数组 answer，里面的元素是每个航班预定的座位总数。
        # [i, j, k] 其实代表的是 第 i 站上来了 k 个人， 一直到 第 j 站都在飞机上，到第 j + 1 就不在飞机上了。
        # 所以第 i 站到第 j 站的每一站都会因此多 k 个人。
        ans = [0] * n

        for i, j, k in bookings:
            while i <= j:
                ans[i - 1] += k  # 航班编号从1到n
                i += 1
        return ans

# todo 方法2：前缀和思想（差分数组）
# 注意到方法1里层的 while 循环是连续的数组全部加上一个数字，不难想到可以利用母题 0 的前缀和思路优化。
# 一种思路就是在 i 的位置 + k， 然后利用前缀和的技巧给 [i..n] 的元素都  +k。
# 但是题目需要加的是一个区间， j + 1 及其之后的元素会被多加一个 k。
# 一个简单的技巧就是给 j + 1 的元素减去 k，这样正负就可以抵消。


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # 返回一个长度为 n 的数组 answer，里面的元素是每个航班预定的座位总数。
        ans = [0] * (n + 1)

        for i, j, k in bookings:
            ans[i] += k
            if j < n:
                ans[j+1] -= k

        for i in range(1, n + 1):
            ans[i] += ans[i - 1]
        return ans[1:]


'''
差分数列问题:
1.航班是从1~n进行编号,说明差分数列diffs的索引是0 ~ n-1
2.航班一开始是没人预定的,说明原始数组bookings和diffs都是[0] * (n-1)
3. 预订记录 bookings[i] = [firsti, lasti, seatsi] 
    - 前2个参数代表预定的航班编号区间[i，j],区间是左闭右闭
    - 第三个参数代表在[i，j]区间的航班要增加的预定人数,也就是inc
4.问题是返回一个长度为 n 的数组 answer，里面的元素是每个航班预定的座位总数。
    - 也就是差分数组类最后返回的结果
    
代码跟370题大同小异,只需要修改一下diffs索引
'''



class DiffArr:
    # 构建差分数组
    def __init__(self, nums: list):
        self.n = len(nums)
        self.diffs = [0] * self.n
        # 根据初始数组构造差分数组
        self.diffs[0] = nums[0]
        for i in range(1, self.n):
            self.diffs[i] = nums[i] - nums[i - 1]

    #  给闭区间 [i, j] 增加 inc（可以是负数）
    def update(self, i, j, inc):
        self.diffs[i] += inc
        # 当 j+1 >= diffs.n 时，说明是对 nums[i] 及以后的整个数组都进行修改，那么就不需要再给 diff 数组减 value 了。
        if j + 1 < self.n:
            self.diffs[j + 1] -= inc

    # 返回更新后的结果数组
    def result(self):
        res = [0] * self.n
        # 根据差分数组构造结果数组
        res[0] = self.diffs[0]
        for i in range(1, self.n):
            res[i] = res[i - 1] + self.diffs[i]
        return res


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # arr 初始化为全 0,
        arr = [0] * n
        # 构造差分解法
        df = DiffArr(arr)

        for i, j, inc in bookings:
            # todo 航班是从1~n编号,对应索引应该是0~n-1 !!
            df.update(i-1, j-1, inc)

        return df.result()


if __name__ == '__main__':
    cls = Solution()
    # 输出：[10,55,45,25,25]
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    print(cls.corpFlightBookings(bookings, n))
