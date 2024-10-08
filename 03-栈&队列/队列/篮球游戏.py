"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/135391795

OJ用例
题解 - 篮球游戏 - Hydro

题目描述
幼儿园里有一个放倒的圆桶，它是一个线性结构，允许在桶的右边将篮球放入，可以在桶的左边和右边将篮球取出。

每个篮球有单独的编号，老师可以连续放入一个或多个篮球，小朋友可以在桶左边或右边将篮球取出，当桶只有一个篮球的情况下，必须从左边取出。

如老师按顺序放入1、2、3、4、5 共有 5 个编号的篮球，那么小朋友可以依次取出编号为1、2、3、4、5 或者 3、1、2、4、5 编号的篮球，无法取出 5、1、3、2、4 编号的篮球。

其中 3、1、2、4、5 的取出场景为：

连续放入1、2、3号
从右边取出3号
从左边取出1号
从左边取出2号
放入4号
从左边取出4号
放入5号
从左边取出5号
简答起见，我们以 L 表示左，R表示右，此时取出篮球的依次取出序列为“RLLLL”。

输入描述
每次输入包含一个测试用例：

第一行的数字作为老师依次放入的篮球编号
第二行的数字作为要检查是否能够按照放入的顺序取出给定的篮球的编号，其中篮球的编号用逗号进行分隔。
其中篮球编号用逗号进行分隔。

输出描述
对于每个篮球的取出序列，如果确实可以获取，请打印出其按照左右方向的操作取出顺序，如果无法获取则打印“NO”。

备注
1 ≤ 篮球编号，篮球个数 ≤ 200
篮球上的数字不重复
输出的结果中 LR 必须为大写
用例1
输入
4,5,6,7,0,1,2
6,4,0,1,2,5,7
输出
RLRRRLL
说明
篮球的取出顺序依次为“右、左、右、右、右、左、左”

用例2
输入
4,5,6,7,0,1,2
6,0,5,1,2,4,7
输出
NO
说明
无法取出对应序列的篮球

用例3
输入
1,2,3,4
1,2,3,5
输出
NO
说明
不存在编号为5的篮球，所以无法取出对应编号的数据
"""

# todo 考察双向队列
import collections

# 输入
# 老师依次放入的篮球编号
ipts = list(map(int, input().split(',')))
# 要检查是否能够按照放入的顺序取出给定的篮球的编号
opts = list(map(int, input().split(',')))

# 输出：请打印出其按照左右方向的操作取出顺序
# 模拟圆筒
dq = collections.deque()
ans = []

i = 0
for ip in ipts:
    # 老师总是从右边放球，一次可以放多个
    dq.append(ip)
    # 每放一个球，就检查当前圆筒两遍是不是要取出来的球
    while dq and i < len(opts):
        # 从左边取
        if opts[i] == dq[0]:
            dq.popleft()
            ans.append("L")
            i += 1
        # 从右边取
        elif opts[i] == dq[-1]:
            dq.pop()
            ans.append('R')
            i += 1
        # 本轮不能取
        else:
            break

# print(dq)
# 如果圆筒最后还有球，证明无法按照opts序列取球
print(''.join(ans) if not dq else 'NO')
