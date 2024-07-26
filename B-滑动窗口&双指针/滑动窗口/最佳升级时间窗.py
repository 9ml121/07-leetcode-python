"""
题目来源：https://blog.csdn.net/weixin_46257411/article/details/134643723

题目描述

有一套系统需升级，为减小系统升级期间的影响，需根据系统过去一段时间内的每小时平均访问数据，来预测最佳升级时间窗。

现给长度为168（7*24）的整数数组，表示一个周期（假设从周一00:00到周日24:00）的每小时历史数据，最佳升级时间窗选择规则如下：
1.时间窗内累计用户访问量必须不大于给定的容忍值。
2.时间窗必须是连续的x个小时，最大的x即为最佳升级时间窗，且不超过7*24.
3.时间窗允许跨周期，例如当前周期的第167小时到下一周期的第166小时，是一个长度为168的时间窗。

请计算最佳升级时间窗，并返回其开始时间和结束时间的数组下标。如果存在多个最佳升级时间窗，返回开始时间下标最小的一个。

解答要求

时间限制：1000ms，内存限制：256MB

输入
第一行为整数n，表示给定的升级影响的容忍值，取值范围：[0, 2^31]。
第二行为7*24个整数，表示一个周期（7*24）的每个小时用户访问量，每个值的范围：[0, 2^31]。

输出
两个整数，分别表示所计算出的最佳升级时间窗的开始时间下标（包含）和结束时间下标（包含），不存在时返回 -1 -1 。

样例

输入样例
6
1 2 3 4 5 6 7 8 9 10 11 12 12 11 10 9 8 7 6 5 4 3 2 1 1 2 3 4 5 6 7 8 9 10 11 12 12 11 10 9 8 7 6 5 4 3 2 1 1 2 3 4 5 6 7 8 9 10 11 12 12 11 10 9 8 7 6 5 4 3 2 1


输出样例
22 25
"""

# todo 不固定长度的滑窗


def get_best_time_window(nums:int, k:int):
    # 返回nums[l..r]窗口内的元素总和>k，且窗口长度最大的l和r, 有相同长度最大的返回下标最小的那个
    max_start = -1  # Initial value of -1 indicates no optimal time window found
    max_sz = 0
    
    total = 0

    l = 0
    for r, x in enumerate(nums):
        # 入
        total += x
        
        # 出
        while total >= k:
            total -= nums[l]
            l += 1

        # 更新ans
        sz = r - l + 1
        if sz > max_sz:
            max_sz = sz
            max_start = l

    # Check if the optimal time window was found
    if max_start == -1:
        return [-1, -1]
    else:
        return [max_start, max_start + max_sz - 1]


# Example usage
pv_by_hour_weekly = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1,
    # ... (remaining data)
]
pv_error_tolerance = 6
result = get_best_time_window(pv_by_hour_weekly, pv_error_tolerance)
print(*result)
