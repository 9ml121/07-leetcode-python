"""
描述
现有n种砝码，重量互不相等，分别为 m1,m2,m3…mn ；
每种砝码对应的数量为 x1,x2,x3...xn 。现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。


注：
称重重量包括 0
数据范围：每组输入数据满足 1≤n≤10  ，1≤mi≤2000  ，

输入描述：
对于每组测试数据：
第一行：n --- 砝码的种数(范围[1,10])
第二行：m1 m2 m3 ... mn --- 每种砝码的重量(范围[1,2000])
第三行：x1 x2 x3 .... xn --- 每种砝码对应的数量(范围[1,10])
输出描述：
利用给定的砝码可以称出的不同的重量数

输入：
2
1 2
2 1

输出：
5

说明：
可以表示出0，1，2，3，4五种重量。
"""

"""
方法1:哈希set(推荐)
怎么去重，用set集合。

1.首先根据输入顺序，将砝码用数字序列表示，例如2个1g和1个2g，就用 1 1 2的序列表示；
2.set序列用来表示加入当前砝码之前能产生的重量种类；
3.set初始化为{0}；当第一个1g砝码放入时，则set中需要插入原先set中的所有元素+1g后的结果；即{0, 0+1};
4.当第二个1g加入时，则set会插入{0+1, 1+1},就变成了{0, 1, 2};
5.重复上述步骤加入所有砝码；则最后set的大小即为能产生的重量种类。
"""


def method1():
    n = 2
    m = [1, 2]
    x = [2, 1]
    amount = []  # 拥有的砝码总的集合
    for i in range(len(m)):
        for j in range(x[i]):
            amount.append(m[i])
    print(amount)
    # [1, 1, 2]

    weights = {0, }  # 不同砝码组合总的集合
    for i in amount:
        # set是可变数据类型，在循环遍历中更新会报错，用list方法相当于新建了一个列表
        for j in list(weights):
            weights.add(i + j)
    print(weights)
    # {0, 1, 2, 3, 4}
    ans = len(weights)
    print(ans)


method1()
"""
方法2：利用列表union方法
"""


def method02():
    n = 2
    m = [1, 2]
    x = [2, 1]
    # mx为所有砝码，比如示例mx为[1, 1, 2]
    mx, l = [], {0}
    for i in range(n):
        mx.extend([m[i]] * x[i])
    for i in mx:
        # 每次加一块砝码，使用union(并集)得到新去重的组合，如果不使用union则稍微麻烦一点，需要考虑循环中改变set
        l = l.union({i + j for j in l})
    print(len(l))
