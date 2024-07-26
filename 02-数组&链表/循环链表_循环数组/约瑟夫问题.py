"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/127979790

题目描述
输入一个由随机数组成的数列（数列中每个数均是大于 0 的整数，长度已知），和初始计数值 m。

从数列首位置开始计数，计数到 m 后，将数列该位置数值替换计数值 m，

并将数列该位置数值出列，然后从下一位置从新开始计数，直到数列所有数值出列为止。

如果计数到达数列尾段，则返回数列首位置继续计数。

请编程实现上述计数过程，同时输出数值出列的顺序。

比如：输入的随机数列为：3,1,2,4，初始计数值 m=7，从数列首位置开始计数（数值 3 所在位置）

第一轮计数出列数字为 2，计数值更新 m=2，出列后数列为 3,1,4，从数值 4 所在位置从新开始计数

第二轮计数出列数字为 3，计数值更新 m=3，出列后数列为 1,4，从数值 1 所在位置开始计数

第三轮计数出列数字为 1，计数值更新 m=1，出列后数列为 4，从数值 4 所在位置开始计数

最后一轮计数出列数字为 4，计数过程完成。输出数值出列顺序为：2,3,1,4。

要求实现函数：

void array_iterate(int len, int input_array[], int m, int output_array[])
输入描述
第一行是初始数列intput_array

第二行是初始数列的长度len

第三行是初始计数值m

输出描述
数值出列顺序

用例1
输入
3,1,2,4
4
7
输出
2,3,1,4

"""
import collections

# 获取输入
arr = list(map(int, input().split(',')))
n = int(input())
jump = int(input())

# 方法1:基于动态数组实现循环链表(性能也可以！)
def array_iterate(n: int, arr: list, jump: int):
    out_arr = []
    idx = 0
    while n > 0:
        idx = (idx+jump-1) % n  # todo 注意这里动态数组索引变换规律
        num = arr.pop(idx)
        n -= 1
        out_arr.append(num)
        jump = num
    print(','.join(map(str, out_arr)))


# 方法2:基于双端队列实现循环跳表
"""
本题就是约瑟夫环的变种题。
约瑟夫环的解题有多种方式，比较容易理解和实现的可以使用双端队列。
即intput_array当成双端队列，从队头取出元素，判断此时计数是否为m：
    若是，则将取出的元素加入output_arr，并将取出的元素的值赋值给m，然后len--，计数重置为1
    若不是，则将取出的元素塞回intput_array的队尾，仅计数++
"""

def array_iterate2(n: int, arr: list, jump: int):
    dq = collections.deque(arr)
    out_arr = []
    i = 1
    while n > 0:
        num = dq.popleft()
        if i == jump:
            out_arr.append(num)
            jump = num
            i = 1
            n -= 1
        else:
            dq.append(num)
            i += 1
            
    print(','.join(map(str, out_arr)))


array_iterate2(n, arr, jump)

# 方法3:自己实现循环链表(注意：Python自定义循环链表的性能表现不佳，反而使用动态数组性能更好。)
