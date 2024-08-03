"""
题目描述
给定一个数组nums，将元素分为若干个组，使得每组和相等，求出满足条件的所有分组中，组内元素和的最小值。

输入描述
第一行输入 m
接着输入m个数，表示此数组nums
数据范围：1<=m<=50, 1<=nums[i]<=50

输出描述
最小拆分数组和

用例
输入	7
        4 3 2 3 5 2 1
输出	5

说明
可以等分的情况有：
4 个子集（5），（1,4），（2,3），（2,3）
2 个子集（5, 1, 4），（2,3, 2,3）
但最小的为5。
"""

# todo 二分查找 + 回溯算法（桶装球问题）
'''
题目解析
本题算是LeetCode - 698 划分为k个相等的子集_的变种题，本题同样是要将数组划分为k个和相等的子集。
本题要我们求解：最小拆分数组和，其实就是求解：最小子集和，其实就是求解，最大k值。因为k值越大，则对应的子集的和越小。

这里k的求解很简单，首先，我们可以猜想下k的上限是多少？
比如数组所有元素都相等，则k == m，即每个元素都能作为一个子集，因此我们可以让k从m开始尝试，如果不行，则k--，直到k=1。

而验证nums是否可以划分为k层，其实就是判断nums是否可以划分为k个和相等的子集，这个判断逻辑可以复用LeetCode - 698 划分为k个相等的子集 中的逻辑。
'''


# 算法入口
def get_result(nums, m):
    # nums可以拆分的最大和最小等和子集数k
    maxK = m
    minK = 1
    # 当k最大时，获取的等和值时最小的。可以将k从大到小遍历
    nums.sort(reverse=True)  # 按照从高到低排序，降低递归复杂度
    sumV = sum(nums)
    for k in range(maxK, minK - 1, -1):
        avg = sumV // k
        bucket = [0] * m
        # 先排除特殊情况
        if sumV % k != 0 or nums[0] > avg:
            continue
        elif backtrack(nums, 0, bucket, avg):
            return avg


# 判断nums数组是否可以等分为k个子集的逻辑
def backtrack(nums, index, bucket, avg):
    # index为nums数组索引
    # bucket为每个等分子集num数量之和的列表
    if index == len(nums):
        return True
    # 根据桶选择球的思路递归: 从大到小依次取出nums每个数
    selected = nums[index]
    for i in range(len(bucket)):
        # 剪枝
        if i > 0 and bucket[i] == bucket[i - 1]:
            continue
        # 递归
        elif bucket[i] + selected <= avg:
            bucket[i] += selected
            if backtrack(nums, index + 1, bucket, avg):
                return True
            # 回溯
            bucket[i] -= selected
    # 如果找不到等和
    return False


# 获取输入
m = 7
nums = [4, 3, 2, 3, 5, 2, 1]
res = get_result(nums, m)
print(res)
