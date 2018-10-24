# Runtime: 44 ms, faster than 95.78% of Python online submissions for Linked List Cycle.
# Difficulty: Easy

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()
        while head != None:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False
