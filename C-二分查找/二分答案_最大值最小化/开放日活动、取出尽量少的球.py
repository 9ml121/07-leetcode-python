"""
题目描述
某部门开展Family Day开放日活动，其中有个从桶里取球的游戏，游戏规则如下：
有N个容量一样的小桶等距排开，
且每个小桶都默认装了数量不等的小球，
每个小桶装的小球数量记录在数组 bucketBallNums 中，
游戏开始时，要求所有桶的小球总数不能超过SUM，
如果小球总数超过SUM，则需对所有的小桶统一设置一个容量最大值 maxCapacity，
并需将超过容量最大值的小球拿出来，直至小桶里的小球数量小于 maxCapacity;

请您根据输入的数据，计算从每个小桶里拿出的小球数量。

限制规则一：
1.所有小桶的小球总和小于SUM，则无需设置容量值maxCapacity，并且无需从小桶中拿球出来，返回结果[]

限制规则二：
2.如果所有小桶的小球总和大于SUM，则需设置容量最大值maxCapacity，并且需从小桶中拿球出来，返回从每个小桶拿出的小球数量组成的数组；

输入描述
第一行输入2个正整数，数字之间使用空格隔开，其中第一个数字表示SUM，第二个数字表示bucketBallNums数组长度；
第二行输入N个正整数，数字之间使用空格隔开，表示bucketBallNums的每一项；

输出描述
找到一个maxCapacity，来保证取出尽量少的球，并返回从每个小桶拿出的小球数量组成的数组。

备注
1 ≤ bucketBallNums[i] ≤ 10^9
1 ≤ bucketBallNums.n = n ≤ 10^5
1 ≤ maxCapacity ≤ 10^9
1 ≤ SUM ≤ 10^9

用例
输入	14 7
        2 3 2 5 5 1 4
输出	[0,1,0,3,3,0,2]
    说明	小球总数为22，SUM=14，超出范围了，需从小桶取球，
    maxCapacity=1，取出球后，桶里剩余小球总和为7，远小于14
    maxCapacity=2，取出球后，桶里剩余小球总和为13，
    maxCapacity=3，取出球后，桶里剩余小球总和为16，大于14
    因此maxCapacity为2 ，每个小桶小球数量大于2的都需要拿出来；

输入	3 3
        1 2 3
输出	[0,1,2]
说明	小球总数为6，SUM=3，超出范围了，需从小桶中取球，maxCapacity=1，则小球总数为3，从1号桶取0个球，2号桶取1个球，3号桶取2个球；

输入	6 2
    3 2
输出	[]
说明	小球总数为5，SUM=6，在范围内，无需从小桶取球；
"""

# todo 最小值最大华问题
# 2 算法逻辑
def getResult(nums: list, limit: int):
    n = len(nums)
    # 题目问题是:找到一个maxCapacity，来保证取出尽量少的球，取出球之后,总和跟limit最接近,但不大于limit,
    # 计算从每个小桶里拿出的小球数量。
    # 1.所有小桶的小球总和小于limit，则无需设置容量值maxCapacity，并且无需从小桶中拿球出来，返回结果[]
    befor = sum(nums)
    if befor <= limit:
        return []

    # 2.如果所有小桶的小球总和大于limit，则需设置容量最大值maxCapacity，并且需从小桶中拿球出来，返回从每个小桶拿出的小球数量组成的数组；
    # 已知: 7个桶, 所有球数量最大限制limit是14,
    # 如果限制是1, 最后最多有7个球; 限制为2,最多有14个球,限制为3,最多是21个球
    # 由此可以看出,最低限制数量为limit//n(向下取整)
    # 最多限制数量是nums中最大数, 也就是不用取球,但是这样小球总和肯定是比limit大
    min_maxCap = limit // n  # 2
    max_maxCap = max(nums)  # 5

    # 常规方法可以从min_maxCap开始,限制数量循环加1,直到球的总数大于limit,边界就是循环的最后一次
    # 这里尝试二分. 先从中间试  [2, 3, 2, 5, 5, 1, 4]
    ans = []  # 最终答案
    while min_maxCap <= max_maxCap:  # 最终状态[3,2]
        mid = min_maxCap + (max_maxCap - min_maxCap) // 2  # 3
        # print(mid)
        # 求剩下的球总数: 刚开始的球总数 - 取出的球数量
        pop = list(map(lambda num: num - mid if num > mid else 0, nums))
        # print(pop)
        remain = befor - sum(pop)
        # print(remain)  # 17
        if remain == limit:  # limit = 14
            return pop  # 找到了答案
        elif remain > limit:
            # 需要缩小容量限制,这样取出的球就更多, 剩下的球就越少
            max_maxCap = mid - 1  # 闭区间
        elif remain < limit:
            # 需要增大容量限制,这样取出的球就更少, 剩下的球就越多
            # 题目要求是最后剩余的球不大于limit,所以这里也可能产生最后的结果,需要记录
            ans = pop
            min_maxCap = mid + 1  # 闭区间
    return ans


if __name__ == '__main__':
    """
    输入	14 7
    2 3 2 5 5 1 4
    输出	[0,1,0,3,3,0,2]
    """
    # 1 获取输入
    # 桶个数n 所有小球总数限制limit
    # limit, n = map(int, input().split())
    # 每个桶里小球个数
    # nums = list(map(int, input().split()))
    # print(nums)
    nums = [2, 3, 2, 5, 5, 1, 4]
    limit = 14
    print(getResult(nums, limit))
