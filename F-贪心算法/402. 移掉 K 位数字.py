"""
给你一个以字符串表示的非负整数 num 和一个整数 k ，移除这个数中的 k 位数字，使得剩下的数字最小。
请你以字符串形式返回这个最小的数字。


示例 1 ：

输入：num = "1432219", k = 3
输出："1219"
解释：移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219 。
示例 2 ：

输入：num = "10200", k = 1
输出："200"
解释：移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
示例 3 ：

输入：num = "10", k = 2
输出："0"
解释：从原数字移除所有的数字，剩余为空就是 0 。


提示：
1 <= k <= num.length <= 10^5
num 仅由若干位数字（0 - 9）组成
除了 0 本身之外，num 不含任何前导零
"""
import collections


# 方法 1：贪心算法 + 单调栈
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n <= k:
            return '0'

        stack = collections.deque()
        for i in range(n):
            # 112 k=1   "1432219", k = 3
            while stack and k > 0 and num[i] < stack[-1]:
                # 维持stack单调递增
                stack.pop()
                k -= 1

            stack.append(num[i])

        # 处理特殊
        # 1.针对单调不减的用例，只取前面剩下的部分，比如： 12345, k=2    112 k=1
        while stack and k > 0:
            stack.pop()
            k -= 1

        # 2.stack去除前置 0, 示例 2："10200", k = 1
        while stack and stack[0] == '0':
            # 这里 stack要用 deque
            stack.popleft()

        # 示例 3：10  k=2
        if not stack:
            return '0'

        # 此时栈内从栈底到栈顶拼接成的字符串就是题目要求的结果
        return ''.join(stack)
