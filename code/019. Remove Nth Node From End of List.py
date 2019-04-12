# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 在head前放置一个哨兵, 可以解决删除首个node的情况
        res = ListNode(None)
        res.next = head
        l1 = res
        l2 = res
        count = 0
        while l2.next:
            if count < n:
                count += 1
                l2 = l2.next
            else:
                l1, l2 = l1.next, l2.next
        l1.next = l1.next.next
        return res.next
