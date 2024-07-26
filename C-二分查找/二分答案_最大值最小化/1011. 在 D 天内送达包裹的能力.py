"""
传送带上的包裹必须在 days 天内从一个港口运送到另一个港口。
传送带上的第 i 个包裹的重量为 w[i]。
1.每一天，我们都会按给出重量（w）的顺序往传送带上装载包裹。
2.我们装载的重量不会超过船的最大运载重量。

返回能在 days 天内将传送带上的所有包裹送达的船的最低运载能力。


示例 1：
输入：w = [1,2,3,4,5,6,7,8,9,10], days = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10
请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。

示例 2：
输入：w = [3,2,2,4,1,4], days = 3
输出：6
解释：
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4
示例 3：

输入：w = [1,2,3,1,1], days = 4
输出：3
解释：
第 1 天：1
第 2 天：2
第 3 天：3
第 4 天：1, 1


提示：
1 <= days <= w.n <= 5 * 10^4
1 <= w[i] <= 500
"""
from typing import List


# todo 二分搜索最大值最小化问题
class Solution2:
    # 二分查找写法1
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 在 days 天内将传送带上的所有包裹送达的船的最低运载能力的左右边界值
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            # 计算运载能力为mid时，送达包裹需要的天数
            # 运载能力越大，需要的天数越少
            need = self.check(weights, mid)
            if need > days:
                # 排除mid及mid左边
                left = mid + 1
            else:
                right = mid
        return left

    # 二分查找写法2
    def shipWithinDays2(self, weights: List[int], days: int) -> int:
        # 返回能在 days 天内将传送带上的所有包裹送达的船的最低运载能力。
        # 1 <= days <= w.length

        left = max(weights)  # 运载能力最低时, 需要的天数fv最多,如果fv > days, 继续减少fv,也就是增大v
        right = sum(weights)  # 这时候只需要1天就可以运完.题目days >= 1
        # 默认最小运载能力
        ans = right
        while left <= right:
            midV = left + (right - left) // 2
            need = self.check(weights, midV)
            if need > days:
                # 如果在限定天数运不完,需要减少fv,即增大v
                left = midV + 1
            elif need <= days:
                # 如果在限定天数可以运完,可以增大fv,即减小v
                # 这里可能是最终结果
                ans = midV
                right = midV - 1
        return ans

    # 计算运载能力为V时，需要的运载天数need:f(v) 单调递减函数
    def check(self, weights, maxCapacity) -> int:
        """返回最大运载能力为maxCapacity时，将所有包裹送达所需要的天数
        Capacity取值范围[max(w)..sum(w)]
        """
        # 货物必须按照给定的顺序装运, 最少需要一天
        need = 1
        # 船已经装载的货物总重量
        curItervalSum = 0
        for weight in weights:
            if curItervalSum + weight > maxCapacity:
                # 如果装下当前重量就超标，就需要多一天运送, 船载总量重新置0
                need += 1
                curItervalSum = 0
            curItervalSum += weight
        return need

    # 另外一种写法
    def check2(self, weights, v):
        # 按照题目要求,是按照weights列表顺序依次装货
        need = 0
        i = 0
        while i < len(weights):
            cap = v  # 尽可能多的装货物
            while cap > 0 and i < len(weights):
                if cap < weights[i]:
                    break
                elif cap >= weights[i]:
                    cap -= weights[i]
                i += 1
            need += 1

        return need


if __name__ == '__main__':
    # 输出：15
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5
    # print(shipWithinDays(w, days))

    print(calNeed2(weights, 15))
