"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/131019925?spm=1001.2014.3001.5501

题目描述
有若干个文件，使用刻录光盘的方式进行备份，假设每张光盘的容量是500MB，求使用光盘最少的文件分布方式

所有文件的大小都是整数的MB，且不超过500MB；文件不能分割、分卷打包

输入描述
一组文件大小的数据

输出描述
使用光盘的数量

备注
不用考虑输入数据不合法的情况；假设最多100个输入文件。

用例1
输入
100,500,300,200,400
输出
3
说明
(100,400),(200,300),(500) 3张光盘即可。

输入和输出内容都不含空格。

用例2
输入
1,100,200,300
输出
2
"""

# todo 考察二分查找 + 回溯算法（桶装球问题）
# 类似题型：
# C-回溯算法\划分k个等和子集问题\项目排期.py


# 输入
nums = list(map(int, input().split(',')))
# todo 这里降序排列是为了降低后面回溯算法的时间复杂度
nums.sort(reverse=True)
# print(nums)

# 输出：使用最少光盘数量


def check(buckets, idx):
    # k个桶，最大容量限制是500， 能否放满nums所有球
    if idx == len(nums):
        return True

    selected = nums[idx]
    for i in range(len(buckets)):
        # 剪枝
        if i > 0 and buckets[i] == buckets[i-1]:
            continue

        if buckets[i] + selected <= 500:
            buckets[i] += selected
            # todo 找到一种可以装满所有球的方法，就不用再尝试了
            if check(buckets, idx+1):
                return True
            # 如果不能装完所有球，就反悔
            buckets[i] -= selected

    return False


lo = 1
hi = len(nums)
ans = hi
while lo <= hi:
    mid = (lo+hi) >> 1
    buckets = [0] * mid
    if check(buckets, 0):
        ans = mid
        hi -= 1
    else:
        lo += 1
print(ans)
