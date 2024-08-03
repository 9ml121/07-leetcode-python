"""
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
 
示例 1：
输入：n = 13
输出：6

示例 2：
输入：n = 0
输出：0
 

提示：
0 <= n <= 10^9
"""
from functools import cache

# todo 数位DP模版
"""
将 n 转换成字符串 s，定义 f(i,cnt1,isLimit) 表示构造到从左往右第 i 位，已经出现了 cnt1个1，
在这种情况下，继续构造最终会得到的 1 的个数（你可以直接从回溯的角度理解这个过程，只不过是多了个记忆化）。

其余参数的含义为：
    - cnt1表示左边填了多少个 1。
    - isLimit 表示当前是否受到了 n 的约束（我们要构造的数字不能超过 n）。
        若为真，则第 i 位填入的数字至多为 n[i]，否则至多为 9，这个数记作 hi。
        如果在受到约束的情况下填了 n[i]，那么后续填入的数字仍会受到 n 的约束。
        例如 n=123，那么 i=0 填的是 1 的话，i=1 的这一位至多填 2。
    
递归边界：当所有数字填完时，返回 cnt1。
递归入口：f(0,0,true)，一开始没有填数字，并且会受到 n 的约束。

复杂度分析
时间复杂度：O(m^2 * D)，其中 m=O(logn)，D=10。
    由于每个状态只会计算一次，动态规划的时间复杂度 = 状态个数 × 单个状态的计算时间。
    本题状态个数等于 O(m^2)，单个状态的计算时间为 O(D)，所以动态规划的时间复杂度为 O(m^2*D)。
空间复杂度：O(m^2)。即状态个数。

作者：灵茶山艾府
链接：https://leetcode.cn/problems/number-of-digit-one/solutions/1750339/by-endlesscheng-h9ua/
"""

class Solution:
    def countDigitOne(self, n: int) -> int:
        # 统计所有小于等于 n 的非负整数中数字 1 出现的个数
        s = str(n)

        @cache
        def dfs(i:int=0, cnt1:int=0, is_limit:bool=True) -> int:
            """dfs表示构造到从左往右第 i 位，已经出现了 cnt1个 1
            @cnt1:表示左边填了多少个 1
            @isLimit: 表示当前是否受到了 n 的约束（我们要构造的数字不能超过 n）
                若为真，则第 i 位填入的数字至多为 n[i]，否则至多为 9
                如果在受到约束的情况下填了 n[i]，那么后续填入的数字仍会受到 n 的约束。
                例如 n=123，那么 i=0 填的是 1 的话，i=1 的这一位至多填 2。
            """
            if i == len(s):
                return cnt1
            
            
            up = int(s[i]) if is_limit else 9
            res = 0
            # 从高位到低位依次枚举要填入的数字 d
            for d in range(up + 1):  
                res += dfs(i + 1, cnt1 + (d == 1), is_limit and d == up)
                
            return res
        
        return dfs()






