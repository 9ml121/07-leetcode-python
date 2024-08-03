"""
在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和 达到或超过  100 的玩家，即为胜者。

如果我们将游戏规则改为 “玩家 不能 重复使用整数” 呢？

例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。

给定两个整数 maxChoosableInteger （整数池中可选择的最大数）和 desiredTotal（累计和），若先出手的玩家能稳赢则返回 true ，否则返回 false 。假设两位玩家游戏时都表现 最佳 。

 

示例 1：

输入：maxChoosableInteger = 10, desiredTotal = 11
输出：false
解释：
无论第一个玩家选择哪个整数，他都会失败。
第一个玩家可以选择从 1 到 10 的整数。
如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。
示例 2:

输入：maxChoosableInteger = 10, desiredTotal = 0
输出：true
示例 3:

输入：maxChoosableInteger = 10, desiredTotal = 1
输出：true
 

提示:

1 <= maxChoosableInteger <= 20
0 <= desiredTotal <= 300
"""
from functools import cache

# todo 回溯算法 + 状态压缩  困难！！

# https://mp.weixin.qq.com/s/ecxTTrRvUJbdWwSFbKgDiw
# 「可重复选」的暴力核心代码如下
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # acc 表示当前累计的数字和
        @cache
        def dfs(acc:int=0):
            if acc >= desiredTotal:
                return False
            
            for n in range(1, maxChoosableInteger + 1):
                # 对方有一种情况赢不了，我就选这个数字就能赢了，返回 true，代表可以赢。
                if not dfs(acc + n):
                    return True
            return False

        # 初始化集合，用于保存当前已经选择过的数。
        return dfs()

# 「如果数字不允许重复选」:一个直观的思路是使用 set 记录已经被取的数字。当选数字的时候，如果是在 set 中则不取即可
# 使用 set 的值传递，每个递归树的节点都会存一个完整的 set，空间大概是 「节点的数目」 *「set 中数字个数」,空间消耗巨大
# 使用本状态回溯的方式。由于每次都要从 set 中移除指定数字，时间复杂度是「节点的数目」* maxChoosableInteger，这样做时间复杂度又太高了。
# 为什么不使用记忆化递归？这样可以有效减少逻辑树的节点数，从指数级下降到多项式级。
# todo 这里的原因在于 set 是不可直接序列化的，因此不可直接存储到诸如哈希表这样的数据结构。
# 如果你自己写序列化，比如最粗糙的将 set 转换为字符串或者元祖存。看起来可行，set 是 ordered 的，因此如果想正确序列化还需要排序。
# 当然你可用一个 orderedhashset，不过效率依然不好
# 问题的关键基本上锁定为找到一个「可以序列化且容量大大减少的数据结构」来存是不是就可行了？
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger:
            return True
        
        if sum(range(maxChoosableInteger + 1)) < desiredTotal:
            return False
        # picked 用于保存当前已经选择过的数。
        # acc 表示当前累计的数字和

        def backtrack(picked:set, acc:int)->bool:
            if acc >= desiredTotal:
                return False
            if len(picked) == maxChoosableInteger:
                # 说明全部都被选了，没得选了，返回 False， 代表输了。
                return False
            
            for n in range(1, maxChoosableInteger + 1):
                if n not in picked:
                    picked.add(n)
                    # 对方有一种情况赢不了，我就选这个数字就能赢了，返回 true，代表可以赢。
                    if not backtrack(picked, acc + n):
                        picked.remove(n)
                        return True
                    picked.remove(n)
            return False

        # 初始化集合，用于保存当前已经选择过的数。
        return backtrack(set(), 0)


# 注意到 「maxChoosableInteger  不会大于 20」
# 由于 20 是一个不大于 32 的数字， 因此这道题很有可能和状态压缩有关，比如用 4 个字节存储状态
# 我们可以将状态进行压缩，使用位来模拟。实际上使用状态压缩和上面「思路一模一样，只是 API 不一样」罢了。
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger:
            return True
        if sum(range(maxChoosableInteger + 1)) < desiredTotal:
            return False

        @cache
        def dp(picked:int, acc:int):
            if acc >= desiredTotal:
                return False
            # todo 判断集合大小是否等于 maxChoosableInteger，
            # 「第 maxChoosableInteger 位以及低于 maxChoosableInteger 的位是否全部是 1」。
            # 我们只需要将 1 左移 maxChoosableInteger + 1 位再减去 1 即可
            if picked == (1 << (maxChoosableInteger + 1)) - 1:
                return False
            
            for n in range(1, maxChoosableInteger + 1):
                # todo 模拟 n in picked
                # 判断 picked 的第 n 位是 0 还是 1:如果是 0 表示不在 picked 中，如果是 1 表示在 picked 中
                if picked & 1 << n == 0:
                    # todo 如果实现 add 操作？
                    if not dp(picked | 1 << n, acc + n):
                        return True
            return False

        return dp(0, 0)
