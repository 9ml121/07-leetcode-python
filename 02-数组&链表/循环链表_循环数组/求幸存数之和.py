""" 
题目描述
给一个正整数数列 nums，一个跳数 jump，及幸存数量 left。

运算过程为：从索引0的位置开始向后跳，中间跳过 J 个数字，命中索引为 J+1 的数字，该数被敲出，并从该点起跳，以此类推，直到幸存 left 个数为止，然后返回幸存数之和。

约束：

0是第一个起跳点
起跳点和命中点之间间隔 jump 个数字，已被敲出的数字不计入在内。
跳到末尾时无缝从头开始（循环查找），并可以多次循环。
若起始时 left > len(nums) 则无需跳数处理过程。
方法设计：

/**
 * @param nums 正整数数列，长度范围 [1, 10000]
 * @param jump 跳数，范围 [1, 10000]
 * @param left 幸存数量，范围 [0, 10000]
 * @return 幸存数之和
 */
int sumOfLeft(int[] nums, int jump, int left)

输入描述
第一行输入正整数数列

第二行输入跳数

第三行输入幸存数量

输出描述
输出幸存数之和

用例
输入	1,2,3,4,5,6,7,8,9
4
3
输出	13
说明	从1（索引为0）开始起跳，中间跳过 4 个数字，因此依次删除 6,2,8,5,4,7。剩余1,3,9，返回和为13
"""
import collections
# 获取输入
nums = list(map(int, input().split(',')))
jump = int(input())
left = int(input())

# 方法1:基于动态数组实现循环跳表


def sumOfLeft(nums: list, jump, left):
    n = len(nums)
    i = 1
    while n > left:
        # 跳到的下一个数索引
        i = (i + jump) % len(nums)  # todo 注意这里动态数组索引变换规律
        # del nums[i]
        nums.pop(i)
        n -= 1

    # print(nums)
    return sum(nums)


# 方法2:基于双端队列实现循环跳表(部分超时！)
def sumOfLeft2(nums: list, jump, left):
    dq = collections.deque(nums)
    n = len(dq)
    i = -1
    while n > left:
        top = dq.popleft()
        if i == jump:
            # print(top)
            n -= 1
            i = 0
        else:
            dq.append(top)
            i += 1

    return sum(dq)


# 方法3:自己实现循环链表(注意：Python自定义循环链表的性能表现不佳，反而使用动态数组性能更好。)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    jump = 4
    left = 3
    # nums = list(map(int, input().split(',')))
    # jump = int(input())
    # left = int(input())
    print(sumOfLeft(nums, jump, left))
