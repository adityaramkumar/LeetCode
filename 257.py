# Runtime: 44 ms, faster than 59.47% of Python3 online submissions for Binary Tree Paths.
# Difficulty: Easy

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = list()
        if root == None:
            return paths
        if root.right == None and root.left == None:
            return [str(root.val)]
        if root.left != None:
            for path in Solution.binaryTreePaths(None, root.left):
                paths.append(str(root.val) + '->' + path)
        if root.right != None:
            for path in Solution.binaryTreePaths(None, root.right):
                paths.append(str(root.val) + '->' + path)
        return paths
