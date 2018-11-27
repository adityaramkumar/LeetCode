# Runtime: 44 ms, faster than 37.20% of Python3 online submissions for Binary Tree Preorder Traversal.
# Difficulty: Medium

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) \
            + self.preorderTraversal(root.right) 
