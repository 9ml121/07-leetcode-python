"""
有两个水壶，容量分别为 jug1Capacity 和 jug2Capacity 升。
水的供应是无限的。
确定是否有可能使用这两个壶准确得到 targetCapacity 升。

如果可以得到 targetCapacity 升水，最后请用以上水壶中的一或两个来盛放取得的 targetCapacity 升水。

你可以：
1.装满任意一个水壶
2.清空任意一个水壶
3.从一个水壶向另外一个水壶倒水，直到装满或者倒空


示例 1:
输入: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
输出: true
解释：来自著名的 "Die Hard"

示例 2:
输入: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
输出: false

示例 3:
输入: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
输出: true


提示:

1 <= jug1Capacity, jug2Capacity, targetCapacity <= 10^6
"""
import collections
import math

"""
题目描述：
有两个容量分别为x升和y升的水壶，可以进行以下操作：
1.倒空任意一个水壶；
2.把一个水壶的水倒入另外一个水壶，直到装满或倒空。
判断能否通过这些操作，使得其中一个水壶恰好装有z升的水。

注意：
1.x、y和z都是非负整数。
2.可以假设x和y的最大公约数是d，且z是d的倍数。

解题思路：
1.这是一个经典的数学问题，可以使用"裴蜀定理"（Bézout's identity）来解决。
2.根据裴蜀定理，对于任意两个非负整数x和y，存在整数a和b，使得ax + by = d，其中d为x和y的最大公约数。
  如果z是d的倍数，那么存在整数a'和b'，使得a'x + b'y = z。
3.因此，我们可以通过计算x和y的最大公约数d，并判断z是否是d的倍数来判断能否得到z升水。
  具体的步骤如下：
    1)如果z大于x和y的和，显然无法通过操作得到z升水，返回False。
    2)计算x和y的最大公约数d，使用辗转相除法或欧几里得算法。
    3)如果z是d的倍数，返回True；否则，返回False。
"""


# 数学方法
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # 求正整数x和y的最大公约数
        # 这里可以直接调用库包：math.gcd(6,9)
        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        # math.gcd(6, 9)  # Greatest Common Divisor.结果为3
        # 特判
        if z > x + y:
            return False
        if x == 0 or y == 0:
            return z == x or z == y

        # 贝祖定理: ax+by=z 有解当且仅当 z 是 x,y 的最大公约数的倍数
        return z % gcd(x, y) == 0


"""
如果要使用广度优先搜索（BFS）来解决 "365. 水壶问题"，可以按照以下思路进行编程：
1.定义一个队列（可以使用 Python 中的 deque）来存储搜索过程中的状态。
2.定义一个集合（可以使用 Python 中的 set）来存储已经搜索过的状态，以避免重复搜索。
3.将初始状态（0, 0）加入队列和集合中。
4.通过循环遍历队列中的状态，直到队列为空：
    1)从队列中取出一个状态（x, y）。
    2)根据题目给出的操作规则，生成可能的下一个状态（倒满、倒空、相互倒）。
    3)如果下一个状态为目标状态（其中一个水壶的水量为 z），则返回 True。
    4)如果下一个状态不在集合中，将其加入队列和集合中。
5.如果循环结束后仍然没有找到目标状态，则返回 False。
"""


# BFS方法
class Solution2:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        # 特判
        if targetCapacity > jug1Capacity + jug2Capacity:
            return False

        # (0,0)代表两个水壶的初始状态，这里也可以用具名元祖区分第一个壶和第二个壶
        dq = collections.deque([(0, 0)])
        visited = {(0, 0)}

        while dq:
            curr_x, curr_y = dq.popleft()

            if curr_x == targetCapacity or curr_y == targetCapacity or curr_x + curr_y == targetCapacity:
                return True

            # 从当前状态获得所有可能的下一步的状态
            next_states = self.getNextStates(curr_x, curr_y, jug1Capacity, jug2Capacity)

            print(next_states)

            for state in next_states:
                if state not in visited:
                    dq.append(state)
                    visited.add(state)  # 添加到队列以后，必须马上设置为已经访问，否则会出现死循环

            print(dq)
            print("---------------")
        return False

    def getNextStates(self, curr_x, curr_y, x, y):
        next_states = []
        # 按理说应该先判断状态是否存在，再生成「状态」对象，这里为了阅读方便，一次生成 8 个对象
        # 1.倒满x
        next_states1 = (x, curr_y)
        # 2.倒满y
        next_states2 = (curr_x, y)

        # 3.倒空x
        next_states3 = (0, curr_y)
        # 4.倒空y
        next_states4 = (curr_x, 0)

        # 5.x倒入y, 倒满y, x还有剩: x=3,y=5 curr_x=3, curr_y=3
        next_states5 = (curr_x - (y - curr_y), y)
        # 6.x倒入y, 没倒满y, x空: x=3,y=5 curr_x=3, curr_y=0
        next_states6 = (0, curr_y + curr_x)

        # 7.y倒入x, 倒满x, y还有剩
        next_states7 = (x, curr_y - (x - curr_x))
        # 8.y倒入x, 没倒满x, y空
        next_states8 = (curr_x + curr_y, 0)

        # 没有满的时候，才需要加水
        if curr_x < x:
            next_states.append(next_states1)
        if curr_x < y:
            next_states.append(next_states2)

        # 原来有水，才能倒空
        if curr_x > 0:
            next_states.append(next_states3)
        if curr_y > 0:
            next_states.append(next_states4)

        # 有剩余才倒
        if curr_x > y - curr_y:
            next_states.append(next_states5)
        if curr_y > x - curr_x:
            next_states.append(next_states7)

        # 倒过去倒不满才倒
        if curr_x + curr_y < y:
            next_states.append(next_states6)
        if curr_x + curr_y < x:
            next_states.append(next_states8)

        return next_states


# bfs简写
class Solution3:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # 特判
        if z > x + y:
            return False
        # (0,0)代表两个水壶的初始状态，这里也可以用具名元祖区分第一个壶和第二个壶
        dq = collections.deque([(0, 0)])
        visited = {(0, 0)}

        while dq:
            curr_x, curr_y = dq.popleft()
            if curr_x == z or curr_y == z or curr_x + curr_y == z:
                return True

            # 从当前状态获得所有可能的下一步的状态
            next_states = [
                (x, curr_y),  # 倒满 x
                (curr_x, y),  # 倒满 y
                (0, curr_y),  # 倒空 x
                (curr_x, 0),  # 倒空 y
                # 把 X 壶的水灌进 Y 壶，直至 Y灌满或 X倒空。
                (curr_x - min(curr_x, y - curr_y), curr_y + min(curr_x, y - curr_y)),
                # 把 Y 壶的水灌进 X 壶，直至X 灌满或 Y倒空。
                (curr_x + min(curr_y, x - curr_x), curr_y - min(curr_y, x - curr_x))  # y 倒入 x
            ]

            for state in next_states:
                if state not in visited:
                    dq.append(state)
                    visited.add(state)  # 添加到队列以后，必须马上设置为已经访问，否则会出现死循环

        return False


if __name__ == '__main__':
    jug1Capacity = 3
    jug2Capacity = 5
    targetCapacity = 4
    print(Solution().canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity))
    print(Solution2().canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity))
