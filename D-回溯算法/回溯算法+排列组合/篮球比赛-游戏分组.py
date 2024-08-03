"""
https://blog.csdn.net/qfc_128220/article/details/127710678
https://fcqian.blog.csdn.net/article/details/134633477

题目描述
篮球(5V5)比赛中，每个球员拥有一个战斗力，每个队伍的所有球员战斗力之和为该队伍的总体战斗力。

现有10个球员准备分为两队进行训练赛，教练希望2个队伍的战斗力差值能够尽可能的小，以达到最佳训练效果。

给出10个球员的战斗力，如果你是教练，你该如何分队，才能达到最佳训练效果?请说出该分队方案下的最小战斗力差值。

输入描述
10个篮球队员的战斗力(整数，范围[1,10000]),战斗力之间用空格分隔，如:10987654321

不需要考虑异常输入的场景。

输出描述
最小的战斗力差值，如:1

用例
输入	10 9 8 7 6 5 4 3 2 1
输出	1
说明	1 2 5 9 10分为一队，3 4 6 7 8分为一队，两队战斗力之差最小，输出差值1。备注：球员分队方案不唯一，但最小战斗力差值固定是1

"""


# todo 有重复元素的组合：10个里面挑5个， 树形dfs
# 获取输入：1 2 3 4 5 6 7 8 9 100
nums = list(map(int, input().split()))
nums.sort()
total = sum(nums)
ans = float('inf')

# 写法1:
def dfs(i, path):
    global ans
    # 出口(path长度不足5个的组合，不进行计算)
    if len(path) == 5:
        groupA = sum(path)
        groupB = total - groupA
        diff = abs(groupA - groupB)
        ans = min(ans, diff)
        return

    # 组合不讲究顺序，所以每次只遍历索引后面的元素
    for j in range(i, 10):
        # 重复的组合，进行剪枝（nums已经升序）
        # 这里需要特别注意的是，必须是同一层的相邻元素。
        if j > i and nums[j] == nums[j-1]:
            continue
        
        path.append(nums[j])
        dfs(j+1, path)
        path.pop()


dfs(0, [])
print(ans)


# 写法2:
def dfs2(i, level, sumV):
    global ans
    if level == 5:
        diff = abs(total - sumV - sumV)
        ans = min(ans, diff)
        return

    # 剪枝：可供选择的元素不足5个，可以跳过
    if level + (10-i) < 5:
        return

    for j in range(i, 10):
        # 剪枝：nums已升序，同一层有相同元素，可以跳过
        if j > i and nums[j] == nums[j-1]:
            continue

        # 注意：sumV是局部变量，在参数里面直接赋值，就不需要写回溯的代码
        dfs2(j+1, level+1, sumV + nums[j])


dfs2(0, 0, 0)
print(ans)
