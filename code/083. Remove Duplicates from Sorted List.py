class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self.next is None:
            return None
        node = self.next
        nums = []
        nums.append(str(self.val))
        while node:
            nums.append(str(node.val))
            node = node.next
        return '->'.join(nums)

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return []
        node = head
        num = head.val
        while node.next:
            if num != node.next.val:
                num = node.next.val
                node = node.next
            else:
                node.next = node.next.next
        return head


if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(1)
    l.next.next = ListNode(2)
    l.next.next.next = ListNode(3)
    l.next.next.next.next = ListNode(3)
    s = Solution()
    print(s.deleteDuplicates(l))
