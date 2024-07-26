
# 什么情况应当用 BFS 搜索
BFS 可以看成是层序遍历。从某个结点出发，BFS 首先遍历到距离为 1 的结点，然后是距离为 2、3、4…… 的结点。
因此，BFS 可以用来求最短路径问题。BFS 先搜索到的结点，一定是距离最近的结点。

> 腐烂的橘子
再看看这道题的题目要求：返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。
翻译一下，实际上就是求腐烂橘子到所有新鲜橘子的最短路径。那么这道题使用 BFS，应该是毫无疑问的了。



# BFS和DFS的区别
BFS 的核心思想应该不难理解的，就是把一些问题抽象成图，从一个点开始，向四周开始扩散。一般来说，我们写 BFS 算法都是用「队列」这种数据结构，每次将一个节点周围的所有节点加入队列。
BFS 相对 DFS 的最主要的区别是：BFS 找到的路径一定是最短的，但代价就是空间复杂度可能比 DFS 大很多

问题的本质就是让你在一幅「图」中找到从起点 start 到终点 target 的最近距离，这个例子听起来很枯燥，但是 BFS 算法问题其实都是在干这个事儿，

# 如何写（最短路径的） BFS 代码
```python
# todo 写法1: queue记录所有腐败的橘子坐标， 同时将depth也记录到queue(推荐)
def orangesRotting(grid: List[List[int]]) -> int:
    row, col = len(grid), len(grid[0])
    OFFSETS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queues = []
    depth = 0  # todo 记录队列循环次数，也就是橘子腐烂经过的分钟数
    # add the rotten orange to the queue
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 2:
                queues.append((i, j, depth))
    
    # bfs
    while queues:
        x, y, depth = queues.pop(0)  # todo 要理解为什么要用队列先进先出，才能实现这个？
        for offsetX, offsetY in OFFSETS:
            newX = x + offsetX
            newY = y + offsetY
            if 0 <= newX < row and 0 <= newY < col and grid[newX][newY] == 1:
                grid[newX][newY] = 2
                queues.append((newX, newY, depth + 1))  # todo 从队列尾部加入
            
```
另外一种写法：
```python
# 写法2：queue只记录标记为2的橘子坐标，depth单独统计（比较标准，但写起来麻烦）
def orangesRotting2(grid: List[List[int]]) -> int:
    row, col = len(grid), len(grid[0])
    OFFSETS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queues = []  # todo 记录所有腐败的橘子坐标， 注意也要将depth直接记录到queue

    # add the rotten orange to the queue
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 2:
                queues.append((i, j))

    # bfs
    depth = 0  # todo 记录队列循环次数，也就是橘子腐烂经过的分钟数
    while queues:
        exist = False
        n = len(queues)
        for i in range(n):
            x, y = queues.pop(0)  # todo 要理解为什么要用队列先进先出，才能实现这个？

            for offsetX, offsetY in OFFSETS:
                newX = x + offsetX
                newY = y + offsetY
                if 0 <= newX < row and 0 <= newY < col and grid[newX][newY] == 1:
                    exist = True
                    grid[newX][newY] = 2
                    queues.append((newX, newY))  # todo 从队列尾部加入
        # 判断坐标四周是否还有新鲜的橘子
        if exist:
            depth += 1
```

# 为什么要用队列实现，不用栈？
如果采用stack栈来保存感染区的话，则必然先弹栈一个感染区位置， 然后将其上下左右区域感染，
这个过程中，将新的感染区压栈，而之后再次弹栈，必然是第二批的感染区位置，也就是后进先出，
这将会产生深度优先搜索的效果。

# 1、为什么 BFS 可以找到最短距离，DFS 不行吗？
首先，你看 BFS 的逻辑，depth 每增加一次，队列中的所有节点都向前迈一步，这保证了第一次到达终点的时候，走的步数是最少的。
DFS 不能找最短路径吗？其实也是可以的，但是时间复杂度相对高很多。
你想啊，DFS 实际上是靠递归的**堆栈**记录走过的路径，你要找到最短路径，肯定得把二叉树中所有树杈都探索完才能对比出最短的路径有多长对不对？
而 BFS 借助**队列**做到一次一步「齐头并进」，是可以在不遍历完整棵树的条件下找到最短距离的。

**形象点说，DFS 是线，BFS 是面；DFS 是单打独斗，BFS 是集体行动**。这个应该比较容易理解吧。

