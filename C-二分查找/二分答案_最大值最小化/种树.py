"""
题目描述
小明在直线的公路上种树，现在给定可以种树的坑位的数量和位置，以及需要种多少棵树苗，问树苗之间的最小间距是多少时，可以保证种的最均匀（两棵树苗之间的最小间距最大）？

输入描述
输入三行：

第一行：坑位的数量
第二行：坑位的位置
第三行：需要种植树苗的数量
输出描述
树苗之间的最小间距

用例
输入	    7
        1 3 6 7 8 11 13
        3
输出	    6
说明	3棵树苗分别种植在1，7，13位置的坑位时，树苗种植的最均匀，最小间距为6
"""

'''
分析：
两棵树苗之间的最小间距最大？
'''
# 1.获取输入
n = 7  # 坑位的数量
pos = [1, 3, 6, 7, 8, 11, 13]  # 坑位的位置
k = 3  # 需要种植树苗的数量
ans = 1  # 树苗之间的最小间距

# 先排序
pos.sort()
# k个树之间的最大间距和最小间距
maxDis = pos[-1] - pos[0]
minDis = 1


# 判断pos在间距最小间距为dis时，是否能种下k棵树？
def check(pos, k, dis):
    # 第一个位置先种一颗
    cnt = 1
    curPos = pos[0]
    # 统计总共能种几个树
    for i in range(1, len(pos)):
        if pos[i] >= curPos + dis:
            cnt += 1
            curPos = pos[i]

        if cnt >= k:
            return True
    return False


# B-二分查找
while minDis <= maxDis:
    # 先尝试中间间距
    mid = (maxDis + minDis) // 2
    # pos在间距最小间距为mid时，是否能种下k棵树？
    if check(pos, k, mid):
        ans = mid
        minDis = mid + 1
    else:
        maxDis = mid - 1

print(ans)