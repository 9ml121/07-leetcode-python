"""
给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。
注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。

示例 1：
输入：n = 12
输出：21

示例 2：
输入：n = 21
输出：-1

提示：
1 <= n <= 2^31 - 1
"""


# todo 贪心问题,不需要用到单调栈, 
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """给你一个正整数 n ，请你找出符合条件的最小整数:
        1.由重新排列 n 中存在的每位数字组成;
        2.其值大于 n, 且输入重新排列中最小的那个数
        整体思路： n = 46873 ==> 47 863 => 47 368
        """
        # 正整数转换为字符串列表
        s = list(str(n))
        sz = len(s)
        
        # 1.先倒序遍历n, 找到第一个当前数 严格小于 后面一位数的位置i(i后面的数单调递减)
        for i in range(sz - 2, -1, -1): 
            if s[i] < s[i + 1]:
                j = i # j最终指向i后面大于s[i]的最小数
                while j + 1 < sz and s[j + 1] > s[i]:
                    # 2. 在正序遍历[i+1..sz), 找到i后面大于s[i]的最小数字位置j, 交换2个位置数字
                    j += 1
                s[i], s[j] = s[j], s[i]

                # 3.对 i 后面的元素升序排列，得到符合条件的最小整数ans
                s = s[:i + 1] + sorted(s[i + 1:])
                ans = int(''.join(s))
                
                # 4.判断结果是否溢出，并返回结果
                return ans if ans < 2 ** 31 else -1
            
        # 5.如果所有元素下一个都小于等于当前元素，返回-1， 比如 44321
        return -1


# 写法2
class Solution2:
    def nextGreaterElement(self, n: int) -> int:
        s = []
        # 将正整数转换为数值列表的另外一种写法
        while n > 0:  # n = 46873
            s.append(n % 10)
            n //= 10
        
        s = s[::-1]
        sz = len(s)
        
        # 1.从右往左遍历列表，找到第一个前面的数小于后面的数的位置i(i后面的数单调递减)
        for i in range(sz - 2, -1, -1):
            if s[i] < s[i + 1]:
                # 2.从i+1到末尾，找到最后一个严格大于s[i]的数的位置j，交换两者位置
                # 4 6 873 ==> 4 7 863
                j = i + 1
                while j < sz and s[j] > s[i]:
                    j += 1
                s[i], s[j - 1] = s[j - 1], s[i]
                
                # 3.将i+1到末尾的数翻转
                # 47 863 ==> 47 368
                left, right = i + 1, sz - 1
                while left < right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
                    
                # 4.将数值列表重新转换为整数
                ans = int(''.join(map(str, s)))

                # 5.判断结果是否溢出
                return ans if ans < 2 ** 31 else -1
            
        # 6.如果所有元素下一个都小于等于当前元素，返回-1， 比如 44321
        return -1


if __name__ == '__main__':
    # n = 486
    # n = 4863
    n = 46873

    print(Solution2().nextGreaterElement(n))
