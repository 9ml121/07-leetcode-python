"""
给你一组多米诺骨牌 dominoes 。

形式上，dominoes[i] = [a, b] 与 dominoes[j] = [c, d] 等价 当且仅当 (a == c 且 b == d) 或者 (a == d 且 b == c) 。即一张骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌。

在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。

 

示例 1：

输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
输出：1
示例 2：

输入：dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
输出：3
 

提示：

1 <= dominoes.length <= 4 * 104
dominoes[i].length == 2
1 <= dominoes[i][j] <= 9
"""

import collections
from typing import List

# https://leetcode-solution-leetcode-pp.gitbook.io/leetcode-solution/easy/1128.number-of-equivalent-domino-pairs
# 方法 1：“排序” + 计数
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # 1.将[a,b]转换为元祖，或者字符串，作为哈希字典的 key, 统计每个 key出现的次数cnt
        # 2.计算等价数组对，也就是计算从 1 到（cnt-1） 公差为 1 的等差数列和
        cnts = collections.defaultdict(int)
        ans = 0
        for d in dominoes:
            key = tuple(sorted(d))
            # 我们的计数信息其实就是公差为 1 的等差数列，正好对应前面写的等差数列: cnt*(cnt-1)//2
            ans += cnts[key]
            cnts[key] += 1
            
        return ans
       

    
# todo 方法 2：状态压缩 + 一次遍历

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # 1 <= dominoes[i][j] <= 9, 可以压缩为 4bit
        # 二元数组，可以压缩为8bit,总共有 256 种状态
        counts = [0] * 256
        ans = 0
        for a, b in dominoes:
            if a >= b:
                v = a << 4 | b
            else:
                v = b << 4 | a
            
            ans += counts[v]
            counts[v] += 1
        return ans
        

# 方法 3：状态压缩优化
# 由于 1 <= dominoes[i][j] <= 9，我们也可直接用 9 进制来存，刚好 9 * 9 = 81 种状态。 这样开辟一个大小为 81 的数组即可
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = [0] * 9 * 9
        ans = 0
        for a, b in dominoes:
            v = min((a - 1) * 9 + (b - 1), (b - 1) * 9 + (a - 1))
            ans += counts[v]
            counts[v] += 1
        return ans
