""" 
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/127711201

题目描述
开头和结尾都是元音字母（aeiouAEIOU）的字符串为元音字符串，其中混杂的非元音字母数量为其瑕疵度。比如:

“a” 、 “aa”是元音字符串，其瑕疵度都为0
“aiur”不是元音字符串（结尾不是元音字符）
“abira”是元音字符串，其瑕疵度为2
给定一个字符串，请找出指定瑕疵度的最长元音字符子串，并输出其长度，如果找不到满足条件的元音字符子串，输出0。

子串：字符串中任意个连续的字符组成的子序列称为该字符串的子串。

输入描述
首行输入是一个整数，表示预期的瑕疵度flaw，取值范围[0, 65535]。
接下来一行是一个仅由字符a-z和A-Z组成的字符串，字符串长度(0, 65535]。

输出描述
输出为一个整数，代表满足条件的元音字符子串的长度。

用例1
输入
0
asdbuiodevauufgh
输出
3

用例2
输入
2
aeueo
输出
0
"""


# todo 快慢双指针

# 输入
# 预期的瑕疵度flaw
flaw = int(input())
# 由字符a-z和A-Z组成的字符串，字符串长度(0, 65535]
s = input()

# 输出：指定瑕疵度的最长元音字符子串，并输出其长度
ans = 0
# 开头和结尾都是元音字母（aeiouAEIOU）的字符串为元音字符串
# todo 用一个数组统计s中各个元音字符的索引下标
yuan_idxs = [i for i in range(len(s)) if s[i] in 'aeiouAEIOU']


l = 0
r = 0
while r < len(yuan_idxs):
    # todo 计算s[l..r]的瑕疵度: 区间元音字符个数为r-l+1, 区间总长度为yuan_idxs[r] - yuan_idxs[l] + 1
    cur_flaw = (yuan_idxs[r] - yuan_idxs[l] + 1) - (r - l + 1)
    if cur_flaw > flaw: # 超过指定微瑕度，l右移
        l += 1
    elif cur_flaw < flaw: # 小于指定微瑕度，r右移
        r += 1
    else: # 等于指定微瑕度，更新最大长度，r右移
        ans = max(ans, yuan_idxs[r] - yuan_idxs[l] + 1)
        r += 1
print(ans)
