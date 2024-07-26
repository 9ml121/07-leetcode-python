"""
MP3 Player因为屏幕较小，显示歌曲列表的时候每屏只能显示几首歌曲，用户要通过上下键才能浏览所有的歌曲。为了简化处理，假设每屏只能显示4首歌曲，光标初始的位置为第1首歌。
现在要实现通过上下键控制光标移动来浏览歌曲列表，控制逻辑如下：
    歌曲总数<=4的时候，不需要翻页，只是挪动光标位置。
    光标在第一首歌曲上时，按Up键光标挪到最后一首歌曲；
    光标在最后一首歌曲时，按Down键光标挪到第一首歌曲。

输入描述：
输入说明：
1 输入歌曲数量
2 输入命令 U或者D

输出描述：
输出说明
1 输出当前列表
2 输出当前选中歌曲

输入：
10
UUUU

输出：
7 8 9 10
7
"""

# 歌曲数量[1,150]
n = int(input())
# 命令长度【1，100】
ops = input()

# 光标初始位置为第1首歌
index = 1
# 初始页面
page = []

# 1.只有4首以下歌
if 1 <= n <= 4:
    # 当前页面是固定不变的，只要挪动光标位置
    page = range(1, n + 1)
    for op in ops:
        if op == "U":
            # 光标在第一个，按向上光标返回最后一个
            if index == 1:
                index = n
            # 其他情况下用户按Up键，光标挪到上一首歌曲；用户按Down键，光标挪到下一首歌曲
            else:
                index -= 1
        elif op == "D":
            # 光标在最后一个，按向下光标返回第一个
            if index == n:
                index = 1
            else:
                index += 1

# 2.歌曲总数大于4
elif n > 4:
    # 初始页面列表
    page = [1, 2, 3, 4]
    for op in ops:
        if op == "U":
            # 2.1 特殊翻页
            # 光标在第一首歌曲上，用户按Up键后，屏幕要显示最后一页,同时光标放到最后一首歌上
            if index == 1:
                index = n
                page = range(index - 3, index + 1)
            # 2.2 一般翻页
            # 屏幕显示的不是第一页时，光标在当前屏幕显示的第一首歌曲时，用户按Up键后，屏幕从当前歌曲的上一首开始显示，光标也挪到上一首歌曲
            elif index == page[0]:
                index -= 1
                page = range(index, index + 4)
            # 2.3 其他情况，不用翻页，只是挪动光标就行。
            else:
                index -= 1

        elif op == "D":
            # 屏幕显示最后一页时，光标在最后一首歌曲上，用户按Down键，屏幕要显示第一页，光标挪到第一首歌上
            if index == n:
                index = 1
                page = [1, 2, 3, 4]
            # 光标在当前屏幕显示的最后一首歌曲时，用户按Down键后，屏幕从当前歌曲的第二首开始显示，光标也挪到下一首歌曲
            elif index == page[-1]:
                index += 1
                page = range(index - 3, index + 1)
            # 2.3 其他情况，不用翻页，只是挪动光标就行。
            else:
                index += 1

print(*page)
print(index)
