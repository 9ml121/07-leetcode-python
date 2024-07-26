from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.size = 0

    @staticmethod
    def fromList(arr: List[int]) -> 'ListNode':
        """通过数组创建链表,返回head节点"""
        if len(arr) == 0:
            raise ValueError("数组不能为空")
        head = ListNode(arr[0])
        cur = head
        cur.size = len(arr)
        for i in range(1, len(arr)):
            cur.next = ListNode(arr[i])
            cur = cur.next
        return head

    # 将链表反序列化为数组
    def toList(self) -> List[int]:
        """返回一个数组, 数组中包含链表的元素"""
        head = self
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        return arr

    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"
        # return str(self.value) + '->' + str(self.next)

    def __str__(self):
        """
        打印格式：1 -> 2 -> 3 -> None
        """
        p = self
        output = ""
        while p:
            output += str(p.val) + "->"
            p = p.next
        output += "None"
        return output

    def __lt__(self, other):
        return self.val < other.value

    def show(self):
        """
        打印格式：ListNode(1, ListNode(2, ListNode(4, None)))
        """
        p = self
        # self.size = self.getSize()

        output = ""
        while p:
            output += f'ListNode({p.val}, '
            p = p.next
        output += "None" + ')' * self.size

        print(output)

    def getSize(self) -> int:
        p = self
        while p:
            self.size += 1
            p = p.next
        return self.size


if __name__ == '__main__':
    nums = [1, 2, 4]
    # node = list2Node(nums)
    node = ListNode.fromList(nums)

    print(node)
    print(repr(node))
    node.show()
