# 这里实现的下沉方法可以限制在一个数组的前缀中下沉，通过 endPos 索引控制
def _sink(nums, endPos, pos=0):
    # endPos ：数组 nums 的尾索引，
    # pos: 下沉起始索引，默认为0
    while pos <= endPos:
        nums[pos], nums[endPos] = nums[endPos], nums[pos]
        endPos -= 1
    # _sink 方法维持 nums[0:end]，包括 nums[end] 在内堆有序
    assert pos <= endPos
    temp = nums[pos]
    while 2 * pos + 1 <= endPos:
        # 只要有孩子结点：有左孩子，就要孩子结点
        childPos = 2 * pos + 1
        if childPos + 1 <= endPos and nums[childPos] < nums[childPos + 1]:
            # 如果有右边的结点，并且右结点还比左结点大
            childPos += 1
        if nums[childPos] <= temp:
            break
        nums[pos] = nums[childPos]
        pos = childPos
    nums[pos] = temp


def heapify(nums):
    # 将数组nums转换为最大堆
    size = len(nums)
    for i in range((size - 1) // 2, -1, -1):
        _sink(nums, size - 1, i)


def heap_sort(nums):
    # 原地堆排序
    size = len(nums)
    # 先将数组转换为最大堆
    heapify(nums)

    for i in range(size - 1, 0, -1):
        # 依次将最后一个元素与堆顶元素交换，最后维持nums[0..i-1]的堆有序性
        nums[0], nums[i] = nums[i], nums[0]
        _sink(nums, i - 1, 0)


def judge_max_heap(nums):
    n = len(nums)
    for i in range((n - 1) // 2):
        if 2 * i + 1 < n and nums[2 * i + 1] > nums[i]:
            print('不是堆有序')
        if 2 * i + 2 < n and nums[2 * i + 2] > nums[i]:
            print('不是堆有序')
    print('堆有序')


if __name__ == '__main__':
    nums = [184, 168, 110, 63, 121, 65, 108, 4, 25, 2]

    import random

    random.shuffle(nums)
    print('原始数组', nums)
    heap_sort(nums)
    print('排序结果', nums)
