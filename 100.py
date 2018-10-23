# Runtime: 36 ms, faster than 91.77% of Python3 online submissions for Same Tree.
# Difficulty: Easy

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        return Solution.isSameTree(None, p.right, q.right) and Solution.isSameTree(None, p.left, q.left)
