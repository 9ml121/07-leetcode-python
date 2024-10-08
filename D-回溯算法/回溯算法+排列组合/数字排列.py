"""
题目描述
小明负责公司年会，想出一个趣味游戏：

屏幕给出 1 ~ 9 中任意 4 个不重复的数字，大家以最快时间给出这几个数字可拼成的数字从小到大排列位于第 N 位置的数字，其中 N 为给出数字中最大的（如果不到这么多数字则给出最后一个即可）。

注意：

2 可以当作 5 来使用，5 也可以当作 2 来使用进行数字拼接，且屏幕不能同时给出 2 和 5；
6 可以当作 9 来使用，9 也可以当作 6 来使用进行数字拼接，且屏幕不能同时给出 6 和 9。
如给出：1，4，8，7，则可以拼接的数字为：

1，4，7，8，14，17，18，41，47，48，71，74，78，81，84，87，147，148，178 ... (省略后面的数字)

那么第 N （即8）个的数字为 41。

输入描述
输入以逗号分隔的 4 个 int 类型整数的字符串。

输出描述
输出为这几个数字可拼成的数字从小大大排列位于第 N （N为输入数字中最大的数字）位置的数字，

如果输入的数字不在范围内或者有重复，则输出-1。

用例
输入	1,4,8,7
输出	41
说明	
可以构成的数字按从小到大排序为：

1，4，7，8，14，17，18，41，47，48，71，74，78，81，84，87，147，148，178  ... （省略后面的数字），

故第8个为41

输入	2,5,1
输出	-1
说明	2和5不能同时出现

输入	3,0,9
输出	-1
说明	0不在1到9范围内

输入	3,9,7,8
输出	39
说明	
注意9可以当6使用，所以可以构成的数字按从小到大排序为：3，6，7，8，9，36，37，38，39，63，67，68，73，76，78，79，83 ... （省略后面的数字），

故第9个为39
"""

# todo 考察全排列， 参考：C-回溯算法/排列&组合&子集/46. 全排列.py
# 输入
f4 = list(map(int, input().split(',')))

# 输出：从小到大第N大的数子，错误输入输出-1
def main():
    # 错误输入
    f4.sort()
    f4_set = set(f4)
    if len(f4_set) != 4 or f4[0] < 1 or f4[3] > 9:
        return -1

    if {2, 5}.issubset(f4_set) or {6, 9}.issubset(f4_set):
        return -1

    k = f4[-1]

    res = []
    vis = [False] * 4
    dfs(vis, 0, res)

    res.sort()
    # print(res)
    return res[k-1]


maps = {2: 5, 5: 2, 6: 9, 9: 6}


def dfs(vis, path, res):
    if path > 0:
        res.append(path)

    for i in range(4):
        if vis[i]:
            continue
        vis[i] = True
        path = path * 10 + f4[i]
        dfs(vis, path, res)
        path = (path - f4[i])//10

        if f4[i] in maps:
            path = path * 10 + maps[f4[i]]
            dfs(vis, path, res)
            path = (path - maps[f4[i]])//10

        vis[i] = False


print(main())
