"""
题目描述
在第一人称射击游戏中，玩家通过键盘的A、S、D、W四个按键控制游戏人物分别向左、向后、向右、向前进行移动，从而完成走位。
假设玩家每按动一次键盘，游戏任务会向某个方向移动一步，如果玩家在操作一定次数的键盘并且各个方向的步数相同时，此时游戏任务必定会回到原点，则称此次走位为完美走位。
现给定玩家的走位（例如：ASDA），请通过更换其中"一段连续走位的方式"使得原走位能够变成一个完美走位。
其中待更换的连续走位可以是相同长度的任何走位。

请返回待更换的连续走位的最小可能长度。
如果原走位本身是一个完美走位，则返回0。

输入描述
输入为由键盘字母表示的走位s，例如：ASDA

输出描述
输出为待更换的连续走位的最小可能长度。

用例

输入：ASDW
输出：0
说明：已经是完美走位了

输入	WASDAASD
输出	1
说明	将第二个A替换为W，即可得到完美走位

输入	AAAA
输出	3
说明	将其中三个连续的A替换为WSD，即可得到完美走位

补充说明：
1、走位长度1 <= s.n <= 10^5
2、s.n 是 4 的倍数
3、s 中只含有 'A', 'S', 'D', 'W' 四种字符
"""

# 分析
'''
题目解析: 滑动窗口问题
题目要求，保持W,A,S,D字母个数平衡，即相等，如果不相等，可以从字符串中选取一段连续子串替换，来让字符串平衡。
比如：WWWWAAAASSSS
字符串长度12，W,A,S,D平衡的话，则每个字母个数应该是3个，而现在W,A,S各有4个，也就是说各超了1个。
因此我们应该从字符串中，选取一段包含1个W，1个A，1个S的子串，来替换为D。
而符合这种要求的子串可能很多，我们需要找出其中最短的，即WAAAAS。

本题其实就是求最小覆盖子串，同LeetCode - 76 最小覆盖子串
'''

# 1。获取输入
# s = input()
s = 'SWSAAASS'

dic_s = {}
for ch in s:
    dic_s[ch] = dic_s.get(ch, 0) + 1
# print(dic_s)
# {'S': 4, 'W': 1, 'A': 3}
avg = len(s) // 4
need = {}  # 需要替换的字符和个数
cnt = 0  # 需要替换的字符总个数
for ch in 'WSAD':
    dic_s.setdefault(ch, 0)
    if dic_s.get(ch) > avg:
        need[ch] = dic_s[ch] - avg
        cnt += need[ch]
# print(need)
# {'S': 2, 'A': 1}

# 需要再s中找到一个包含need所有数量的最小连续子字符串, 取代成缺少的字符
i = 0
min_len = len(s)
min_str = ''
for j, sj in enumerate(s):
    if need.get(sj) is not None:
        if need[sj] > 0:
            cnt -= 1
        need[sj] -= 1
    # 当cnt==0，代表已经找到符合子串，开始移动左窗口
    while cnt == 0:
        si = s[i]
        # 记录最小长度和结果
        if j - i + 1 < min_len:
            min_len = j - i + 1
            min_str = s[i:j+1]
        if need.get(si) is not None:
            if need[si] == 0:
                cnt += 1
            need[si] += 1
        i += 1

if min_len < len(s):
    print(min_len)
else:
    print(0)

print(min_str)