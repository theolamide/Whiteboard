class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode

        CN_L1 = l1
        CN_L2 = l2
        CN_L3 = l3
        TENS_INT = 0
        L3 = []

        while CN_L1 or CN_L2:
            Sum_Val = CN_L1.val + CN_L2.val + TENS_INT
            print(Sum_Val)
            if CN_L1.next and CN_L2.next:
                if Sum_Val < 10:
                    CN_L3.val = Sum_Val
                    CN_L1 = CN_L1.next
                    CN_L2 = CN_L2.next
                    L3.insert(0, CN_L3.val)
                    TENS_INT = 0
                else:
                    CN_L3.val = Sum_Val % 10
                    TENS_INT = 1
                    CN_L1 = CN_L1.next
                    CN_L2 = CN_L2.next
                    L3.insert(0, CN_L3.val)

            elif CN_L1.next and not CN_L2.next:
                if Sum_Val < 10:
                    CN_L3.val = Sum_Val
                    CN_L1 = CN_L1.next
                    L3.insert(0, CN_L3.val)
                    TENS_INT = 0
                else:
                    CN_L3.val = Sum_Val % 10
                    TENS_INT = 1
                    CN_L1 = CN_L1.next
                    L3.insert(0, CN_L3.val)

            elif CN_L2.next and not CN_L1.next:
                if Sum_Val < 10:
                    CN_L3.val = Sum_Val
                    CN_L2 = CN_L2.next
                    L3.insert(0, CN_L3.val)
                    TENS_INT = 0
                else:
                    CN_L3.val = Sum_Val % 10
                    TENS_INT = 1
                    CN_L2 = CN_L2.next
                    L3.insert(0, CN_L3.val)

            else:
                if Sum_Val < 10:
                    CN_L3.val = Sum_Val
                    CN_L1 = CN_L1.next
                    CN_L2 = CN_L2.next
                    L3.insert(0, CN_L3.val)
                    print(L3)
                else:
                    CN_L3.val = Sum_Val % 10
                    TENS_INT = 1
                    CN_L1 = CN_L1.next
                    CN_L2 = CN_L2.next
                    L3.insert(0, CN_L3.val)
                    L3.insert(0, TENS_INT)

        next = None

        for i in range(0, len(L3)):
            node = ListNode(L3[i])
            node.next = next
            next = node
        return node
