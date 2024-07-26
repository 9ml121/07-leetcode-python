"""
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。



示例 1：

输入：nums = [3,0,1]
输出：2
解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。
示例 2：

输入：nums = [0,1]
输出：2
解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。
示例 3：

输入：nums = [9,6,4,2,3,5,7,0,1]
输出：8
解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。
示例 4：

输入：nums = [0]
输出：1
解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。


提示：

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
nums 中的所有数字都 独一无二


进阶：你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?
"""
from typing import List


# 解法 1：原地数组哈希
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 原地哈希：时间复杂度 0(N), 空间复杂的 O(1)的解法
        # 0在下标为 0的位置，1 在下标为 1 的位置。。
        n = len(nums)
        for i in range(n):
            while nums[i] != i and nums[i] != n:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        print(nums)
        for i in range(n):
            if nums[i] != i:
                return i
        return n


# 解法 2：位运算：异或运算
"""
两个数字进行异或运算时，它们的二进制表示进行逐位比较。如果两个对应位的数字相同，则结果为0；如果不同，则结果为1
1.两个相同的数字进行异或运算的结果是0
2.当一个数字与0进行异或运算时，结果将是该数字本身。


 异或运算在计算机科学和电子工程中有广泛的应用。以下是一些异或运算的常见应用：
 1. 数据加密：异或运算可以用于对数据进行简单的加密和解密。通过将数据与一个密钥进行异或运算，可以实现简单的加密和解密过程。
 2. 校验和计算：在数据通信中，异或运算可以用于计算校验和。通过对数据的每个字节进行异或运算，可以生成一个校验和值，用于验证数据的完整性。
 3. 交换值：通过异或运算，可以在不使用额外变量的情况下，交换两个变量的值。这是因为异或运算满足交换律和结合律。
 4. 位操作：异或运算可以用于对二进制数进行位操作。例如，可以使用异或运算来翻转特定位的值，或者将特定位设置为1或0。
 总的来说，异或运算在编程和电子工程中具有广泛的应用，可以用于加密、校验和计算、位操作等多个领域。

解题思路：
1. 数组 nums 中有 n 个数，在这 n 个数的后面添加从 0 到 n 的每个整数，则添加了 n+1 个整数，共有 2n+1 个整数。
2. 在 2n+1 个整数中，丢失的数字只在后面 n+1 个整数中出现一次，其余的数字在前面 n 个整数中（即数组中）和后面 n+1个整数中各出现一次，即其余的数字都出现了两次。
3. 根据出现的次数的奇偶性，可以使用按位异或运算得到丢失的数字。按位异或运算 ^ 满足交换律和结合律，且对任意整数 x 都满足 x^x=0 和 x^0=x。
4. 由于上述 2n+1 个整数中，丢失的数字出现了一次，其余的数字都出现了两次，因此对上述 2n+1 个整数进行按位异或运算，结果即为丢失的数字。
"""


class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        # 先和新补的索引异或一下
        res ^= n
        # 和其他的元素、索引做异或
        for i in range(n):
            res ^= i ^ nums[i]
        return res


# 解法 3：数学
class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        arrSum = sum(nums)
        return total - arrSum


# 解法 4：排序(时间复杂度比上面 3 种方法高一点，O(nlogn))
class Solution4:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, num in enumerate(nums):
            if num != i:
                return i
        return len(nums)


if __name__ == '__main__':
    s = Solution2()
    print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(s.missingNumber([0]))
    print(s.missingNumber([1]))
    print(s.missingNumber([3, 0, 1]))
