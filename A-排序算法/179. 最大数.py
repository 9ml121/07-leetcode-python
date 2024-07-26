"""
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

 

示例 1：

输入：nums = [10,2]
输出："210"
示例 2：

输入：nums = [3,30,34,5,9]
输出："9534330"
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 10^9
"""


import functools
from typing import List
# todo 考察sort自定义排序规则

# 自定义sort()排序规则写法1：
class Cmp(str):
    def __lt__(x: str, y: str):
        # 排序规则：比较两个字符串x,y的拼接结果x+y和y+x哪个更大
        return x + y > y + x


class Solution:
    def largestNumber(self, nums_str: List[int]) -> str:
        # 重新排列nums每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
        # 先把nums中的所有数字转化为字符串，形成字符串数组 nums_str
        nums_str = list(map(str, nums_str))
        nums_str.sort(key=Cmp)
        ans = ''.join(nums_str)
        return ans if ans[0] != '0' else '0'


# 自定义sort()排序规则写法2：
class Solution:
    def largestNumber(self, nums_str: List[int]) -> str:
        # 重新排列nums每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
        nums_str = list(map(str, nums_str))

        def cmp(x: str, y: str):
            # functools.cmp_to_key排序规则：
            # 1.如果得到的值小于0，则交换值。
            # 2.如果值大于等于0，则不执行任何操作
            # 3.x代表为后面的一个元素，y代表前面的一个元素。
            return -1 if x+y > y+x else 1

        nums_str.sort(key=functools.cmp_to_key(cmp))
        ans = ''.join(nums_str)
        return ans if ans[0] != '0' else '0'


"""
https://blog.csdn.net/qq_48081868/article/details/115680333
Python3排序函数functools.cmp_to_key原理

compare=lambda x,y:1 if x<y else -1。
1.如果得到的值小于0，则交换值。如果值大于等于0，则不执行任何操作
2.x代表为后面的一个元素，y代表前面的一个元素。
"""

def test1():
    def compare(x, y): return 1 if x < y else -1

    test = [1, 2, 3, 4, 5]
    test.sort(key=functools.cmp_to_key(compare))
    print(test)  # [5, 4, 3, 2, 1]

# test1()

def test2():
    def compare(x, y): return 1 if x < y else print('x:', x)

    test = [1, 2, 3, 4, 5]
    test.sort(key=functools.cmp_to_key(compare))
    print(test)  # x: 2, 报错

# test2()

# 方法3：快速排序


