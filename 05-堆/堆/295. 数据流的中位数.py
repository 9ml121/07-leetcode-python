"""
中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

例如 arr = [2,3,4] 的中位数是 3 。
例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
实现 MedianFinder 类:

MedianFinder() 初始化 MedianFinder 对象。

void addNum(int num) 将数据流中的整数 num 添加到数据结构中。

double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。

示例 1：

输入
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
输出
[null, null, null, 1.5, null, 2.0]

解释
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
提示:

-105 <= num <= 105
在调用 findMedian 之前，数据结构中至少有一个元素
最多 5 * 104 次调用 addNum 和 findMedian
"""
import heapq

"""
解题思路： 
要解决这个问题，我们可以使用两个堆来维护数据流中的数字。一个最大堆用于存储较小的一半数字，一个最小堆用于存储较大的一半数字。 
 
具体的解题步骤如下： 
 
1. 初始化两个堆，一个最大堆  max_heap  和一个最小堆  min_heap 。 
2. 当添加数字时，首先将数字加入最大堆  max_heap 。 
3. 然后将最大堆的堆顶元素（即最大值）取出，并将其加入最小堆  min_heap 。 
4. 如果最小堆的大小超过最大堆的大小，则将最小堆的堆顶元素取出，并将其加入最大堆。 
5. 最后，如果最大堆的大小大于最小堆的大小，则中位数为最大堆的堆顶元素；如果两个堆的大小相等，则中位数为两个堆顶元素的平均值。 

复杂度分析：

时间复杂度：O(logN)，优先队列的出队入队操作都是对数级别的，数据在两个堆中间来回操作是常数级别的，综上时间复杂度是 O(logN) 级别的；

空间复杂度：O(N)，使用了三个辅助空间，其中两个堆的空间复杂度是 O( 2N )，一个表示数据流元素个数的计数器 count，占用空间 O(1)，综上空间复杂度为 O(N)。
"""


class MedianFinder:

    def __init__(self):
        # 最小堆存升序数组后半部分数据
        self.min_heap = []
        # 最大堆存升序数组前半部分数据
        self.max_heap = []
        # 数组长度size为奇数时，中位数是max_heap堆顶元素，
        # size为偶数时，中位数是最大堆和最小堆堆顶元素和的1/2
        self.size = 0

    def addNum(self, num: int) -> None:
        self.size += 1
        if len(self.max_heap) <= len(self.min_heap):
            heapq.heappush(self.min_heap, num)
            top_min_heap = heapq.heappop(self.min_heap)
            # python默认是最小堆,所以最大堆要传入一个 tuple，用于比较的元素需是相反数，
            heapq.heappush(self.max_heap, (-top_min_heap, top_min_heap))
        else:
            heapq.heappush(self.max_heap, (-num, num))
            _, top_max_heap = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, top_max_heap)

    def findMedian(self) -> float:
        if self.size % 2 == 1:
            return float(self.max_heap[0][1])
        else:
            return (self.max_heap[0][1] + self.min_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

"""
除了使用两个堆的解法，还可以使用平衡二叉搜索树（AVL树）来实现。AVL树是一种自平衡的二叉搜索树，可以在O(logN)的时间内插入和删除节点，并保持树的平衡性。 
具体的解题步骤如下： 
1. 初始化一个空的AVL树。 
2. 当添加数字时，将数字插入AVL树中。 
3. 在插入过程中，保持AVL树的平衡性。 
4. 在插入完成后，通过中序遍历AVL树来获取中位数。 
Python代码实现如下
"""


class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        if not root:
            return AVLNode(val)
        elif val < root.value:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balanceFactor = self.getBalanceFactor(root)
        if balanceFactor > 1:
            if val < root.left.val:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if val > root.right.val:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalanceFactor(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z

        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z

        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y


class MedianFinder2:
    def __init__(self):
        self.avl_tree = AVLTree()

    def addNum(self, num: int) -> None:
        self.avl_tree.root = self.avl_tree.insert(self.avl_tree.root, num)

    def findMedian(self) -> float:
        inorder = []
        self.inorderTraversal(self.avl_tree.root, inorder)
        n = len(inorder)
        if n % 2 == 0:
            return (inorder[n // 2 - 1] + inorder[n // 2]) / 2
        else:
            return inorder[n // 2]

    def inorderTraversal(self, root, inorder):
        if root:
            self.inorderTraversal(root.left, inorder)
            inorder.append(root.value)
            self.inorderTraversal(root.right, inorder)


"""
除了使用两个堆或AVL树的解法外，还可以使用动态数组的解法来求解中位数。 
具体的解题步骤如下： 
1. 初始化一个空的动态数组。 
2. 当添加数字时，将数字插入动态数组中，并保持数组有序。 
3. 在插入完成后，通过数组的中间位置来获取中位数。 
4. 如果数组长度为偶数，则中位数为中间两个数的平均值；如果数组长度为奇数，则中位数为中间位置的数。 

使用动态数组的解法相对于使用两个堆或AVL树的解法，实现起来较为简单。但是在插入数字时需要保持数组有序，可能会有较高的时间复杂度。 
"""


# 超出时间限制
class MedianFinder3:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        i = 0
        while i < len(self.nums) and self.nums[i] < num:
            i += 1
        self.nums.insert(i, num)

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2 == 0:
            return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2
        else:
            return self.nums[n // 2]
