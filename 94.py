# Runtime: 36 ms, faster than 96.42% of Python3 online submissions for Binary Tree Inorder Traversal.
# Difficulty: Medium

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lst = list()
        if root == None:
            return []
        lst.extend(Solution.inorderTraversal(None, root.left))
        lst.append(root.val)
        lst.extend(Solution.inorderTraversal(None, root.right))
        return lst
