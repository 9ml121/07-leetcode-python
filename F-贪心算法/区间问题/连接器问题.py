"""
题目描述
有一组区间[a0，b0]，[a1，b1]，…（a，b表示起点，终点），区间有可能重叠、相邻，重叠或相邻则可以合并为更大的区间；
给定一组连接器[x1，x2，x3，…]（x表示连接器的最大可连接长度，即x>=gap），可用于将分离的区间连接起来，但两个分离区间之间只能使用1个连接器；

请编程实现使用连接器后，最少的区间数结果。

区间数量<10000，a,b均 <=10000
连接器梳理<10000；x <= 10000

输入描述
区间组：[1,10],[15,20],[18,30],[33,40]
连接器组：[5,4,3,2]

输出描述
    1

说明：
合并后：[1,10],[15,30],[33,40]，使用5, 3两个连接器连接后只剩下 [1, 40]。

用例
输入	[1,10],[15,20],[18,30],[33,40]
    [5,4,3,2]
输出	1
说明	合并后：[1,10], [15,30], [33,40]，使用5, 3两个连接器连接后只剩下[1,40]。

输入	[1,2],[3,5],[7,10],[15,20],[30,100]
    [5,4,3,2,1]
输出	2
说明	无重叠和相邻，使用1，2，5三个连接器连接后只剩下[1,20]，[30,100]
"""


# todo 单调递增栈问题


# 2.算法逻辑
def getResult(rans, cons):
    # todo 1 先对原区间升序排列
    rans.sort(key=lambda x: x[0])
    # todo 2.定义1个单调递增栈stack: 每次压入合并后的区间
    stack = [rans.pop(0)]
    # diffs数组记录两个区间的间隔
    diffs = []
    for ran in rans:
        s1, e1 = stack[-1]  # ran每次都是跟mergerRan栈顶区间比较
        s2, e2 = ran
        if s2 <= e1:   # 可以合并,栈顶更新为合并后的区间
            stack.pop()
            stack.append([s1, max(e1, e2)])
        elif s2 > e1:  # 不可以合并, 栈顶增加新区间(单调递增), 并且diffs记录两个区间的间隔
            diffs.append(s2 - e1)
            stack.append(ran)

    # todo 3. 将diffs和cons都降序排列, 然后二者进行匹配
    diffs.sort(reverse=True)
    cons.sort(reverse=True)
    while len(cons) > 0 and len(diffs) > 0:
        if cons.pop() >= diffs[-1]:  # 每次都弹出cons最小的跟diffs匹配,匹配上了,diffs就弹出该区间
            diffs.pop()

    ans = len(diffs) + 1  # diff最后剩下的,都是连不上的,加上全部连接上的一个区间,就是题目问的最少区间结果
    return ans


if __name__ == '__main__':
    # 1。获取输入
    # rans = eval('[' + input() + ']')
    # print(rans)
    rans = [[1, 10], [15, 20], [18, 30], [33, 40]]
    # cons = eval(input())
    cons = [5, 4, 3, 2]
    ans = getResult(rans, cons)
    print(ans)
