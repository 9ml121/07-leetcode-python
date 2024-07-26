"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/129300840

题目描述
有一堆长方体积木，它们的宽度和高度都相同，但长度不一。

小橙想把这堆积木叠成一面墙，墙的每层可以放一个积木，也可以将两个积木拼接起来，要求每层的长度相同。

若必须用完这些积木，叠成的墙最多为多少层？

image

输入描述
输入为一行，为各个积木的长度，数字为正整数，并由空格分隔。积木的数量和长度都不超过5000。

输出描述
输出一个数字，为墙的最大层数，如果无法按要求叠成每层长度一致的墙，则输出-1。

用例1
输入
3 6 6 3
输出
3
说明
可以每层都是长度3和6的积木拼接起来，这样每层的长度为9，层数为2；也可以其中两层直接用长度6的积木，两个长度3的积木拼接为一层，这样层数为3，故输出3。

用例2
输入
1 4 2 3 6
输出
-1
说明
无法用这些积木叠成每层长度一致的墙，故输出-1。
"""

# todo 考察点： 同向双指针 + 贪心

# 输入
# 输入为一行，为各个积木的长度
nums = list(map(int, input().split()))

# 输出：一个数字，为墙的最大层数，如果无法按要求叠成每层长度一致的墙，则输出-1。
# 墙的每层可以放一个积木，也可以将两个积木拼接起来，要求每层的长度相同。
# 本题限制了一层最多只能有两个积木，最少有一个积木。
# 如果没有这个上面限制条件，那么本题需要换另一种解法：C-回溯算法/划分k个等和子集问题/叠积木Ⅱ.py

# todo 双指针判断nums是否可以叠成每层高度一致，高度为h的墙。
def check(nums, total, level):
    if total % level != 0:
        return False

    l = 0
    r = len(nums) - 1
    while r>=0  and nums[r] == level:
        # 只用最大那一个
        r -= 1
        
    while l < r:
        # 用最大的和最小的2个组合(不然最小那个就用不上)
        if nums[r] + nums[l] == level:
            l += 1
            r -= 1
        else:
            return False
    return True


def main():
    n = len(nums)
    # 如果只有1个积木，最多就是放1层
    if n == 1:
        return 1
    
    # 如果只有2个积木,长度一样可以放2层，否则只能放一层
    if n == 2:
        return 2 if nums[0] == nums[1] else 1
    
    # 3个积木以上
    nums.sort()
    # 贪心思维：因为每层只能放1-2个积木，因此每层长度要么为nums[-1], 要么为nums[-1] + nums[0]
    # 否则最小那个积木就没地方放
    lo = nums[-1]
    hi = nums[-1] + nums[0]
    # 只用检查lo和hi这2个长度能否放下，中间长度不用检查
    total = sum(nums)
    # for level in range(lo, hi+1):
    for level in [lo, hi]:
        if check(nums, total, level):
            return total // level
    return -1  
    
print(main())
        
        
                
        

