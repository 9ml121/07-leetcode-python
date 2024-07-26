"""
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。
1。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
2。锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
3。列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。

示例 1:
输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定。

示例 2:
输入: deadends = ["8888"], target = "0009"
输出：1
解释：把最后一位反向旋转一次即可 "0000" -> "0009"。

示例 3:
输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
输出：-1
解释：无法旋转到目标数字且不被锁定。


提示：

1 <= deadends.n <= 500
deadends[i].n == 4
target.n == 4
target 不在 deadends 之中
target 和 deadends[i] 仅由若干位数字组成
"""
import collections
from typing import List

"""
解题思路：
这个问题可以使用广度优先搜索（BFS）来解决。
我们可以将每个可能的密码看作图中的一个节点，两个密码之间存在边，当且仅当它们在一位上的数字相差1。
我们可以从初始密码开始，通过旋转拨轮来生成所有可能的后继密码，然后将其添加到搜索队列中。

具体的解题步骤如下：
1.创建一个队列，将初始密码 '0000' 加入队列，并创建一个集合用于记录已经访问过的密码。
2.初始化步数为0。
3.进入循环，直到队列为空：
    - 从队列中取出一个密码，记为 current。
    - 如果 current 等于 target，则返回步数。
    - 将 current 的未访问过的后继密码加入队列，并将其标记为已访问。
4.如果循环结束时仍未找到目标密码，则返回 -1。
"""


# 双向BFS, 类似leetcode 127. 单词接龙
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deads = set(deadends)
        if '0000' in deads:
            return -1
        # 从起点开始启动广度优先搜索
        dq = collections.deque([("0000", 0)])
        # 记录已经穷举过的密码，防止走回头路
        visited = set("0000")

        while dq:
            # 将当前队列中的所有节点向周围扩散
            cur, step = dq.popleft()

            # 判断是否找到目标
            if cur == target:
                return step

            # 将一个节点的未遍历相邻节点加入队列
            for i in range(4):
                digit = int(cur[i])
                for j in [-1, 1]:
                    new_digit = (digit + j) % 10  # (-1) % 10 = 9
                    new_password = cur[0:i] + str(new_digit) + cur[i + 1:]
                    if new_password not in visited and new_password not in deads:
                        dq.append((new_password, step + 1))
                        visited.add(new_password)

        # 如果穷举完都没找到目标密码，那就是找不到了
        return -1


if __name__ == '__main__':
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"  # 6
    print(Solution().openLock(deadends, target))
