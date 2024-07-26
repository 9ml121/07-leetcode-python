import heapq

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.height = 0

res = []
def mid_order(root):
    if not root:
        return
    
    mid_order(root.left)
    res.append(root.val)
    mid_order(root.right)


def solution(nums):
    minHeap = []
    for num in nums:
        node = Node(num)
        heapq.heappush(minHeap, (num, 0, node))  # num升序，树高度升序
    
    while len(minHeap) >= 2:
        l_val, l_height, l_node = heapq.heappop(minHeap)
        r_val, r_height, r_node = heapq.heappop(minHeap)
        
        node = Node(l_val + r_val)
        node.left = l_node
        node.right = r_node
        node.height = r_height + 1
        heapq.heappush(minHeap, (l_val + r_val, r_height + 1, node))
    
    _, _, root = minHeap[0]

    return root

n = 5
leafs = [5,15,40,30,10]
root = solution(leafs)

mid_order(root)
print(res)
# [40, 100, 30, 60, 15, 30, 5, 15, 10]