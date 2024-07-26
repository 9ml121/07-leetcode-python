"""
实现一个基本的计算器来计算简单的表达式字符串。

表达式字符串只包含非负整数，算符 +、-、*、/ ，左括号 ( 和右括号 ) 。整数除法需要 向下截断 。

你可以假定给定的表达式总是有效的。所有的中间结果的范围均满足 [-231, 231 - 1] 。

注意：你不能使用任何将字符串作为表达式求值的内置函数，比如 eval() 。



示例 1：
输入：s = "1+1"
输出：2

示例 2：
输入：s = "6-4/2"
输出：4

示例 3：
输入：s = "2*(5+5*2)/3+(6/2+8)"
输出：21


提示：
1 <= s <= 10^4
s 由整数、'+'、'-'、'*'、'/'、'(' 和 ')' 组成
s 是一个 有效的 表达式
"""
import collections

"""
calculate(3 * (4 - 5/2) - 6)
= 3 * calculate(4 - 5/2) - 6
= 3 * 2 - 6
= 0

无论多少层括号嵌套，通过 calculate 函数递归调用自己，都可以将括号中的算式化简成一个数字。
换句话说，括号包含的算式，我们直接视为一个数字就行了。
递归的开始条件和结束条件是什么？遇到 ( 开始递归，遇到 ) 结束递归
"""


# 参考：https://labuladong.github.io/algo/di-san-zha-24031/jing-dian--a94a0/
# todo 递归处理括号和计算的优先级:
class Solution:
    def calculate(self, s: str) -> int:
        def helper(dq: collections.deque) -> int:
            stack = []
            num = 0
            op = '+'

            while dq:
                c = dq.popleft()
                # 字符串转整数
                if c.isdigit():
                    num = num * 10 + int(c)

                # todo 遇到左括号开始递归计算 num
                if c == '(':
                    num = helper(dq)

                if (not c.isdigit() and c != ' ') or len(dq) == 0:
                    if op == '+':
                        stack.append(num)
                    elif op == '-':
                        stack.append(-num)
                    elif op == '*':
                        stack.append(stack.pop() * num)
                    elif op == '/':
                        stack.append(int(stack.pop() / num))

                    op = c
                    num = 0

                # 遇到右括号返回递归结果
                if c == ')':
                    break

            return sum(stack)

        # 将s转换为双向队列，与之前判断字符串s索引方法是一样的
        dq = collections.deque(s)
        return helper(dq)


if __name__ == '__main__':
    s = "2*(5+5*2)/3+(6/2+8)"  # 21
    print(Solution().calculate(s))
