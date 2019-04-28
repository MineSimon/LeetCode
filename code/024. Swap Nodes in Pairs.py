# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        nums = []
        nums.append(str(self.val))
        node = self.next
        while node is not None:
            nums.append(str(node.val))
            node = node.next
        return '->'.join(nums)


class Solution1:
    def swapPairs(self, head: ListNode) -> ListNode:
        count = 1
        pre = head
        cur = head.next
        # 将返回节点指向转换后的第二个节点
        if cur is not None:
            head = cur
        ppre = head

        while True:
            if cur is None:
                break
            pre.next = cur.next
            cur.next = pre
            pre, cur = cur, pre
            # 将两个交换节点前的节点指向转换后的前节点
            if ppre == head:
                ppre = cur
            else:
                ppre.next = pre
                ppre = cur
            # 判断节点存在性并向下遍历
            if cur.next is None:
                break
            else:
                pre = cur.next
                cur = pre.next
        return head


class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 建立一个新的头结点，方便后续进行交换
        dummyHead = ListNode(-1)
        dummyHead.next = head
        prev, p = dummyHead, head
        while p is not None and p.next is not None:
            q, r = p.next, p.next.next
            prev.next = q
            p.next = r
            q.next = p
            prev = p
            p = r
        return dummyHead.next



if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    s = Solution2()
    print(s.swapPairs(l))
