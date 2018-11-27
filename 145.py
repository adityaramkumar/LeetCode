# Runtime: 44 ms, faster than 37.94% of Python3 online submissions for Binary Tree Postorder Traversal.
# Difficulty: Hard

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.postorderTraversal(root.left) \
            + self.postorderTraversal(root.right) \
            + [root.val]
