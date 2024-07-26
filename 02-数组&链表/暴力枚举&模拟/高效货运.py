"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/134725218?spm=1001.2014.3001.5502

OJ用例
题解 - 高效货运 - Hydro

题目描述
老李是货运公司承运人，老李的货车额定载货重量为 wt。

现有两种货物：

货物 A 单件重量为 wa，单件运费利润为 pa
货物 B 单件重量为 wb，单件运费利润为 pb
老李每次发车时载货总重量刚好为货车额定的载货重量 wt，车上必须同时有货物 A 和货物 B ，货物A、B不可切割。

老李单次满载运输可获得的最高利润是多少？

输入描述
第一列输入为货物 A 的单件重量 wa

0 < wa < 10000
第二列输入为货物 B 的单件重量 wb

0 < wb < 10000
第三列输入为货车的额定载重 wt

0 < wt < 100000
第四列输入为货物 A 的单件运费利润 pa

0 < pa < 1000
第五列输入为货物 B 的单件运费利润 pb

0 < pb < 1000
输出描述
单次满载运输的最高利润

用例1
输入
10 8 36 15 7
输出
44
用例2
输入
1 1 2 1 1
输出
2
"""


# 看似背包问题，其实就是贪心算法


# 看似背包问题，其实就是贪心算法

# 输入
wa, wb, wt, pa, pb = map(int, input().split())
# print(wa, wb, wt, pa, pb)


# 老李单次满载运输可获得的最高利润是多少？
def main():
    # 车上必须同时有货物 A 和货物 B
    if wa + wb > wt:
        return 0

    remain = wt - (wa + wb)  # 剩余重量
    p = pa + pb  # 已获得利润

    # wa * x + wb * y = remain
    # pa * x + pb * y = ?
    # 枚举
    cnt_a = remain // wa
    max_p = 0
    # print(f'p={p}, remain={remain}, cnt_a={cnt_a}')
    # 老李每次发车时载货总重量刚好为货车额定的载货重量 wt
    for x in range(cnt_a + 1):
        if (remain - wa * x) % wb == 0:
            y = (remain - wa * x)//wb
            cur_p = pa * x + pb * y
            # print(f' x={x},y={y}, cur_p={cur_p}')
            max_p = max(max_p, cur_p)

    p += max_p

    return p


print(main())
