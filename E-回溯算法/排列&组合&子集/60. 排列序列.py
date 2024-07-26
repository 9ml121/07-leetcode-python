"""
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

示例 1：
输入：n = 3, k = 3
输出："213"

示例 2：
输入：n = 4, k = 9
输出："2314"

示例 3：
输入：n = 3, k = 1
输出："123"


提示：
1 <= n <= 9
1 <= k <= n!
"""


# Hard：回溯 + 剪枝
# todo 难点：如何找到第k个排列？
# 所求排列 一定在叶子结点处得到，进入每一个分支，可以根据已经选定的数的个数，进而计算还未选定的数的个数，
# 然后计算阶乘，就知道这一个分支的 叶子结点 的个数
# 详细思路见力扣第一个解题思路

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 给定 n 和 k，返回第 k 个排列。
        # factorial[i]代表i个数字所有的排列组合数，其实就是一个阶乘数组
        factorial = [1] * (n + 1)
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i
       
        def dfs(k, path:list, i=0, used=[False] * (n + 1)):
            """
            @i 在这一步之前已经选择了几个数字，其值恰好等于这一步需要确定的下标位置
            """
            if i == n:
                return

            # cnt计算多叉树当前分支路径还未确定的数字的全排列的个数, 假设n=4，k=9
            # i=0(也就是当前处于递归树的第一层)，后面还有3个节点没有确定位置，总的节点个数就是cnt = 3! = 6
            cnt = factorial[n - 1 - i]
            
            # j枚举第一层选择[1..n]
            for j in range(1, n + 1):
                if used[j]:
                    continue
                
                # todo 1.如果 k大于这一个分支将要产生的叶子结点数，直接跳过这个分支(剪枝), k需要减去上一轮剪枝的叶子节点数
                # j=1, k > cnt, k=9-6=3, 然后j枚举下个数
                # j=2, k < cnt, 说明第k个数就在这一层后面的叶子节点
                if k > cnt:  
                    k -= cnt
                    continue
                
                # todo 2.如果 k小于等于这一个分支将要产生的叶子结点数，那说明所求的全排列一定在这一个分支将要产生的叶子结点里，需要递归求解。
                # path和used先记录第k个排列已经确定的第一个数j，递归搜索下一层
                path.append(j)
                used[j] = True
                dfs(k, path, j + 1, used)
                
                # 注意 1：不可以回溯（重置变量），算法设计是「一下子来到叶子结点」，没有回头的过程
                # 注意 2：这里要加 return，后面的数没有必要遍历去尝试了
                # todo 3.当到达第k个节点的叶子节点，就立刻返回，第k个排列就是当前path
                return
        

        path = []
        dfs(k, path)
        return ''.join(map(str, path))


