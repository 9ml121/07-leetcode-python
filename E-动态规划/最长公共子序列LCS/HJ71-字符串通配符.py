"""
描述
问题描述：在计算机中，通配符一种特殊语法，广泛应用于文件搜索、数据库、正则表达式等领域。现要求各位实现字符串通配符的算法。
要求：
实现如下2个通配符：
*：匹配0个或以上的字符（注：能被*和?匹配的字符仅由英文字母和数字0到9组成，下同）
？：匹配1个字符

注意：匹配时不区分大小写。

输入：
通配符表达式；
一组字符串。

输出：
返回不区分大小写的匹配结果，匹配成功输出true，匹配失败输出false
数据范围：字符串长度：1≤s≤100
进阶：时间复杂度：O(n^2) ，空间复杂度：O(n)

输入描述：
先输入一个带有通配符的字符串，再输入一个需要匹配的字符串
te?t*.*
txt12.xls

输出描述：
返回不区分大小写的匹配结果，匹配成功输出true，匹配失败输出false
false
"""


# 方法1：动态规划
def method01():
    # 不区分大小写
    p = input().lower()
    s = input().lower()

    # 默认为fasle
    dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

    # 边界情况:
    # 1. p和s都为空，true
    dp[0][0] = True
    # 2. p为空，s不为空，false
    # 3. s为空，p不为空，不确定：需要判断p前i个字符是否连续为’*”
    for i in range(1, len(p) + 1):
        if p[i - 1] == '*':
            dp[i][0] = True
        else:
            break

    # 填充正常单元格
    for i in range(1, len(p) + 1):
        for j in range(1, len(s) + 1):
            # p1 = p[i-1]
            # s1 = s[j-1]
            if p[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # 能被*和?匹配的字符仅由英文字母和数字0到9组成
            # elif p[i-1] == '?' and (s[j-1].isalpha() or s[j-1].isdigit()):
            elif p[i - 1] == '?' and s[j - 1].isalnum():
                dp[i][j] = dp[i - 1][j - 1]
            # *：匹配0个或以上的字符：如果匹配0个，就等价于dp[i-1][j]； 如果是匹配1个及以上，就等价于dp[i][j-1]
            elif p[i - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
            # 其他情况都为false

    if dp[len(p)][len(s)]:
        print('true')
    else:
        print('false')


"""
# 方法2: 递归
首先判断第一个通配符：
    1。如果为?，只能匹配数字或字母，匹配一个字符，从下一个位置开始继续递归匹配。
    2。如果为∗，首先要明白多个∗的效果和一个的效果是一样的，为了减少计算复杂度，将多个变为一个。
        ∗号有三种情况，配0个（str+1,str1不用动），匹配1个（str和str1都往前移动1位），匹配多个（str不用动，str+1），分三种情况递归。
    3。如果为其他字符，则要求与被匹配字符串的字符相同或者是它的大小写才能继续往下一个位置递归匹配。
两个字符串同时结束,递归结束，说明匹配成功；两个字符串中有一个先结束，递归结束，匹配失败。

复杂度分析：
时间复杂度：O(2^n)，最坏情况下，递归呈树形。
空间复杂度：O(n)，递归栈大小为n。

解释2：
采用递归的思路。从前向后依次匹配：
一、遇到相同字符，都向后移动一个字符；
二、如果通配符遇到"?"，则不需匹配，自动跳过一个字符；
三、如果通配符遇到"*"，则可以匹配任意多个字符，包括0个，此时可以有三种选择：
    1.匹配0个，通配符向后移动一个字符，字符串不动；
    2.匹配1个，通配符和字符串都向后移动一个字符；
    3.匹配多个，通配符不动，字符串向后移动一个字符。
"""


class Solution:
    def match(self, p: str, s: str) -> bool:
        # 边界定义-各种单边或双边为空的情况
        if s == '' and p == '':
            return True
        elif s != '' and p == '':
            return False
        elif s == '':
            if p.replace('*', '') == '':
                return True
            else:
                return False
        # 字符串与通配符均不为空，递归检查
        else:
            n, m = len(s), len(p)
            # 通配符是问号或者字母
            if (p[m - 1] == '?' and s[n - 1].isalnum()) or p[m - 1].lower() == s[n - 1].lower():
                return self.match(p[0:m - 1], s[0:n - 1])
            # 通配符是星号
            elif p[m - 1] == '*':
                return self.match(p[0:m - 1], s) or self.match(p, s[0:n - 1])
            # 通配符不是问号或者字母，还跟字符串匹配不上
            else:
                return False


while True:
    try:
        p, s = input(), input()
        s1 = Solution()
        print('true' if s1.match(p, s) else 'false')

    except:
        break

"""
方法3: 正则
/**
 * 实现通配符
 * ? 匹配一个字符  [0-9A-Za-z]{1}
 * * 匹配0个或以上的字符  [0-9A-Za-z]{0,}
 * （字符由英文字母和数字0-9组成，不区分大小写。下同）
 */
"""


def method2():
    import re

    while 1:
        try:
            a = input().lower()
            b = input().lower()
            a = a.replace('.', '\.').replace('?', '[a-z0-9]{1}').replace('*', "[a-z0-9]*")
            if b in re.findall(a, b):  # 这题问的是上面一个字符串能不能完全代表下面一个字符串
                print('true')
            else:
                print('false')
        except:
            break
