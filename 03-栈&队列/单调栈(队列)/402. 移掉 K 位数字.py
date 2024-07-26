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


# todo 单调栈: 及时去除无效数据，保持栈单调性
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        给你一个以字符串表示的非负整数 num 和一个整数 k ，移除这个数中的 k 位数字，使得剩下的数字最小。
        请你以字符串形式返回这个最小的数字
        """
        if k >= len(num):
            return '0'

        # todo st: 非严格单调递增, 保存num移除k个字符之后的元素
        st = []
        for i, c in enumerate(num):
            # num=112 k=1 => 112, num=1432219, k = 3 =>1219
            while st and k > 0 and c < st[-1]:
                st.pop()
                k -= 1

            st.append(c)

        # 处理特殊
        # 1.num单调递增，比如‘112’， k=1, 只取前面剩下的部分
        while st and k > 0:
            st.pop()
            k -= 1

        # 2.num去除k个字符之后含有前导0，比如："10200", k = 1 ==> 0200
        while st and st[0] == '0':
            st.pop()

        # 3.st去除前导0之后变为空
        # 此时栈内从栈底到栈顶拼接成的字符串就是题目要求的结果
        return ''.join(st) if st else '0'
