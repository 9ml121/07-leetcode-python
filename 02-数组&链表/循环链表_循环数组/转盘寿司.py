"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/134495777

OJ用例
https://hydro.ac/d/HWOD2023/p/OD351/solution

题目描述
寿司店周年庆，正在举办优惠活动回馈新老客户。

寿司转盘上总共有 n 盘寿司，prices[i] 是第 i 盘寿司的价格，

如果客户选择了第 i 盘寿司，寿司店免费赠送客户距离第 i 盘寿司最近的下一盘寿司 j，前提是 prices[j] < prices[i]，如果没有满足条件的 j，则不赠送寿司。

每个价格的寿司都可无限供应。

输入描述
输入的每一个数字代表每盘寿司的价格，每盘寿司的价格之间使用空格分隔，例如:

3 15 6 14

表示：

第 0 盘寿司价格 prices[0] 为 3
第 1 盘寿司价格 prices[1] 为 15
第 2 盘寿司价格 prices[2] 为 6
第 3 盘寿司价格 prices[3] 为 14
寿司的盘数 n 范围为：1 ≤ n ≤ 500

每盘寿司的价格 price 范围为：1 ≤ price ≤ 1000

输出描述
输出享受优惠后的一组数据，每个值表示客户选择第 i 盘寿司时实际得到的寿司的总价格。使用空格进行分隔，例如：

3 21 9 17

用例1
输入
3 15 6 14
输出
3 21 9 17
"""

# todo 循环数组 + 单调栈

# 方法1: 数据量10^3，采用双层for循环，暴力求解
# 输入的每一个数字代表每盘寿司的价格
prices = list(map(int, input().split()))
# print(prices)

def main1():
    n = len(prices)
    # 循环数组，当作数组长度*2进行遍历
    ans = []
    for i in range(n):
        cur = prices[i]
        for j in range(i+1, n*2):
            nxt = prices[j % n]
            if nxt < cur:
                cur += nxt
                break
        ans.append(cur)

    # print(ans)
    print(' '.join(map(str, ans)))


# 方法2: 倒序遍历，利用单调栈保存前面价格从高到低的数组元素，可以一次遍历完成
# 类似：04-栈&队列/栈/单调栈/503-下一个更大元素 II.py
# 类似：04-栈&队列/栈/单调栈/找朋友.py

def main(prices):
    # 3 15 6 14  => 3 21 9 17
    n = len(prices)
    stack = [] 
    ans = [0] * n
    # 循环数组，当作数组长度*2进行倒序遍历
    for i in range(n*2-1, -1, -1):
        p = prices[i%n]
        # print(f'i={i},p={p}')
        # 1.[n..n*2-1] 之间的元素只用来更新单调栈(单调递增)
        while stack and stack[-1] >= p:
            stack.pop()
        
        # 3 15 6 14  3 15 6 14  stack=[6, 3]
        # 2.[0..n-1] 之间的元素，开始更新结果集
        if i < n:
            if stack:
                ans[i] = p + stack[-1]
            else:
                ans[i] = p
            # print(f' ans={ans}')  
        stack.append(p)
        # print(f' stack={stack}')
    
    # print(ans)
    return ' '.join(map(str, ans))

print(main(prices))