"""
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。


示例 1:

输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
示例 2:

输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
示例 3:

输入: temperatures = [30,60,90]
输出: [1,1,0]


提示：

1 <= temperatures.n <= 105
30 <= temperatures[i] <= 100
"""
from typing import List


# todo 单调栈：及时去除无用数据，保证栈中数据有序
# 写法1：从后往前遍历
class Solution1:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。"""
        n = len(temperatures)
        ans = [0] * n
        st = []  # 单调递减,保存后面出现更高温度的索引

        for i in range(n - 1, -1, -1):
            t = temperatures[i]
            while st and t >= temperatures[st[-1]]:  # 注意，这里要非严格大于
                st.pop()

            # while循环外更新ans
            if st:
                ans[i] = st[-1] - i
            st.append(i)

        return ans

# 写法2：从前往后遍历
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # answer[i] 是指对于第 i 天，下一个更高温度出现在几天后
        n = len(temperatures)
        ans = [0] * n
        st = []  # 单调递减,保存前面没有找到更高温度的索引

        for i, t in enumerate(temperatures):
            while st and t > temperatures[st[-1]]: # 注意，这里要严格大于
                # while 循环内更新ans
                top = st.pop()
                ans[top] = i - top
            
            st.append(i)
        
        return ans