# Runtime: 80 ms, faster than 97.06% of Python3 online submissions for Palindrome Linked List.
# Difficulty: Easy

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        runner = head
        stack = list()
        while runner:
            stack.append(runner.val)
            runner = runner.next
            
        while head:
            if head.val != stack.pop():
                return False
            head = head.next
            
        return True
