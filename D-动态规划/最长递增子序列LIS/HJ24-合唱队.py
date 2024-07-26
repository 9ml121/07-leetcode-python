"""
n 位同学站成一排，音乐老师要请最少的同学出列，使得剩下的 K 位同学排成合唱队形。
通俗来说，能找到一个同学，他的两边的同学身高都依次严格降低的队形就是合唱队形。
例子：
123 124 125 123 121 是一个合唱队形
123 123 124 122不是合唱队形，因为前两名同学身高相等，不符合要求
123 122 121 122不是合唱队形，因为找不到一个同学，他的两侧同学身高递减。

你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。

注意：不允许改变队列元素的先后顺序 且 不要求最高同学左右人数必须相等

数据范围： 1≤n≤3000

输入描述：
用例两行数据，第一行是同学的总数 n ，第二行是 n 位同学的身高，以空格隔开

输出描述：
最少需要几位同学出列

示例1
输入：
8
186 186 150 200 160 130 197 200

输出：
4

说明：
由于不允许改变队列元素的先后顺序，所以最终剩下的队列应该为186 200 160 130或150 200 160 130
"""

'''
方法1：动态规划
# 最长子序列问题
1.先找到每一个位置i左侧的最长上升子序列长度numL[i]：每一个位置左侧最长子序列长度等于其左侧比它小的所有位置的最长子序列长度中的最大值+1
2.再找到每一个位置i右侧的最长下降子序列长度numR[i]：每一个位置右侧最长子序列长度等于其右侧比它小的所有位置的最长子序列长度中的最大值+1
3.然后求出所有位置的最长序列长度=左侧最长子序列长度+右侧最长子序列长度-1（因为该位置被算了两次，所以减1）
4.然后用数目减去最长序列长度就是答案
'''
# 方法1：动态规划
# n = int(input())
# stack = list(map(int, input().split()))
lst = [2, 7, 3, 5, 6]
n = len(lst)


# 先找到每一个位置i左侧的最长上升子序列长度numL[i]：每一个位置左侧最长子序列长度等于其左侧比它小的所有位置的最长子序列长度中的最大值+1
# 最左边的数，左侧最长子序列长度等于1(包含自己）
def helper(lst):
    dp = [1] * len(lst)
    for i in range(1, len(lst)):
        for j in range(0, i):
            # if stack[j] < stack[i]:
            #     dp[i] = max(dp[j] + 1, dp[i])
            if lst[j] < lst[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
    return dp


# # 再找到每一个位置i右侧的最长下降子序列长度numR[i]：每一个位置右侧最长子序列长度等于其右侧比它小的所有位置的最长子序列长度中的最大值+1
# dp2 = [1] * n
# for i in range(n - 2, -1, -1):  # 3,2,1,0
#     for j in range(i + 1, n):  #
#         if stack[j] < stack[i]:
#             dp2[i] = max(dp2[j] + 1, dp2[j])
# print(dp2)

left_dp = helper(lst)
right_dp = helper(lst[::-1])[::-1]
# print(left_dp)
# print(right_dp)

# 3.然后求出所有位置的最长序列长度=左侧最长子序列长度+右侧最长子序列长度-1（因为该位置被算了两次，所以减1）
dp = [left_dp[i] + right_dp[i] - 1 for i in range(n)]
# print(dp)
# 4.然后用数目减去最长序列长度就是答案
res = n - max(dp)
print(res)


"""
方法2：二分法
二分法代替往回遍历的过程，时间复杂度是o(nlogn)。
二分法的过程为：首先创建数组arr=[ele_1]，ele_1是原序列第一个元素，然后从第二个元素开始从左至右遍历原序列
1. 如果ele_i > max(arr)，将ele_i加到arr最后
2. 如果ele_i <= max(arr)，用二分法找到arr中第一个比ele_i大（或相等）的元素并用ele_i替换
遍历完成后arr的长度即为最长递增子序列的长度（但arr不是最长递增子序列）。第二步替换是因为为遍历到的元素可能会有比ele_i大但比替换元素小的元素，比如原序列为[2,5,8,3,4,6]。
"""


def method2():
    import bisect
    def inc_max(l):
        dp = [1] * len(l)  # 初始化dp，最小递增子序列长度为1
        arr = [l[0]]  # 创建数组
        for i in range(1, len(l)):  # 从原序列第二个元素开始遍历
            if l[i] > arr[-1]:
                arr.append(l[i])
                dp[i] = len(arr)
            else:
                pos = bisect.bisect_left(arr, l[i])  # 用二分法找到arr中第一个比ele_i大（或相等）的元素的位置
                arr[pos] = l[i]
                dp[i] = pos + 1
        return dp

    # while True:
    #   try:
    # n = int(input())
    # s = list(map(int, input().split()))
    # n = 8
    # s = [186, 186, 150, 200, 160, 130, 197, 200]
    N = 6
    s = [2, 5, 8, 3, 4, 6]
    left_s = inc_max(s)  # 从左至右
    right_s = inc_max(s[::-1])[::-1]  # 从右至左
    sum_s = [left_s[i] + right_s[i] - 1 for i in range(len(s))]  # 相加并减去重复计算
    print(str(N - max(sum_s)))
    #   except:
    #       break