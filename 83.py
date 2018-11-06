# Runtime: 32 ms, faster than 71.73% of Python online submissions for Remove Duplicates from Sorted List.
# Difficulty: Easy

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        if head.val == head.next.val:
            return self.deleteDuplicates(head.next)
        ln = ListNode(head.val)
        ln.next = self.deleteDuplicates(head.next)
        return ln
