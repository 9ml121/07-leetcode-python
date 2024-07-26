"""
描述
把m个同样的苹果放在n个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？
注意：如果有7个苹果和3个盘子，（5，1，1）和（1，5，1）被视为是同一种分法。

数据范围：0≤m≤10 ，1≤n≤10 。

输入描述：
输入两个int整数

输出描述：
输出结果，int型

输入：
7 3

输出：
8
"""

"""
题目分析
题目给我们苹果的数量m和盘子的数量n
要将苹果放在盘子里，可以允许空盘，问有多少种放置方案
但是盘子顺序是可以任意调换的，调换前后认为是同一种放置方案

方法1：D-动态规划
使用动态规划思想求解，记 dp[i][j] 表示使用 i 个苹果放入到 j 个盘子的方案数。

1 若 i<j，即苹果比盘子数小
    比如将 2 个苹果放入 3 个盘子，必然会有一个盘子为空，即{0,x,y}，其中一位固定为 0，不会影响最终的方案数，
    这和将 2 个苹果放入 2 个盘子的方案数目是一样的，即 {x,y}
    因此有当 i<j 时，dp[i][j] = dp[i][i]
2 若 i>=j，即苹果数目不小于盘子数时，考虑是否允许有空盘子（比如将 4 个苹果放入 3 个盘子）
    若允许有空盘，相当于盘子数量少一个（因为固定认为是空盘，不会影响最终方案数目），即 {x,y,0}，这对应着 dp[i][j-1]
    若不允许有空盘，对于 j 个盘子，相当于拿出来 j 个苹果，分配到每个盘子中，保证每个盘子分配到一个苹果，这对应着 dp[i−j][j]
    因此有当 i>=j 时，dp[i][j] = dp[i][j-1] + dp[i−j][j]
3 边界条件
    对于只有 1 个盘子的情况，分配方案只有 1 种，dp[i][1] = 1;
    对于只有 0 个苹果的情况，分配方案只有 1 种，dp[0][j] = 1;
    对于只有 1 个苹果的情况，分配方案只有 1 种，dp[1][j] = 1;

复杂度分析
时间复杂度：O(mn)，双重循环的时间开销
空间复杂度：O(mn)，动态规划矩阵的空间开销

"""


def solution(m, n):  # 苹果的数量m和盘子的数量n
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(m + 1):
        dp[i][1] = 1  # 如果只有一个盘子则只有一种放置方案
    for j in range(1, n + 1):
        dp[0][j] = 1  # 如果没有苹果则只有一种放置方案
        dp[1][j] = 1  # 如果只有一个苹果也相当于只有一种方案
    for i in range(2, m + 1):
        for j in range(2, n + 1):
            if i < j:
                # 如果苹果数量少，则盘子一定会空，所以去除那些空的盘子其实不影响方案数
                dp[i][j] = dp[i][i]
            else:
                # 如果苹果数量多，则考虑是否要装够j个盘子，如果不装够则有dp[i][j-1]，
                # 如果装够则相当于从所有盘子同时去掉一个苹果无影响，则有dp[i-j][j]
                dp[i][j] = dp[i - j][j] + dp[i][j - 1]

    return dp[m][n]


while True:
    try:
        m, n = map(int, input().split())
        print(solution(m, n))
    except:
        break

"""
方法一：递归
设f(m,n) 为m个苹果，n个盘子的放法数目，则先对n作讨论，
当n>m：必定有n-m个盘子永远空着，去掉它们对摆放苹果方法数目不产生影响。即if(n>m) f(m,n) = f(m,m)　　
当n<=m：不同的放法可以分成两类：
1、有至少一个盘子空着，即相当于f(m,n) = f(m,n-1);
2、所有盘子都有苹果，相当于可以从每个盘子中拿掉一个苹果，不影响不同放法的数目，即f(m,n) = f(m-n,n).
而总的放苹果的放法数目等于两者的和，即 f(m,n) =f(m,n-1)+f(m-n,n)

递归出口条件说明：
    当n=1时，所有苹果都必须放在一个盘子里，所以返回１；
    当没有苹果可放时，定义为１种放法；
递归的两条路，第一条n会逐渐减少，终会到达出口n==1;
第二条m会逐渐减少，因为n>m时，我们会return f(m,m)　所以终会到达出口m==0．

复杂度分析
时间复杂度： O(2^n)，画出递归树，执行时间复杂度即为(同斐波拉契数列）
空间复杂度：O(n)，递归栈的深度。
"""


def method1():
    def count(m, n):
        if m == 0 or n == 1:
            return 1
        elif n > m:
            return count(m, m)
        else:
            return count(m, n - 1) + count(m - n, n)

    while True:
        try:
            num = input().split()  # ['7','3']
            apple = int(num[0])
            disk = int(num[1])
            print(count(apple, disk))  # 函数返回值不可以直接写count(apple,disk)
        except:
            break
