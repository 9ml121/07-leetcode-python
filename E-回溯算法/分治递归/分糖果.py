"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/126009910?ops_request_misc=&request_id=708c00c1e3604a3db4fd497ad612eb76&biz_id=&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~koosearch~default-1-126009910-null-null.268%5Ev1%5Econtrol&utm_term=%E5%88%86%E7%B3%96%E6%9E%9C&spm=1018.2226.3001.4450

题目描述
小明从糖果盒中随意抓一把糖果，每次小明会取出一半的糖果分给同学们。

当糖果不能平均分配时，小明可以选择从糖果盒中（假设盒中糖果足够）取出一个糖果或放回一个糖果。

小明最少需要多少次（取出、放回和平均分配均记一次），能将手中糖果分至只剩一颗。

输入描述
抓取的糖果数（<10000000000）：15

输出描述
最少分至一颗糖果的次数：5

用例1
输入
15
输出
5
说明
15+1=16;

16/2=8;

8/2=4;

4/2=2;

2/2=1;
"""

# 输入：抓取的糖果数
n = int(input())

"""
本题由于是每次折半，因此本题数量级即便很大，也不怕超时。

没有了超时的后顾之忧，本题，直接可以暴力逻辑求解，假设输入的是num，分配次数count初始为0，那么：

如果num % 2 == 0，则可以直接折半，此时分配次数count++， num /= 2
如果num % 2 !=0，则不可以直接折半，此时需要开两个分支：
    取出一个糖，即num += 1，然后分配次数count++，之后继续前面折半逻辑
    放回一个糖，即num -= 1，然后分配次数count++，之后继续前面折半逻辑
最终我们只需要在众多分支中，取最少的count即可。
"""

# 输出：小明最少需要多少次（取出、放回和平均分配均记一次），能将手中糖果分至只剩一颗。
def dfs(n, cnt):
    if n == 1:
        return cnt

    if n % 2 == 0:
        return dfs(n//2, cnt+1)
    else:
        return min(dfs(n+1, cnt+1), dfs(n-1, cnt+1))


print(dfs(n, 0))
