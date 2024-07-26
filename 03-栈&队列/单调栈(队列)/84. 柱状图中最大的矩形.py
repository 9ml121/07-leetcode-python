"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。



示例 1:



输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
示例 2：



输入： heights = [2,4]
输出： 4


提示：

1 <= heights.length <=105
0 <= heights[i] <= 104
"""
from typing import List

# 暴力枚举写法1：超时
"""
可以枚举以每个柱形为高度的最大矩形的面积。
具体来说是：依次遍历柱形的高度，对于每一个高度分别向两边扩散，求出以当前高度为矩形的最大宽度多少。
为此，我们需要：
    - 左边看一下，看最多能向左延伸多长，找到大于等于当前柱形高度的最左边元素的下标；
    - 右边看一下，看最多能向右延伸多长；找到大于等于当前柱形高度的最右边元素的下标。
时间复杂度：O(N^2)，这里 N 是输入数组的长度。
空间复杂度：O(1)。

看到时间复杂度为 O(N^2) 和空间复杂度为 O(1) 的组合，
那么我们是不是可以一次遍历，不需要中心扩散就能够计算出每一个高度所对应的那个最大面积矩形的面积呢？
很容易想到的优化的思路就是「以空间换时间」。我们需要在遍历的过程中记录一些信息。
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        sz = len(heights)
        for i in range(sz):
            curHeight = heights[i]
            left, right = i, i
            while left > 0 and heights[left - 1] >= curHeight:
                left -= 1
            while right < sz - 1 and heights[right + 1] >= curHeight:
                right += 1

            maxWidth = right - left + 1
            maxArea = max(maxArea, curHeight * maxWidth)

        return maxArea


# 暴力枚举写法2：超时
"""
是的，还有一种常用的方法是暴力枚举。该方法的基本思路是枚举所有可能的矩形，然后计算它们的面积，最后返回最大的面积。具体步骤如下： 
1. 枚举所有可能的矩形，即枚举所有可能的左右边界。 
2. 对于每个矩形，计算它的高度，即矩形中最小的高度。 
3. 计算当前矩形的面积，即高度乘以宽度。 
4. 返回所有矩形中面积最大的那个。 

该算法的时间复杂度为 $O(n^2)$，空间复杂度为 $O(1)$。虽然时间复杂度较高，但是在数据规模较小的情况下，该算法仍然是可行的。
代码实现如下：
"""


class Solution11:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                h = min(heights[i:j + 1])
                ans = max(ans, h * (j - i + 1))
        return ans


"""
代码优化1：
这段代码实现的是求解一个柱状图中最大的矩形面积。具体实现步骤如下：
1. 定义最大面积 maxArea 和柱子个数 sz，初始化为0。
2. 定义一个栈 stack，用于维护单调递增的柱子序列，以及两个数组 leftSize 和 rightSize，分别用于保存每个柱子左边和右边大于等于它的柱子个数。
3. 遍历输入的柱子高度 heights，对于每个柱子，将其与栈顶元素比较，
    - 如果当前柱子高度小于栈顶元素，则弹出栈顶元素，并更新 leftSize 或 rightSize 数组。
    - 如果当前柱子高度大于等于栈顶元素，则将当前柱子索引入栈。
4. 遍历完整个柱子序列后，再次遍历 heights，计算每个柱子的最大矩形面积，更新 maxArea 并返回。
 
 具体实现步骤中，
 1.使用栈来维护单调递增的柱子序列，可以保证每个柱子左边和右边第一个小于它的柱子的位置都可以通过栈中元素快速得到。
 2.左边大于等于当前元素的个数可以通过弹出栈顶元素并更新 leftSize 数组得到，右边大于等于当前元素的个数同理。
 3.最终，计算每个柱子的最大矩形面积时，左右两边大于等于当前元素的柱子个数都已经确定，只需要计算当前柱子的面积并更新 maxArea 即可。
"""


class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        sz = len(heights)

        # stack用于维护单调递增的柱子序列，保存的是遍历过的元素索引
        stack = []
        leftSize = [0] * sz  # 保存左边大于等于当前元素的个数
        for i in range(sz):
            curVal = heights[i]
            while stack and heights[stack[-1]] >= curVal:
                top = stack.pop()
                leftSize[i] += leftSize[top] + 1
            stack.append(i)

        stack = []
        rightSize = [0] * sz  # 保存右边大于等于当前元素的个数
        for i in range(sz - 1, -1, -1):
            curVal = heights[i]
            while stack and heights[stack[-1]] >= curVal:
                top = stack.pop()
                rightSize[i] += rightSize[top] + 1
            stack.append(i)

        for i in range(sz):
            curArea = heights[i] * (leftSize[i] + rightSize[i] + 1)
            maxArea = max(maxArea, curArea)

        return maxArea


"""
代码优化3：
计算左右两边大于等于当前元素的个数，可以直接根据索引加减计算，
前提是stack要设置2个哨兵（Sentinel）。，分别为-1和sz
"""


