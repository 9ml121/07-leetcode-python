"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/134725138?spm=1001.2014.3001.5502

题目描述
某部门计划通过结队编程来进行项目开发，

已知该部门有 N 名员工，每个员工有独一无二的职级，每三个员工形成一个小组进行结队编程，结队分组规则如下：

从部门中选出序号分别为 i、j、k 的3名员工，他们的职级分贝为 level[i]，level[j]，level[k]，

结队小组满足 level[i] < level[j] < level[k] 或者 level[i] > level[j] > level[k]，

其中 0 ≤ i < j < k < n。

请你按上述条件计算可能组合的小组数量。同一员工可以参加多个小组。

输入描述
第一行输入：员工总数 n

第二行输入：按序号依次排列的员工的职级 level，中间用空格隔开

限制：

1 ≤ n ≤ 6000
1 ≤ level[i] ≤ 10^5
输出描述
可能结队的小组数量

用例1
输入
4
1 2 3 4
输出
4
说明
可能结队成的组合(1,2,3)、(1,2,4)、(1,3,4)、(2,3,4)

用例2
输入
3
5 4 7
输出
0
说明
根据结队条件，我们无法为该部门组建小组
"""

# 获取输入
n = int(input())
level = list(map(int, input().split()))

# 方法1: 按照n选3的组合算法(dfs回溯算法更通用，但是可能超时！)


def solution1(n, level):
    if n < 3:
        return 0

    ans = 0

    def dfs(i, cnt, flag):
        nonlocal ans
        if cnt == 3:
            ans += 1
            return

        for j in range(i+1, n):
            if flag and level[j] > level[i]:
                dfs(j, cnt+1, flag)

            if not flag and level[j] < level[i]:
                dfs(j, cnt+1, flag)

    for i in range(n-2):
        # 小剪枝
        if i > 0 and level[i] == level[i-1]:
            continue
        dfs(i, 1, True)
        dfs(i, 1, False)

    return ans

# 方法2：题目要求按照level数组索引升序，递增或者递减的3个数组合，其实就是求：
# 递增=》左边小于level[i]的个数 * 右边大于level[i]的个数
# 递减=》左边大于level[i]的个数 * 右边小于level[i]的个数
# 一种方法是双层循环O(N^2)，1 ≤ n ≤ 6000，百万级别以上，有超时风险
# 另外一种方法是构建二叉搜索树(O(N(logN))), 时间复杂度更低


def solution2(n, level):
    if n < 3:
        return 0

    ans = 0
    for i in range(n):
        # 统计左边
        left_smaller_cnt = 0
        left_bigger_cnt = 0
        for j in range(i):
            if level[j] > level[i]:
                left_bigger_cnt += 1
            elif level[j] < level[i]:
                left_smaller_cnt += 1

        # 统计右边
        right_smaller_cnt = 0
        right_bigger_cnt = 0
        for k in range(i+1, n):
            if level[k] > level[i]:
                right_bigger_cnt += 1
            elif level[k] < level[i]:
                right_smaller_cnt += 1

        ans += left_smaller_cnt * right_bigger_cnt + left_bigger_cnt * right_smaller_cnt

    return ans


def solution3(n,level):
    # 构建二叉搜索树，左子树都比父节点小，右子树都比父节点大
    class BST:
        def __init__(self, idx, val) -> None:
            self.val = val
            self.idx = idx
            self.left = None
            self.right = None
            self.cnt = 0  # 存在左右节点