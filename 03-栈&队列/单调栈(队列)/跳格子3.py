"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/135064109?spm=1001.2014.3001.5501

OJ用例
https://hydro.ac/d/HWOD2023/p/OD394/solution

题目描述
小明和朋友们一起玩跳格子游戏，

每个格子上有特定的分数 score = [1, -1, -6, 7, -17, 7]，

从起点score[0]开始，每次最大的步长为k，请你返回小明跳到终点 score[n-1] 时，能得到的最大得分。

输入描述
第一行输入总的格子数量 n

第二行输入每个格子的分数 score[i]

第三行输入最大跳的步长 k

输出描述
输出最大得分

备注
格子的总长度 n 和步长 k 的区间在 [1, 100000]
每个格子的分数 score[i] 在 [-10000, 10000] 区间中
用例1
输入
6
1 -1 -6 7 -17 7
2
输出
14
说明
输出最大得分数，小明从起点score[0]开始跳，第一次跳score[1],第二次跳到score[3],第三次跳到score[5]，因此得到的最大的得分是score[0] + score[1] + score[3] + score[5] = 14
"""
import collections

# todo 考察 滑动窗口 + 单调队列

# 输入
# 总的格子数量 n
n = int(input())
# 每个格子的分数 score[i]
score = list(map(int, input().split()))
# 最大跳的步长 k
k = int(input())

# 测试用例
# n = 6
# score = [1, -1, -6, 7, -17, 7]
# k = 2

# 输出：返回小明跳到终点 score[n-1] 时，能得到的最大得分
"""
假设第 i 个格子的最大得分为 dp[i]，那么存在如下递推公式：

dp[i] = max(dp[i-k], dp[i-k+1], ...., dp[i-2], dp[i-1]) + score[i]

可以发现，dp[i]的状态取决于 dp数组的 i-k ~ i-1 范围内的最大值状态。
即第 i 个格子想要最大得分，可以从第 i-k 到 第 i-1 个格子中选择一个最大得分的格子起跳。

因此本题难点就变成了：求一个数组的任意长度为k的子区间内的最大值。

高效的求解办法是利用单调队列，具体可以看：

LeetCode - 04-栈&队列/队列/239-滑动窗口最大值.py
"""

# 方法1.暴力解法（超时）

def main1():
    # dp[i]代表跳到第i个方格的最大的分
    dp = [0] * n
    dp[0] = score[0]
    for r in range(1, n):
        l = max(r-k, 0)
        # 每次用前k步最大的得分 + 当前得分
        dp[r] = max(dp[l:r]) + score[r]

    # print(dp)
    return dp[-1]


# 方法2.滑动窗口 + 单调队列
# 类似：# 类似：A-滑动窗口&双指针\滑动窗口+单调队列.py\239.滑动窗口最大值.py

def main():
    # dp[i]代表跳到第i个方格的最大的分
    dp = [0] * n
    dp[0] = score[0]
    
    # todo q保存前一个窗口单调递减的最大得分，窗口大小为k+1
    # 从起点score[0]开始，每次最大的步长为k
    q = collections.deque([dp[0]])
    
    
    # 第一个窗口
    for i in range(1, min(k+1, n)):
        dp[i] = score[i] + q[0]
        while q and q[-1] < dp[i]:  
            q.pop()  # 维护queue单调递减

        q.append(dp[i])

    # 后续窗口
    for i in range(k+1, n):
        # 先移除左窗口元素
        if dp[i-(k+1)] == q[0]:
            q.popleft()

        # 后面逻辑跟上面一样
        dp[i] = score[i] + q[0]
        while q and dp[i] > q[-1]:  # 非严格
            q.pop()

        q.append(dp[i])

    # print(dp)
    return dp[-1]

print(main())
