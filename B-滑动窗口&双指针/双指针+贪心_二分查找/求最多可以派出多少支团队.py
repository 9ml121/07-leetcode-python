""" 
https://fcqian.blog.csdn.net/article/details/127418310

题目描述
用数组代表每个人的能力，一个比赛活动要求参赛团队的最低能力值为N，每个团队可以由1人或者2人组成，且1个人只能参加1个团队，
计算出最多可以派出多少只符合要求的团队。

输入描述
第一行代表总人数，范围1-500000
第二行数组代表每个人的能力
数组大小，范围1-500000
元素取值，范围1-500000
第三行数值为团队要求的最低能力值，范围1-500000

输出描述
最多可以派出的团队数量

用例
输入	
5
3 1 5 7 9
8
输出	3
说明	说明 3、5组成一队   1、7一队  9自己一队  输出3

输入	
7
3 1 5 7 9 2 6
8
输出	4
说明	3、5组成一队，1、7一队，9自己一队，2、6一队，输出4

输入	3
1 1 9
8
输出	1
说明	9自己一队，输出1

"""

# todo 简单的左右双指针 + 贪心
# 类似：
# 输入
# 总人数，范围1-500000
n = int(input())
# 数组代表每个人的能力
nums = list(map(int, input().split()))
# 团队要求的最低能力值
limit = int(input())

# 输出：计算出最多可以派出多少只符合要求的团队。
# 按照能力从低到高排列，左指针指向能力最低，右指针指向能力最高
nums.sort()
l, r = 0, n-1
ans = 0  # 最多可以派出的团队数量

# 1人1组的个数
while r >= 0 and nums[r] >= limit:
    # 个人能力超过limit的1人一组
    ans += 1
    r -= 1
    
# 2人一组的个数
while l < r:
    # 能力最大的考虑携带能力最小的为一组
    if nums[l] + nums[r] >= limit:
        l += 1
        r -= 1
        ans += 1
    else:
        # 如果能力最小的搭配能力最大的还小于limit,就放弃能力最小的
        l += 1

print(ans)
