"""
题目来源
https://acm.hdu.edu.cn/showproblem.php?pid=2063

题目描述
RPG girls今天和大家一起去游乐场玩，终于可以坐上梦寐以求的过山车了。

可是，过山车的每一排只有两个座位，而且还有条不成文的规矩，就是每个女生必须找个男生做partner和她同坐。

但是，每个女孩都有各自的想法，举个例子把，

Rabbit只愿意和XHD或PQK做partner
Grass只愿意和linle或LL做partner
PrincessSnow愿意和水域浪子或伪酷儿做partner
考虑到经费问题，boss刘决定只让找到partner的人去坐过山车，其他的人，嘿嘿，就站在下面看着吧。

聪明的Acmer，你可以帮忙算算最多有多少对组合可以坐上过山车吗？

输入描述
输入数据的第一行是三个整数K , M , N，分别表示可能的组合数目，女生的人数，男生的人数。

0 < K ≤ 1000
1 ≤ N, M ≤ 500
接下来的K行，每行有两个数，分别表示女生 Ai 愿意和男生 Bj 做partner。

最后一个0结束输入。

输出描述
对于每组数据，输出一个整数，表示可以坐上过山车的最多组合数。

用例
输入	
6 3 3
1 1
1 2
1 3
2 1
2 3
3 1
0
输出	3
"""



# 输入获取
k, m, n = map(int, input().split())  # k个配对, m个女生, n个男生

edges = [[False] * (n + 1) for _ in range(m + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    edges[a][b] = True  # edges[a][b] == true 表示 a女生 和 b男生 可以配对

# 最后一个0结束输入。
input()

match = [0] * (n + 1)  # match[b] 表示男生b确定配对的女生


def dfs(a, vis): # a表示女生编号
    #  遍历男生b
    for b in range(1, n + 1):
        # 如果男生b不在女生a发起的探索的增广路中，且a,b可以配对
        if not vis[b] and edges[a][b]:
            # 则当前增广路加入男生b
            vis[b] = True

            # 如果男生b没有被其他人配对 || 已经和其他人配对，但是男生b当前配对的女生match[b]可以放弃男生b，而和其他男生配对
            if match[b] == 0 or dfs(match[b], vis):
                # 则男生b可以和女生a配对，即配对成功，match[b] = a
                match[b] = a
                return True

    return False


# 算法入口
def getResult():
    ans = 0

    for a in range(1, m + 1):
        # vis[b] 表示男生b是否在a女生发起的增广路探索中
        vis = [False] * (n + 1)

        # 如果a找到配对男生，则配对边+1
        if dfs(a, vis):
            ans += 1

    return ans


# 算法调用
print(getResult())
