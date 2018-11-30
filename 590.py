# Runtime: 112 ms, faster than 98.45% of Python online submissions for N-ary Tree Postorder Traversal.
# Difficulty: Easy

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        p_list = list()
        for child in root.children:
            p_list.extend(self.postorder(child))
        p_list.append(root.val)
        return p_list
