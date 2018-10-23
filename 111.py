# Runtime: 56 ms, faster than 74.98% of Python3 online submissions for Minimum Depth of Binary Tree.
# Difficulty: Easy

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        elif root.left == None and root.right != None:
            return 1 + Solution.minDepth(self, root.right)
        elif root.left != None and root.right == None:
            return 1 + Solution.minDepth(self, root.left)
        elif root.left == None and root.right == None:
            return 1
        elif root.left != None and root.right != None:
            return 1 + min(Solution.minDepth(self, root.left), Solution.minDepth(self, root.right))