class Solution21:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        sz = len(heights)
        # 计算左边大于等于当前元素的个数
        leftSize = [0] * sz
        stack = [-1]  # 栈中保存的是遍历过的元素索引，初始值为-1
        for i in range(sz):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            leftSize[i] = i - stack[-1] - 1
            stack.append(i)
        # 计算右边大于等于当前元素的个数
        rightSize = [0] * sz
        stack = [sz]  # 栈中保存的是遍历过的元素索引，初始值为sz
        for i in range(sz - 1, -1, -1):
            while stack[-1] != sz and heights[stack[-1]] >= heights[i]:
                stack.pop()
            rightSize[i] = stack[-1] - i - 1
            stack.append(i)
        # 计算最大面积
        for i in range(sz):
            curArea = heights[i] * (leftSize[i] + rightSize[i] + 1)
            maxArea = max(maxArea, curArea)
        return maxArea


"""
代码优化4: 只需要设置一个哨兵
是的，还有一种更优秀的算法，称为单调栈。单调栈可以在 $O(n)$ 的时间复杂度内解决此问题。具体思路如下： 
1. 维护一个单调递增的栈，栈中存储的是每个元素的下标。 
2. 遍历数组，如果当前元素小于栈顶元素，则弹出栈顶元素，并计算以该元素为高度的最大矩形面积。 
3. 计算当前元素与栈顶元素之间的矩形面积，取最大值。 
4. 将当前元素的下标入栈。 
5. 遍历完数组后，如果栈不为空，则依次弹出栈顶元素，并计算以该元素为高度的最大矩形面积。 
"""


class Solution22:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]  # 维护单调递增栈，初始时栈中只有一个-1
        maxArea = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                # 如果当前元素小于栈顶元素，则弹出栈顶元素，并计算以该元素为高度的最大矩形面积
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                maxArea = max(maxArea, h * w)
            stack.append(i)
        while stack[-1] != -1:
            # 遍历完数组后，如果栈不为空，则依次弹出栈顶元素，并计算以该元素为高度的最大矩形面积
            h = heights[stack.pop()]
            w = len(heights) - stack[-1] - 1
            maxArea = max(maxArea, h * w)
        return maxArea


# 更精简的写法
"""
以上参考代码 2 需要考虑两种特殊的情况：
1.弹栈的时候，栈为空或者stack[-1] != -1；
2.遍历完成以后，栈中还有元素；

为此可以我们可以在输入数组的两端加上两个高度为 0 （或者是 0.5，只要比 1 严格小都行）的柱形，可以回避上面这两种分类讨论。
这两个站在两边的柱形有一个很形象的名词，叫做哨兵（Sentinel）。


头尾都加0的目的:
1.头部的0是为了不用判断栈是否为空, 因为题目中都是非负整数, 所以没有数会比0小, 即0一直会在栈底.
2.尾部的0是为了压出最后已经形成的单调栈的, 
    比如说示例: 2,1,5,6,2,3 遍历完之后单调栈[1,2,3],
    然后如果没有尾部0, 我们就会像weiwei哥第一段代码那样子, 最后考虑单调栈是否为空,做一个额外的判断,写很多类似的逻辑代码, 
    加入了尾部0, 就可以把遍历完单调栈[1,2,3]给压出来.

这里栈对应到高度，呈单调增加不减的形态，因此称为单调栈（Monotone Stack）。
它是暴力解法的优化，计算每个柱形的高度对应的最大矩形的顺序由出栈顺序决定。
"""


class Solution23:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        res = 0
        heights = [0] + heights + [0]  # 这里前后哨兵初始值设置为严格<1都可以，目的是保证第一个柱子一定可以入栈，stack剩余的柱子都可以出栈
        # 先放入哨兵结点，在循环中就不用做非空判断
        stack = [0]  # 这里初始值必须为0，单调递增
        size += 2

        for i in range(1, size):
            while heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                res = max(res, cur_height * cur_width)
            stack.append(i)
        return res


"""
计算柱状图中最大的矩形，可以使用分治法解决。具体思路如下： 
1. 找到数组中最小的元素，将该元素作为矩形的高度，计算以该元素为高度的最大矩形面积。 
2. 将数组分成两个部分，分别递归地处理左半部分和右半部分，找到左半部分和右半部分的最大矩形面积。 
3. 返回以上三个面积中的最大值。 
 
该算法的时间复杂度为 $O(n\log n)$，空间复杂度为 $O(\log n)$。
超出时间限制
代码实现如下：
"""


class Solution5:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def findMinIndex(heights, start, end):
            minIndex = start
            for i in range(start, end + 1):
                if heights[i] < heights[minIndex]:
                    minIndex = i
            return minIndex

        def largestRectangleAreaHelper(heights, start, end):
            if start > end:
                return 0
            minIndex = findMinIndex(heights, start, end)
            leftMaxArea = largestRectangleAreaHelper(heights, start, minIndex - 1)
            rightMaxArea = largestRectangleAreaHelper(heights, minIndex + 1, end)
            return max(leftMaxArea, rightMaxArea, heights[minIndex] * (end - start + 1))

        return largestRectangleAreaHelper(heights, 0, len(heights) - 1)
