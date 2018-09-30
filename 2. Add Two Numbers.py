# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # thought 1: transfer the linked list to num and transfer the sum back
        # defect: cannot handle large number

        # thought 2: do the add digit by digit
        # error: forgot to consider last num is carry(like 5 + 5 = 10)

        head = ListNode(0)
        curr = head
        num = 0
        while l1 is not None or l2 is not None or num is not 0:
            if l1 is not None:
                num += l1.val
                l1 = l1.next
            if l2 is not None:
                num += l2.val
                l2 = l2.next
            curr.next = ListNode(num%10)
            curr = curr.next
            num /= 10
        return head.next

# test
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l3 = Solution().addTwoNumbers(l1, l2)
print l3.val, l3.next.val, l3.next.next.val

l1 = ListNode(5)
l2 = ListNode(5)
l3 = Solution().addTwoNumbers(l1, l2)
print l3.val, l3.next.val
