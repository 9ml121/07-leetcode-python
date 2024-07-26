"""
题目描述
游戏里面，队伍通过匹配实力相近的对手进行对战。但是如果匹配的队伍实力相差太大，对于双方游戏体验都不会太好。
给定n个队伍的实力值，对其进行两两实力匹配，两支队伍实例差距在允许的最大差距d内，则可以匹配。

todo:要求在匹配队伍最多的情况下匹配出的各组实力差距的总和最小。

输入描述
第一行，n，d。队伍个数n。允许的最大实力差距d。
2<=n <=50
0<=d<=100
第二行，n个队伍的实力值空格分割。
0<=各队伍实力值<=100

输出描述
匹配后，各组对战的实力差值的总和。若没有队伍可以匹配，则输出-1。

用例
输入	6 30
    81 87 47 59 81 18
输出	57
说明
    18与47配对，实力差距29
    59与81配对，实力差距22
    81与87配对，实力差距6
    总实力差距29+22+6=57

输入	6 20
    81 87 47 59 81 18
输出	12
说明
    最多能匹配成功4支队伍。
    47与59配对，实力差距12，
    81与81配对，实力差距0。
    总实力差距12+0=12

输入	4 10
    40 51 62 73
输出	-1
    说明	实力差距都在10以上，
    没有队伍可以匹配成功。
"""

'''
难度：*****
题目解析
https://fcqian.blog.csdn.net/article/details/128794908
'''
# 输入获取
import sys

n, d = map(int, input().split())
arr = list(map(int, input().split()))


def getMaxCountMinSum(segment, index, abandon, total, minTotal):
    if index >= len(segment):
        if total < minTotal[0]:
            minTotal[0] = total
        return

    getMaxCountMinSum(segment, index + 2, abandon, total + segment[index], minTotal)

    if not abandon and len(segment) % 2 == 0:
        getMaxCountMinSum(segment, index + 1, True, total, minTotal)


# 算法入口
def getResult(n, d, arr):
    """
    :param n: 队伍个数n
    :param d: 允许的最大实力差距d
    :param arr: n个队伍的实力值数组
    :return: 匹配队伍最多的情况下匹配出的各组实力差距的总和最小
    """

    # 实力数组升序
    arr.sort()

    # ans记录各组实力差之和
    ans = 0

    # 此flag标记是否没有队伍可以匹配，true表示没有队伍可以匹配，此时应该返回-1
    flag = True

    # segment用于保存分段
    segment = []
    for i in range(1, n):
        # 相邻两队的实力差diff
        diff = arr[i] - arr[i - 1]

        # 如果diff大于d，那么说明 i - 1 无法和 i 组队匹配
        if diff > d:
            # 此时分段开始
            if len(segment) > 0:
                flag = False
                minTotal = [sys.maxsize]
                getMaxCountMinSum(segment, 0, False, 0, minTotal)  # 计算分段部分的组队匹配的：匹配队伍最多的情况下匹配出的各组实力差距的最小总和
                ans += minTotal[0]
                segment.clear()  # 开始记录新的分段
        else:
            # 如果diff不大于d，那么说明 i - 1 可以和 i 组队匹配，此时将实力差（相当于一个组队匹配）计入分段
            segment.append(diff)

    # 最后一个分段也要记得处理，上面逻辑无法将最后一个分段处理到
    if len(segment) > 0:
        flag = False
        minTotal = [sys.maxsize]
        getMaxCountMinSum(segment, 0, False, 0, minTotal)
        ans += minTotal[0]

    if flag:
        return -1

    return ans


# 算法调用
print(getResult(n, d, arr))