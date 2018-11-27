# Runtime: 108 ms, faster than 95.44% of Python3 online submissions for Add Two Numbers.
# Difficulty: Medium

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        total, carry = [], 0
        while l1 and l2:
            digit_sum = l1.val + l2.val + carry
            total, carry = total + [digit_sum % 10], digit_sum // 10
            l1, l2 = l1.next, l2.next
        
        remaining = l1 if l1 else l2
        while remaining:
            digit_sum = remaining.val + carry
            total, carry = total + [digit_sum % 10], digit_sum // 10
            remaining = remaining.next
        
        while carry:
            total, carry = total + [carry % 10], carry // 10
        
        rlist = ListNode(total[0])
        head = rlist
        for element in total[1:]:
            rlist.next = ListNode(element)
            rlist = rlist.next
        return head
