# Runtime: 48 ms, faster than 73.86% of Python3 online submissions for Merge Two Sorted Lists.
# Difficulty: Easy

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        if l1.val <= l2.val:
            rln = ListNode(l1.val)
            rln.next = Solution.mergeTwoLists(self, l1.next, l2)
        else:
            rln = ListNode(l2.val)
            rln.next = Solution.mergeTwoLists(self, l1, l2.next)
        return rln
