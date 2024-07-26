""" 
题目描述
给定长度为 n 的无序的数字数组，每个数字代表二叉树的叶子节点的权值，数字数组的值均大于等于1。

请完成一个函数，根据输入的数字数组，生成哈夫曼树，并将哈夫曼树按照中序遍历输出。

为了保证输出的二叉树中序遍历结果统一，增加以下限制：

二叉树节点中，左节点权值小于右节点权值，根节点权值为左右节点权值之和。当左右节点权值相同时，左子树高度小于等于右子树高度。

注意：

所有用例保证有效，并能生成哈夫曼树。

提醒：

哈夫曼树又称为最优二叉树，是一种带权路径长度最短的二叉树。

所谓树的带权路径长度，就是树中所有的叶节点的权值乘上其到根节点的路径长度（若根节点为 0 层，叶节点到根节点的路径长度为叶节点的层数）

输入描述
例如：由叶子节点：5 15 40 30 10，生成的最优二叉树如下图所示，该树的最短带权路径长度为：40 * 1 + 30 * 2 + 5 * 4 + 10 * 4 = 205。



输出描述
输出一个哈夫曼树的中序遍历数组，数值间以空格分隔
 

用例
输入	
5
5 15 40 30 10
输出	40 100 30 60 15 30 5 15 10
说明	根据输入，生成哈夫曼树，按照中序遍历返回。所有节点中，左节点权值小于等于右节点权值之和。当左右节点权值相同时，左子树高度小于右子树。结果如上图所示。

4
80 80 20 60 

4
3 7 8 9

62
655 380 733 99 17 124 137 391 106 322 284 28 568 19 775 97 695 626 570 46 8 166 356 340 617 108 202 61 650 572 601 362 581 21 579 10 1 422 918 329 829 677 302 12 318 358 822 139 271 55 920 338 347 14 50 378 289 313 186 30 360 619

"""
import heapq

n = int(input())
nums = list(map(int, input().split()))

class Node:
    def __init__(self,val, left=None, right=None, height=0) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.height = height

    # 优先级比较时，权重小的优先级更高，权重相同时，高度小的优先级更高
    def __lt__(self, other:'Node'):
        if self.val != other.val:
            return self.val < other.val
        else:
            return self.height < other.height
        
seq = []
def midOrder(root:'Node'):
    global seq
    if root.left:
        midOrder(root.left)
    seq.append(root.val)
    if root.right:
        midOrder(root.right)

# 每次选出最小的2个数
minHeap = []
for w in nums:
    node = Node(w)
    heapq.heappush(minHeap, node)

while len(minHeap) >= 2:
    ln = heapq.heappop(minHeap)
    rn = heapq.heappop(minHeap)
    faNode = Node(ln.val + rn.val, ln, rn, rn.height + 1)
    heapq.heappush(minHeap, faNode)

# 最后minHeap只有1个元素
root = minHeap[0]
midOrder(root)
print(' '.join(map(str,seq)))

