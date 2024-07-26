"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/127957656

题目描述
服务之间交换的接口成功率作为服务调用关键质量特性，某个时间段内的接口失败率使用一个数组表示，

数组中每个元素都是单位时间内失败率数值，数组中的数值为0~100的整数，

给定一个数值(minAverageLost)表示某个时间段内平均失败率容忍值，即平均失败率小于等于minAverageLost，

找出数组中最长时间段，如果未找到则直接返回NULL。

输入描述
输入有两行内容，第一行为{minAverageLost}，第二行为{数组}，数组元素通过空格(” “)分隔，

minAverageLost及数组中元素取值范围为0~100的整数，数组元素的个数不会超过100个。

输出描述
找出平均值小于等于minAverageLost的最长时间段，输出数组下标对，格式{beginIndex}-{endIndx}(下标从0开始)，

如果同时存在多个最长时间段，则输出多个下标对且下标对之间使用空格(” “)拼接，多个下标对按下标从小到大排序。

用例1
输入
1
0 1 2 3 4
输出
0-2
说明
输入解释：minAverageLost=1，数组[0, 1, 2, 3, 4]

前3个元素的平均值为1，因此数组第一个至第三个数组下标，即0-2

用例2
输入
2
0 0 100 2 2 99 0 2
输出
0-1 3-4 6-7
说明
输入解释：minAverageLost=2，数组[0, 0, 100, 2, 2, 99, 0, 2]

通过计算小于等于2的最长时间段为：

数组下标为0-1即[0, 0]，数组下标为3-4即[2, 2]，数组下标为6-7即[0, 2]，这三个部分都满足平均值小于等于2的要求，

因此输出0-1 3-4 6-7
"""

#  todo 前缀和 + 动态规划
# 输入
# (minAverageLost)表示某个时间段内平均失败率容忍值
limit = int(input())
# 行为{数组}：某个时间段内的接口失败率
nums = list(map(int, input().split()))

# 输出：找出平均值小于等于minAverageLost的最长时间段，输出数组下标对
n = len(nums)

preSum = [0] * (n+1)
# 0 1 2 3 4
# 0 1 3 6 10
for i in range(n):
    preSum[i+1] = preSum[i] + nums[i]


max_cnt = 0
ans = []
# 注意：包含单个元素 0-0
for l in range(n):
    for r in range(l, n):
        cnt = r - l + 1
        arrSum = preSum[r+1] - preSum[l]
        limit_num = limit * cnt
        if cnt >= max_cnt and arrSum <= limit_num:
            if cnt > max_cnt:
                max_cnt = cnt
                ans = [[l, r]]
            elif cnt == max_cnt:
                ans.append([l, r])

if not ans:
    print('NULL')
else:
    res = []
    for i, j in ans:
        res.append(f'{i}-{j}')
    print(' '.join(res))
