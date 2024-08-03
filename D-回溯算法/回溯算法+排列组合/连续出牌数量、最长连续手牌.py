"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/127711078

题目描述
有这么一款单人卡牌游戏，牌面由颜色和数字组成，颜色为红、黄、蓝、绿中的一种，数字为0-9中的一个。游戏开始时玩家从手牌中选取一张卡牌打出，接下来如果玩家手中有和他上一次打出的手牌颜色或者数字相同的手牌，他可以继续将该手牌打出，直至手牌打光或者没有符合条件可以继续打出的手牌。

现给定一副手牌，请找到最优的出牌策略，使打出的手牌最多。

输入描述
输入为两行

第一行是每张手牌的数字，数字由空格分隔，
第二行为对应的每张手牌的颜色，用r y b g这4个字母分别代表4种颜色，字母也由空格分隔。
手牌数量不超过10。

输出描述
输出一个数字，即最多能打出的手牌的数量。

用例1
输入
1 4 3 4 5
r y b b r
输出
3
说明
如果打（1, r）-> (5, r)，那么能打两张。

如果打（4，y) -> (4, b) -> (3, b)，那么能打三张。

用例2
输入
1 2 3 4
r y b l
输出
1
说明
没有能够连续出牌的组合，只能在开始时打出一张手牌，故输出1
"""


# 输入
nums = list(input().split())
colors = list(input().split())

# 输出：最多能打出的手牌的数量
class Card:
    def __init__(self, num, color):
        self.num = num
        self.color = color


n = len(nums)
cards = [Card(nums[i], colors[i]) for i in range(n)]
# 手牌数量不超过10。可以暴力回溯
max_cnt = 1


def dfs(path=[], used=[False] * n, level=0):
    global max_cnt
    max_cnt = max(level, max_cnt)

    for i in range(n):
        if used[i]:
            continue

        card = cards[i]
        if not path or (path[-1].num == card.num or path[-1].color == card.color):
            used[i] = True
            path.append(card)
            dfs(path, used, level + 1)
            path.pop()
            used[i] = False


dfs()
print(max_cnt)
