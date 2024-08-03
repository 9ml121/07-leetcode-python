"""
描述
Redraiment是走梅花桩的高手。Redraiment可以选择任意一个起点，从前到后，但只能从低处往高处的桩子走。他希望走的步数最多，你能替Redraiment研究他最多走的步数吗？

数据范围：每组数据长度满足 1≤n≤200  ， 数据大小满足 1≤value≤350


输入描述：
数据共2行，第1行先输入数组的个数，第2行再输入梅花桩的高度

输出描述：
输出一个结果

示例1
输入：
6
2 5 1 5 4 5

输出：
3

说明：
6个点的高度各为 2 5 1 5 4 5
如从第1格开始走,最多为3步, 2 4 5 ，下标分别是 1 5 6
从第2格开始走,最多只有1步,5
而从第3格开始走最多有3步,1 4 5， 下标分别是 3 5 6
从第5格开始走最多有2步,4 5， 下标分别是 5 6
所以这个结果是3。

"""

'''
方法1：动态规划
关于初始化
数组 dp 中存储着对应 nums 位置的桩最大次数，所以创建的时候默认为 1，因为当前桩本身就是一步。

关于状态转移方程
其中 nums[j] < nums[i]，即扫描 i 前面的桩，如果有比 i 小的话就使用状态转移方程 dp[i] = max(dp[i], dp[j] + 1)，
方程的意思是————如果前面某个桩（桩j）比 桩i 小，那么从那个桩踩上 桩i 的话自然就多了一步，我们拿这个踩完之后的步数 dp[j] + 1 跟当前存储的最大步数 dp[i] 比较一下，选个大的放进去。

时间复杂度：O(n^2)

方法论：
1。穷举法/暴力搜索
2。记忆话搜索/剪枝
3。将递归形式改写成更简洁的迭代形式
'''


def method1():
    # n, nums = int(input()), list(map(int, input().split()))
    n = 5
    # nums = [1, 5, 2, 4, 3]
    nums = [2, 5, 6, 4, 7]
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))


# 方法2：递归（带记忆）
# 时间复杂度：O(n * 2^n)
memo = {}

def L(nums, i):
    """返回从索引i开始，nums数组长度最长的递增子序列"""
    # 优化
    if i in memo:
        return memo[i]

    if i == len(nums) - 1:  # last number
        return 1

    max_len = 1
    for j in range(i + 1, len(nums) - 1):
        if nums[j] > nums[i]:
            max_len = max(L(nums, j) + 1, max_len)
    return max_len


def length_of_LIS(nums):
    return max(L(nums, i) for i in range(len(nums)))


nums = [1, 5, 2, 4, 3]
print(length_of_LIS(nums))
