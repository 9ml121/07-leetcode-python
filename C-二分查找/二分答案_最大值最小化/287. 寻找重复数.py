"""
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。

你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

示例 1：
输入：nums = [1,3,4,2,2]
输出：2

示例 2：
输入：nums = [3,1,3,4,2]
输出：3


提示：

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次


进阶：

如何证明 nums 中至少存在一个重复的数字?
你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？
"""
from typing import List

# 思路1：B-二分查找 时间复杂度 O(NlogN)
'''
方法：B-二分查找
因为题目要找的是一个 整数，并且这个整数有明确的范围，所以可以使用「B-二分查找」。

重点理解：
这个问题使用「B-二分查找」是在数组 [1, 2,.., n] 中查找一个整数，而 并非在输入数组数组中查找一个整数。

「B-二分查找」的思路是先猜一个数（搜索范围 [left..right] 里位于中间的数 mid），然后统计原始数组中 小于等于 mid 的元素的个数 count：
1.如果 count 严格大于 mid。根据 抽屉原理，重复元素就在区间 [left..mid] 里；
2.否则，重复元素可以在区间 [mid + 1..right] 里找到，其实只要第 1 点是对的，这里肯定是对的，但要说明这一点，需要一些推导，我们放在最后说。

说明：
题目要求：你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
时间换空间的做法是反直觉的，这道问题当做练习即可，在开发中是绝对不建议这么做的，除非空间资源昂贵的时候。

时间复杂度：O(nlogn)，其中 n 为 nums 数组的长度。
  二分查找最多需要二分 O(logn) 次，
  每次判断的时候需要O(n) 遍历 nums 数组求解小于等于 mid 的数的个数，
  因此总时间复杂度为 O(nlogn)。

空间复杂度：O(1)。我们只需要常数空间存放若干变量。
'''


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        nums:只有一个整数 出现 两次或多次 ，其余整数至多出现 一次
        return:返回重复数
        """
        # 搜索范围在 1 到 len - 1 之间
        lo, hi = 1, len(nums) - 1

        while lo < hi:
            # 在 循环体内，先猜一个数 mid，
            # 然后遍历「输入数组」，统计小于等于 mid 的元素个数 count
            mid = (lo + hi) // 2
            cnt = sum(1 for num in nums if num <= mid)
            if cnt <= mid:
                # [lo..mid]没有重复数，下一轮在[mid+1, hi]查找
                lo = mid + 1
            else:
                # cnt > mid: [lo..mid]有重复数，可能存在多个重复数字
                hi = mid

        return lo


# 思路2：环形链表(双指针) 时间复杂度 O(N)
"""
一、使用环形链表II的方法解题（142.环形链表II），使用 142 题的思想来解决此题的关键是要理解如何将输入的数组看作为链表? 
## 首先明确前提，整数的数组 nums 中的数字范围是 [1,n]。考虑一下两种情况：

1. 如果数组中没有重复的数，以数组 [1,3,4,2]为例，我们将数组下标 n 和数 nums[n] 建立一个映射关系 f(n)， 
其映射关系 n->f(n)为：
idx  0 1 2 3 
nums 1 3 4 2
我们从下标为 0 出发，根据 f(n)计算出一个值，以这个值为新的下标，再用这个函数计算，以此类推，直到下标超界。
这样可以产生一个类似链表一样的序列。 0->1->3->2->4->null

2.如果数组中有重复的数，以数组 [1,3,4,2,2] 为例,我们将数组下标 n 和数 nums[n] 建立一个映射关系 f(n)， 
其映射关系 n->f(n) 为：
idx  0 1 2 3 4
nums 1 3 4 2 2
同样的，我们从下标为 0 出发，根据 f(n) 计算出一个值，以这个值为新的下标，再用这个函数计算，以此类推产生一个类似链表一样的序列。
 0->1->3->2->4->2->4->2->…… 这里 2->4 是一个循环，

从理论上讲，数组中如果有重复的数，那么就会产生多对一的映射，这样，形成的链表就一定会有环路了，

综上:
1.数组中有一个重复的整数 <==> 链表中存在环 
2.找到数组中的重复整数 <==> 找到链表的环入口

二、至此，问题转换为 142 题。那么针对此题，快、慢指针该如何走呢?
根据上述数组转链表的映射关系，可推出：
142 题中慢指针走一步 slow = slow.next ==> 本题 slow = nums[slow] 
142 题中快指针走两步 fast = fast.next.next ==> 本题 fast = nums[nums[fast]]
"""


class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        """查找重复数
        思路2：双指针
        idx  0 1 2 3 4
        nums 1 3 4 2 2
        """
        # 初始化慢指针和快指针
        slow, fast = 0, 0
        # 1.找到相遇点(链表中存在环)
        while True:
            # 慢指针走一步,快指针走两步
            slow = nums[slow]  # slow  1->3->2->4->2->4->...
            fast = nums[nums[fast]]  # 3->4->4->4...
            if slow == fast:  # show=4
                break
        # 2.重置快指针
        fast = 0
        # 3.找到重复数(找到链表的环入口)
        while fast != slow:
            # 快慢指针同步走
            fast = nums[fast]  # 1->3->2->4->2->4->...
            slow = nums[slow]  # 2->4->2...
        return slow


"""
复杂度分析
时间复杂度：O(n)。「Floyd 判圈算法」时间复杂度为线性的时间复杂度。
空间复杂度：O(1)。我们只需要常数空间存放若干变量。
"""
if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    sol = Solution2()
    print(sol.findDuplicate(nums))
