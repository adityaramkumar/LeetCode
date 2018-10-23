# Runtime: 40 ms, faster than 58.20% of Python3 online submissions for Binary Tree Pruning.
# Difficulty: Medium

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def contains_one(tree):
            if tree == None:
                return False
            return any([contains_one(b) for b in [tree.right, tree.left]] + [tree.val == 1])
        
        if contains_one(root):
            t = TreeNode(root.val)
            t.left = Solution.pruneTree(None, root.left)
            t.right = Solution.pruneTree(None, root.right)
            return t
