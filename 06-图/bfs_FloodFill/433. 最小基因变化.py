"""
基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。

假设我们需要调查从基因序列 start 变为 end 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。

例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。
另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。（变化后的基因必须位于基因库 bank 中）

给你两个基因序列 start 和 end ，以及一个基因库 bank ，请你找出并返回能够使 start 变化为 end 所需的最少变化次数。
如果无法完成此基因变化，返回 -1 。

注意：起始基因序列 start 默认是有效的，但是它并不一定会出现在基因库中。



示例 1：
输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
输出：1

示例 2：
输入：start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
输出：2

示例 3：
输入：start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
输出：3


提示：
start.length == 8
end.length == 8
0 <= bank.length <= 10
bank[i].length == 8
start、end 和 bank[i] 仅由字符 ['A', 'C', 'G', 'T'] 组成
"""
import collections
from typing import List


# bfs解法1：枚举每个状态基因可以转换的 8*4 个基因是否都在 bank中
# 同类型题
# 127. 单词接龙.py
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0

        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        bank_set.remove(endGene)
        dq = collections.deque([(endGene, 0)])  # (目标基因, 变化次数)

        while dq:
            target, changes = dq.popleft()
            for i in range(8):  # 枚举每个状态基因可以转换的 8*4 个基因是否都在 bank中
                for c in 'ACGT':
                    if c == target[i]:
                        continue
                    new_gene = target[:i] + c + target[i + 1:]

                    if new_gene == startGene:  # 找到开始基因
                        return changes + 1

                    if new_gene in bank_set:
                        dq.append((new_gene, changes + 1))
                        bank_set.remove(new_gene)

        return -1


# 方法2：bfs思路 2，判断两个基因是否只有 1 个位置不同
class Solution2:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0

        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        # 判断两个基因是否只有 1 个位置不同
        def one_diff(gene1, gene2):
            return sum(gene1[i] != gene2[i] for i in range(8)) == 1

        dq = collections.deque([(startGene, 0)])  # (基因状态, 变化次数)
        while dq:
            gene, changes = dq.popleft()
            remove_genes = set()
            for next_gene in bank_set:
                if one_diff(next_gene, gene):
                    if next_gene == endGene:
                        return changes + 1
                    dq.append((next_gene, changes + 1))
                    remove_genes.add(next_gene)

            # 要从Python集合中移除一个列表中的所有元素，可以使用集合的 difference_update() 方法或 -= 运算符。
            # 这两种方法都可以用于对集合进行差集操作，并更新原始集合。
            bank_set.difference_update(remove_genes)
        return -1


# 方法 3：双向广度优先搜索（BFS）的方法来找到最短路径。
# 双向 BFS 可以从起始基因和目标基因同时开始搜索，相向而行，直到两个搜索路径相遇。
class Solution3:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        start_set = {startGene}
        end_set = {endGene}
        step = 0

        while start_set and end_set:
            if len(start_set) > len(end_set):
                start_set, end_set = end_set, start_set

            next_set = set()

            for gene in start_set:
                for i in range(8):
                    for ch in ['A', 'C', 'G', 'T']:
                        new_gene = gene[:i] + ch + gene[i + 1:]

                        if new_gene in end_set:
                            return step + 1

                        if new_gene in bank_set and new_gene not in start_set:
                            next_set.add(new_gene)
                            bank_set.remove(new_gene)

            start_set = next_set
            step += 1

        return -1
