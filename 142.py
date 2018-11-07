# Runtime: 48 ms, faster than 71.21% of Python online submissions for Linked List Cycle II.
# Difficulty: Medium

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = set()
        while head != None:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return None
