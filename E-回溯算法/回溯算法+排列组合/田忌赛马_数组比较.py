"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/135024242?csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22135024242%22%2C%22source%22%3A%22qfc_128220%22%7D

题目描述
给定两个只包含数字的数组a，b，调整数组 a 里面的数字的顺序，使得尽可能多的a[i] > b[i]。

数组a和b中的数字各不相同。

输出所有可以达到最优结果的a数组的结果。

输入描述
输入的第一行是数组 a 中的数字，其中只包含数字，每两个数字之间相隔一个空格，a数组大小不超过10。

输入的第二行是数组 b 中的数字，其中只包含数字，每两个数字之间相隔一个空格，b数组大小不超过10。

输出描述
输出所有可以达到最优结果的 a 数组的数量。

用例1
输入
11 8 20
10 13 7
输出
1
说明
最优结果只有一个，a = [11, 20, 8]，故输出1

用例2
输入
11 12 20
10 13 7
输出
2
说明
有两个a数组的排列可以达到最优结果，[12, 20, 11] 和 [11, 20, 12]，故输出2

用例3
输入
1 2 3
4 5 6
输出
6
说明
a无论如何都会全输，故a任意排列都行，输出所有a数组的排列，6种排法。

"""

# todo 考察有重复元素的排列组合 + 回溯算法
# 本题数量级不大，可以考虑暴力破解。即求解a数组的所有全排列
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_a.sort()  # 方便剪枝
n = len(arr_a)

# 求数组arr_a的有重复全排列


def dfs(path, vis, res):
    if len(path) == n:
        res.append(path[:])

    for i in range(n):
        if vis[i]:
            continue

        # todo 注意全排列重复元素剪枝技巧
        if i > 0 and arr_a[i] == arr_a[i-1] and not vis[i-1]:
            continue

        vis[i] = True
        path.append(arr_a[i])
        dfs(path, vis, res)
        path.pop()
        vis[i] = False


path = []
vis = [False] * n
res = []
dfs(path, vis, res)

max_bigger = 0
max_cnt = 0
for arr in res:
    bigger = 0
    for i in range(len(arr_b)):
        if arr[i] > arr_b[i]:
            bigger += 1

    if bigger > max_bigger:
        max_bigger = bigger
        max_cnt = 1
    elif bigger == max_bigger:
        max_cnt += 1

print(max_cnt)


# 优化解法：本题不需要我们输出具体排列，因此不用定义path记录全排列。
def dfs(level, vis, bigger):
    '''
    @level: 组合的数字个数
    @vis:标记数组元素是否已经使用
    @bigger:路径组合数比arr_b各位置大的位置个数
    @max_bigger:全局变量，所有组合数中，比arr_b各位置大的最多位置个数
    '''
    global ans, max_bigger
    if level == len(arr_a):
        if bigger > max_bigger:
            max_bigger = bigger
            ans = 1
        elif bigger == max_bigger:
            ans += 1  
        return

    for i in range(len(arr_a)):
        if vis[i]:
            continue

        # todo 注意全排列重复元素剪枝技巧
        if i > 0 and arr_a[i] == arr_a[i-1] and not vis[i-1]:
            continue

        vis[i] = True
        # 注意这里更新bigger技巧
        dfs(level+1, vis, bigger + 1 if arr_a[i] > arr_b[level] else bigger)
        vis[i] = False

level = 0
vis = [False] * len(arr_a)
bigger = 0
max_bigger = 0
ans = 0
dfs(level, vis, bigger)
print(ans)