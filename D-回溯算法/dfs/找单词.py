"""
https://fcqian.blog.csdn.net/article/details/127711515
题目描述
给一个字符串和一个二维字符数组，如果该字符串存在于该数组中，则按字符串的字符顺序输出字符串每个字符所在单元格的位置下标字符串，如果找不到返回字符串“N”。

1.需要按照字符串的字符组成顺序搜索，且搜索到的位置必须是相邻单元格，其中“相邻单元格”是指那些水平相邻或垂直相邻的单元格。

2.同一个单元格内的字母不允许被重复使用。

3.假定在数组中最多只存在一个可能的匹配。

输入描述
第1行为一个数字N指示二维数组在后续输入所占的行数。

第2行到第N+1行输入为一个二维大写字符数组，每行字符用半角,分割。

第N+2行为待查找的字符串，由大写字符组成。

二维数组的大小为N*N，0<N<=100。

单词长度K，0<K<1000。

输出描述
输出一个位置下标字符串，拼接格式为：第1个字符行下标+”,”+第1个字符列下标+”,”+第2个字符行下标+”,”+第2个字符列下标… +”,”+第N个字符行下标+”,”+第N个字符列下标。

用例
输入	
4
A,C,C,F
C,D,E,D
B,E,S,S
F,E,C,A
ACCESS
输出	0,0,0,1,0,2,1,2,2,2,2,3
说明	ACCESS分别对应二维数组的[0,0] [0,1] [0,2] [1,2] [2,2] [2,3]下标位置。

"""

# 类似题型：
# 1.leetcode 79. 单词搜索.py
# 2.加密算法、特殊的加密算法.py
# 3.华为OD机试 - 单词搜索：https://blog.csdn.net/qfc_128220/article/details/127711035?spm=1001.2014.3001.5501


# 输入
# 输入行数
n = int(input())
# 字符数组, 二维数组的大小为N*N
grid = [input().split(',') for _ in range(n)]
# 要查找的字符串
word = input()
# print(grid)

# 输出：位置下标字符串
ans = []
used = set()


def main():
    for i in range(n):
        for j in range(n):
            if check(i, j, 0):
                return ','.join(ans)
    # 如果找不到返回字符串“N”。
    return 'N'


offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def check(i, j, idx):
    if not (0 <= i < n and 0 <= j < n) or (i, j) in used:
        return False

    if grid[i][j] != word[idx]:
        return False

    ans.append(f'{i},{j}')
    used.add((i, j))
    if idx == len(word)-1:
        return True

    for ox, oy in offsets:
        new_x = i + ox
        new_y = j + oy

        if check(new_x, new_y, idx+1):
            return True
    # 回溯
    ans.pop()
    used.remove((i, j))
    return False


print(main())
