"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/128385627

题目描述
A公司准备对他下面的N个产品评选最差奖， 评选的方式是首先对每个产品进行评分，然后根据评分区间计算相邻几个产品中最差的产品。 评选的标准是依次找到从当前产品开始前M个产品中最差的产品，请给出最差产品的评分序列。

输入描述
第一行，数字M，表示评分区间的长度，取值范围是0<M<10000

第二行，产品的评分序列，比如[12,3,8,6,5]，产品数量N范围是-10000 < N <10000

输出描述
评分区间内最差产品的评分序列

用例1
输入
3
12,3,8,6,5
输出
3,3,5
说明
12,3,8 最差的是3

3,8,6 最差的是3

8,6,5 最差的是5
"""
import collections
# todo 滑动窗口 + 单调队列
# 类似：A-滑动窗口&双指针\滑动窗口+单调队列.py\239.滑动窗口最大值.py


# 输入
k = int(input())
nums = list(map(int, input().split(',')))

# 输出：区间内最差产品的评分序列
def main():
    dq = collections.deque()
    ans = []

    # 第一个窗口
    for i in range(k):
        # 维护dq非严格单调递增
        while dq and dq[-1] > nums[i]:
            dq.pop()
        dq.append(nums[i])

    ans.append(dq[0])

    # 后续窗口
    for i in range(k, len(nums)):
        # 先判断窗口移除元素是不是dq最小值
        if nums[i-k] == dq[0]:
            dq.popleft()

        # 维护dq非严格单调递增
        while dq and dq[-1] > nums[i]:
            dq.pop()
        dq.append(nums[i])

        ans.append(dq[0])

    print(','.join(map(str, ans)))
