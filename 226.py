# Runtime: 36 ms, faster than 95.98% of Python3 online submissions for Invert Binary Tree.
# Difficulty: Easy

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        t = TreeNode(root.val)
        t.left = Solution.invertTree(None, root.right) 
        t.right = Solution.invertTree(None, root.left) 
        return t
