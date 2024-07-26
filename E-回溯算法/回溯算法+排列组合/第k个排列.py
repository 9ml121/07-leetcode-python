"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/127260110

题目描述
给定参数n，从1到n会有n个整数：1,2,3,…,n,这n个数字共有n!种排列。

按大小顺序升序列出所有排列的情况，并一一标记，

当n=3时,所有排列如下:

“123” “132” “213” “231” “312” “321”

给定n和k，返回第k个排列。

输入描述
输入两行，第一行为n，第二行为k，

给定n的范围是[1,9],给定k的范围是[1,n!]。

输出描述
输出排在第k位置的数字。

用例1
输入
3
3
输出
213
说明
3的排列有123,132,213…,那么第三位置就是213

用例2
输入
2
2
输出
21
说明
2的排列有12,21，那么第二位置的为21。
"""

# 获取输入
# n = int(input())
# k = int(input())

# 暴力解法：9个数的全排列 9!
# import math
# print(math.factorial(9)) # 362880
def solution1(n, k):
    # 全排列写法1
    def dfs(nums, path):
        if not nums:
            res.append(int(''.join(map(str, path))))
            return

        for i, num in enumerate(nums):
            path.append(num)
            dfs(nums[:i] + nums[i+1:], path)
            path.pop()

    # 全排列写法2
    def dfs2(path, vis=[False] * (n+1)):
        if len(path) == n:
            res.append(int(''.join(map(str, path))))
            return
        
        for i in range(1, n+1):
            if vis[i]:
                continue
            vis[i] = True
            path.append(i)
            dfs2(path, vis)
            vis[i] = False
            path.pop()

    res = []
    nums = list(range(1, n+1))
    # dfs(nums, [])
    dfs2([])
    res.sort()
    print(res[k-1])

# 优化解法
# n=4, 总共有4!(24)个全排列组合，求第k大的数，可以直接判断出是几开头
# 1,2,3,4开头的分别有3!(6)个数 ==>(k-1)//6
def solution2(n, k):
    arr = list(range(1,n+1))
    # 阶乘数组
    fact = [0] * (n+1)
    fact[1] = 1
    for i in range(2, n+1):
        fact[i] = fact[i-1] * i
    
    ans = ''
    while True:   
        if k == 1:
            ans += ''.join(map(str, arr))
            break
        
        # 计算第k大的数是以几开头
        start_idx = (k-1)//fact[n-1]
        start_num = arr[start_idx]
        ans += str(start_num)
        k %= fact[n-1]
        # k=0代表k是以x开头最大的那个数组合
        if k == 0:
            k = fact[n-1]
        
        # 更新剩余的数
        arr.pop(start_idx)
        n -= 1

    return int(ans)


if __name__ == '__main__':
    print(solution2(4,6))