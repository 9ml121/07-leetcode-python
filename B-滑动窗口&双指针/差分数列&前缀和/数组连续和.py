"""
https://fcqian.blog.csdn.net/article/details/127170844
题目描述
给定一个含有N个正整数的数组, 求出有多少个连续区间（包括单个正整数）, 它们的和大于等于x。

输入描述
第一行两个整数N x（0 < N <= 100000, 0 <= x <= 10000000)

第二行有N个正整数（每个正整数小于等于100)。

输出描述
输出一个整数，表示所求的个数。

注意：此题对效率有要求，暴力解法通过率不高，请考虑高效的实现方式。

用例
输入	
3 7
3 4 7

输出	4
说明	第一行的3表示第二行数组输入3个数，第一行的7是比较数，用于判断连续数组是否大于该数；组合为 3 + 4; 3 + 4 + 7; 4 + 7; 7; 
都大于等于指定的7；所以共四组。

输入	
10 10000
1 2 3 4 5 6 7 8 9 10

输出	0
说明	所有元素的和小于10000，所以返回0。
"""

# todo 考察“前缀和 & 差分数列”
# 输入
# 给定一个含有N个正整数的数组, 求出有多少个连续区间（包括单个正整数）, 它们的和大于等于x。
n, x = map(int, input().split())
nums = list(map(int, input().split()))

# 输出：输出一个整数，表示所求的个数。
ans = 0
preSum = [0] * (n+1)
for i in range(1, n+1):
    preSum[i] = preSum[i-1] + nums[i-1]

l = 0
r = 1
while r <= n:
    # preSum[l..r]的区间和要小于x,一旦大于等于x,就说明n-r+1个区间都满足条件
    if preSum[r] - preSum[l] >= x:
        ans += (n-r+1)
        l += 1
        # 注意：这里判断是为了避免l跑到r后面
        if l == r:
            r += 1
    else:
        r += 1
print(ans)
