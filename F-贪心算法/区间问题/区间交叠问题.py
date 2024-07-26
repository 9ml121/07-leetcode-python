"""
题目描述
给定坐标轴上的一组线段，线段的起点和终点均为整数并且长度不小于1，请你从中找到最少数量的线段，这些线段可以覆盖柱所有线段。

输入描述
第一行输入为所有线段的数量，不超过10000，后面每行表示一条线段，格式为"x,y"，x和y分别表示起点和终点，取值范围是[-10^5，10^5]。

输出描述
最少线段数量，为正整数

用例
输入
3
1,4
2,5
3,6

输出	2
说明	无
"""


# todo 单调递增栈问题


# 2.算法逻辑
def getResult(rans):
    rans.sort(key=lambda x: x[0])
    # todo 这里定义的其实就是一个单调递增栈
    stack = [rans.pop(0)]  # 先把第一个区间压栈, 栈里面区间个数就是最后需要的最少线段
    for i, j in rans:
        # rans里面每个区间和stack顶部区间top做比较
        topi, topj = stack[-1]
        # 1.先判断两个区间右值
        if j <= topj:  # top完全包含ran[i], 就不用压栈
            continue
        elif j > topj:
            # 2.top不完全包含, 此时判断rans[i]左值
            if i >= topj:  # 2.1 两个线段没有交集, ran[i]完整压栈
                stack.append([i, j])
            elif i < topj:
                if i > topi:  # 2.2 两个线段有交集,只需要压入ran[i]超出的部分
                    stack.append([topj, j])
                elif i <= topi:  # 2.3. ran[i]完全包含top, stack先弹出,后压栈
                    stack.pop()
                    stack.append([topi, j])
    print(stack)
    # [[0, 4], [4, 7], [7, 8], [10, 12], [12, 14]]
    return len(stack)


if __name__ == '__main__':
    # 1.获取输入
    # n = int(input())
    n = 3
    # ranges = [list(map(int, input().split(','))) for _ in range(n)]
    # print(ranges)
    # rans = [[1, 4], [2, 5], [3, 6]]
    rans = [[0, 4], [1, 2], [1, 4], [3, 7], [6, 8], [10, 12], [11, 13], [12, 14]]
    # rans = [[1, 10], [5, 12], [8, 11]]
    ans = getResult(rans)
    print(ans)
