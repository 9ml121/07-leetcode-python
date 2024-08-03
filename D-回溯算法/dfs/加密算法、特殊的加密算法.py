"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/134708077?csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22134708077%22%2C%22source%22%3A%22qfc_128220%22%7D

题目描述
有一种特殊的加密算法，明文为一段数字串，经过密码本查找转换，生成另一段密文数字串。

规则如下：

明文为一段数字串由 0~9 组成

密码本为数字 0~9 组成的二维数组

需要按明文串的数字顺序在密码本里找到同样的数字串，密码本里的数字串是由相邻的单元格数字组成，上下和左右是相邻的，注意：对角线不相邻，同一个单元格的数字不能重复使用。

每一位明文对应密文即为密码本中找到的单元格所在的行和列序号（序号从0开始）组成的两个数宇。

如明文第 i 位 Data[i] 对应密码本单元格为 Book[x][y]，则明文第 i 位对应的密文为X Y，X和Y之间用空格隔开。

如果有多条密文，返回字符序最小的密文。

如果密码本无法匹配，返回"error"。

请你设计这个加密程序。

示例1：

密码本：

0 0 2

1 3 4

6 6 4

明文："3"，密文："1 1"

示例2：

密码本：

0 0 2

1 3 4

6 6 4

明文："0 3"，密文："0 1 1 1"

示例3：

密码本：

0 0 2 4

1 3 4 6

3 4 1 5

6 6 6 5

明文："0 0 2 4"，密文："0 0 0 1 0 2 0 3" 和 "0 0 0 1 0 2 1 2"，返回字典序最小的"0 0 0 1 0 2 0 3"

明文："8 2 2 3"，密文："error"，密码本中无法匹配

输入描述
第一行输入 1 个正整数 N，代表明文的长度（1 ≤ N ≤ 200）

第二行输入 N 个明文组成的序列 Data[i]（0 ≤ Data[i] ≤ 9）

第三行输入 1 个正整数 M，代表密文的长度

接下来 M 行，每行 M 个数，代表密文矩阵

输出描述
输出字典序最小密文，如果无法匹配，输出"error"

用例1
输入
2
0 3
3
0 0 2
1 3 4
6 6 4
输出
0 1 1 1
用例2
输入
2
0 5
3
0 0 2
1 3 4
6 6 4
输出
error
说明
找不到 0 5 的序列，返回error


"""


# 获取输入
n_data = int(input())
datas = list(map(int, input().split()))
n_book = int(input())
books = [list(map(int, input().split())) for _ in range(n_book)]

# 算法
# 深搜的优先级应该是：上 > 左 > 右 > 下
offsets = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # 遍历顺序不能变


def dfs(x, y, idx, vis, path):
    if idx == n_data:
        return True

    for ox, oy in offsets:
        new_x = x+ox
        new_y = y+oy
        if not (0 <= new_x < n_book and 0 <= new_y < n_book):
            continue
        if (new_x, new_y) in vis:
            continue
        if books[new_x][new_y] != datas[idx]:
            continue

        vis.add((new_x, new_y))
        path.append(f'{new_x} {new_y}')
        # todo 如果当前分支可以找到符合要求的路径，则返回
        if dfs(new_x, new_y, idx+1, vis, path):
            return True

        # 否则，回溯
        path.pop()
        vis.remove((new_x, new_y))

    return False


def solution():
    for i in range(n_book):
        for j in range(n_book):
            if books[i][j] == datas[0]:
                vis = {(i, j)}
                path = [f'{i} {j}']
                if dfs(i, j, 1, vis, path):
                    return ' '.join(path)
    return 'error'


print(solution())

