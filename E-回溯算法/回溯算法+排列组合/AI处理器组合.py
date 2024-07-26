"""
100分
题目描述：

某公司研发了一款高性能AI处理器。每台物理设备具备8颗AI处理器，编号分别为0、1、2、3、4、5、6、7。
编号0-3的处理器处于同一个链路中，编号4-7的处理器处于另外一个链路中，不通链路中的处理器不能通信，如下图所示。
现给定服务器可用的处理器编号数组array，以及任务申请的处理器数量num，找出符合下列亲和性调度原则的芯片组合。
如果不存在符合要求的组合，则返回空列表。

亲和性调度原则：

- 如果申请处理器个数为1，则选择同一链路，剩余可用的处理器数量为1个的最佳，其次是剩余3个的为次佳，然后是剩余2个，最后是剩余4个。
- 如果申请处理器个数为2，则选择同一链路剩余可用的处理器数量2个的为最佳，其次是剩余4个，最后是剩余3个。
- 如果申请处理器个数为4，则必须选择同一链路剩余可用的处理器数量为4个。
- 如果申请处理器个数为8，则申请节点所有8个处理器。

提示：

1. 任务申请的处理器数量只能是1、2、4、8
2. 编号0-3的处理器处于一个链路，编号4-7的处理器处于另外一个链路。
3. 处理器编号唯一，且不存在相同编号处理器

输入描述：

输入包含可用的处理器编号数组array，以及任务申请的处理器数量num两个部分。
第一行为array，第二行为num。例如：
[0, 1, 4, 5, 6, 7]
1
表示当前编号为0、1、4、5、6、7的处理器可用。任务申请1个处理器。
0<= array.n <= 8
0<= array[i] <= 7
num in [1, 2, 4, 8]

输出描述：
输出为组合列表，当array=[0, 1, 4, 5, 6, 7] ，num=1时，输出为[[0], [1]]

示例1

输入：
[0, 1, 4, 5, 6, 7]
1

输出：
[[0], [1]]
说明：
根据第一条亲和性调度原则，在剩余两个处理器的链路（0,1,2,3）中选择处理器。由于只有0和1可用，则返回任意一颗处理器即可

示例2

输入：
[0, 1, 4, 5, 6, 7]
4

输出：
[[4, 5, 6, 7]]
说明：

根据第三条亲和性调度原则，必须选择同一链路剩余可用的处理器数量为4个的环。
"""
import itertools

# 亲和性调度原则：
# - 如果申请处理器个数为1，则选择同一链路，剩余可用的处理器数量为1个的最佳，其次是剩余3个的为次佳，然后是剩余2个，最后是剩余4个。
# - 如果申请处理器个数为2，则选择同一链路剩余可用的处理器数量2个的为最佳，其次是剩余4个，最后是剩余3个。
# - 如果申请处理器个数为4，则必须选择同一链路剩余可用的处理器数量为4个。
# - 如果申请处理器个数为8，则申请节点所有8个处理器。
# 0<= array.n <= 8
# 0<= array[i] <= 7
# num in [1, 2, 4, 8]

'''
方法1：暴力枚举 + python组合工具包
'''
# cpu = eval(input())
cpu = [0, 1, 2, 4, 5, 6, 7]
num = int(input())
link1 = [elem for elem in cpu if elem <= 3]
n1 = len(link1)
link2 = [elem for elem in cpu if elem >= 4]
n2 = len(link2)
ans = []
pri = []  # 选择的优先级
if num == 1:
    pri = [1, 3, 2, 4]
    for p in pri:
        if n1 == p and n2 != p:
            # 选择link1
            ans = [[elem] for elem in link1]
            break
        elif n2 == p and n1 != p:
            ans = [[elem] for elem in link2]
            break
        elif n2 == p and n1 == p:
            ans = [[elem] for elem in cpu]
            break
        else:
            continue

elif num == 2:
    pri = [2, 4, 3]
    for p in pri:
        if n1 == p and n2 != p:
            # todo:选择link1, 2/3/4个选任意2个 [0,1,2]
            ans = [elem for elem in itertools.combinations(link1, 2)]
            break
        elif n2 == p and n1 != p:
            ans = [elem for elem in itertools.combinations(link2, 2)]
            break
        elif n2 == p and n1 == p:
            ans = [elem for elem in itertools.combinations(link1, 2)] + [elem for elem in itertools.combinations(link2, 2)]
            break
        else:
            continue

elif num == 4:
    pri = [4]
    p = 4
    if n1 == p and n2 != p:
        # 选择link1, 2/3/4个选任意2个 [0,1,2]?
        ans = [link1]
    elif n2 == p and n1 != p:
        ans = [link2]
    elif n2 == p and n1 == p:
        ans = [link1, link2]
    else:
        ans = []

elif num == 8:
    pri = [8]
    p = 8
    if n1+n2 == 8:
        ans = [cpu]
    else:
        ans = []

print(ans)


'''
解答2：按照dfs回溯算法 + 组合
'''
# 输入获取
arr = eval(input())
num = int(input())


# 算法入口
def getResult(arr, num):
    link1 = []
    link2 = []

    arr.sort()

    for e in arr:
        if e < 4:
            link1.append(e)
        else:
            link2.append(e)

    ans = []
    len1 = len(link1)
    len2 = len(link2)

    if num == 1:
        if len1 == 1 or len2 == 1:
            if len1 == 1:
                dfs(link1, 0, 1, [], ans)
            if len2 == 1:
                dfs(link2, 0, 1, [], ans)
        elif len1 == 3 or len2 == 3:
            if len1 == 3:
                dfs(link1, 0, 1, [], ans)
            if len2 == 3:
                dfs(link2, 0, 1, [], ans)
        elif len1 == 2 or len2 == 2:
            if len1 == 2:
                dfs(link1, 0, 1, [], ans)
            if len2 == 2:
                dfs(link2, 0, 1, [], ans)
        elif len1 == 4 or len2 == 4:
            if len1 == 4:
                dfs(link1, 0, 1, [], ans)
            if len2 == 4:
                dfs(link2, 0, 1, [], ans)
    elif num == 2:
        if len1 == 2 or len2 == 2:
            if len1 == 2:
                dfs(link1, 0, 2, [], ans)
            if len2 == 2:
                dfs(link2, 0, 2, [], ans)
        elif len1 == 4 or len2 == 4:
            if len1 == 4:
                dfs(link1, 0, 2, [], ans)
            if len2 == 4:
                dfs(link2, 0, 2, [], ans)
        elif len1 == 3 or len2 == 3:
            if len1 == 3:
                dfs(link1, 0, 2, [], ans)
            if len2 == 3:
                dfs(link2, 0, 2, [], ans)
    elif num == 4:
        if len1 == 4 or len2 == 4:
            if len1 == 4:
                ans.append(link1)
            if len2 == 4:
                ans.append(link2)
    elif num == 8:
        if len1 == 4 and len2 == 4:
            tmp = []
            tmp.extend(link1)
            tmp.extend(link2)
            ans.append(tmp)

    return ans


def dfs(arr, index, level, path, res):
    if len(path) == level:
        res.append(path[:])
        return

    for i in range(index, len(arr)):
        path.append(arr[i])
        dfs(arr, i + 1, level, path, res)
        path.pop()


# 算法调用
print(getResult(arr, num))
