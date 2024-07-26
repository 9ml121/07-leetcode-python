"""
题目描述
有一堆长方体积木，它们的高度和宽度都相同，但长度不一。

小橙想把这堆积木叠成一面墙，墙的每层可以放一个积木，也可以将两个积木拼接起来，要求每层的长度相同。

若必须用完这些积木，叠成的墙最多为多少层？

如下是叠成的一面墙的图示，积木仅按宽和高所在的面进行拼接。



输入描述
输入为一行，为各个积木的长度，数字为正整数，并由空格分隔。积木的数量和长度都不超过50。

输出描述
输出一个数字，为墙的最大层数，如果无法按要求叠成每层长度一致的墙，则输出-1。

用例
输入	3 6 3 3 3
输出	3
说明	以 6 为底的墙，第一层为 6 ，第二层为 3 + 3，第三层 3 + 3。
输入	9 9 9 5 3 2 2 2 2 2
输出	5
说明	
5+2+2=9

3+2+2+2=9

9,9,9

共五层
"""

# C-回溯算法/划分k个等和子集问题/698.划分为k个相等的子集.py 变种题
# 本题隐含条件：
# 1.按照测试用例说明，一层可以用多个积木。
# 2.如果无法按要求叠成每层长度一致的墙，则输出-1 ==》 说明最小层数是2

# 输入
# 各个积木的长度,积木的数量和长度都不超过50。
nums = [3,6,3,3,3]

# 输出一个数字，为墙的最大层数
def main():
    # 1.按照最小层数为2，最大层数为len(nums),也就是nums所有数字一样
    n = len(nums)
    
    # 2.将积木从高到低排列,按照层数从高到低开始尝试，是否可以用完所有积木，一旦满足，最高层数就是当前层数
    nums.sort(reverse=True)
    total = sum(nums)
    for h in range(n, 1, -1):
        # 3. 如果不能均分为h层，不满足
        if total % h != 0:
            continue
        # 4. 如果最大长度大于每层长度，不满足
        level = total // h  # 每层长度
        if nums[0] > level:
            continue
        # 5. 先计算单个积木长度为level的个数
        i = 0
        cnt = h
        while i < len(nums) and nums[i] == level:
            cnt -= 1
            i += 1
        # 6. 最后计算nums[i:]是否可以划分为h个等和子集
        if check(nums, i, [0]*cnt, level):
            return h
    return -1

def check(nums, idx, buckets, level):
    # 将nums划分为len(buckets)个等和子集，每层容量为level
    if idx == len(nums):
        return True
    
    # idx代表当前选择的球的索引下标
    selected = nums[idx]
    
    # 遍历桶
    for i in range(len(buckets)):
        # 剪枝：前提是球要倒序排列
        if i>0 and buckets[i] == buckets[i-1]:
            continue
        
        # 如果当前桶装不下当前选择的球，就换下一个桶装
        # 如果可以装下，就用回溯算法
        if buckets[i] + selected <= level: 
            # 先尝试装下当前球，看能不能装完所有       
            buckets[i] += selected
            # todo 找到一个可以装下所有球的方案,就可以返回True
            if check(nums, idx+1, buckets, level):
                print(buckets)
                return True
            # 如果不能装完所有球，就反悔
            buckets[i] -= selected
    return False

print(main())