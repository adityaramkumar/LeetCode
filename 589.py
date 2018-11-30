# Runtime: 124 ms, faster than 56.96% of Python online submissions for N-ary Tree Preorder Traversal.
# Difficulty: Easy

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        p_list = [root.val]
        for child in root.children:
            p_list.extend(self.preorder(child))
        return p_list
