class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_new = l1
        l2_new = l2
        ResNode = None
        add = 0

        while True:
            """
            这里通过将next为None的链表数值表示为-1
            这样就不会导致第一个next为None后无法再通过None向下移动
            直到两个链表的值均为-1时链表结束
            结束后仍需要判断有无进位, 如5+5只需要一轮判断, 但是进位仍然需要表示出来
            """
            if l1_new.val == -1:
                add_1 = 0
            else:
                add_1 = l1_new.val
            if l2_new.val == -1:
                add_2 = 0
            else:
                add_2 = l2_new.val
            # tsum 表示取余
            # add  表示求整, 即进位部分
            tsum = (add_1 + add_2 + add) % 10
            add = (add_1 + add_2 + add) // 10
            l3 = ListNode(tsum)

            # 将新的类添加在链表上
            if ResNode == None:
                ResNode = l3
                Node_add = ResNode
            else:
                Node_add.next = l3
                Node_add = Node_add.next

            # 通过-1的值来表示链表结束
            if l1_new.next == None:
                l1_new.val = -1
            else:
                l1_new = l1_new.next
            if l2_new.next == None:
                l2_new.val = -1
            else:
                l2_new = l2_new.next

            # 判断两个链表是否均结束
            if l1_new.val == -1 and l2_new.val == -1:
                break

        # 判断有无进位
        if add != 0:
            l3 = ListNode(add)
            Node_add.next = l3

        return ResNode


if __name__ == '__main__':
    l1_1 = ListNode(2)
    l1_2 = ListNode(4)
    l1_3 = ListNode(3)
    l1_1.next = l1_2
    l1_2.next = l1_3

    l2_1 = ListNode(5)
    l2_2 = ListNode(6)
    l2_3 = ListNode(4)
    l2_1.next = l2_2
    l2_2.next = l2_3

    s1 = Solution()
    result = s1.addTwoNumbers(l1_1, l2_1)
    print(result.val, result.next.val, result.next.next.val)