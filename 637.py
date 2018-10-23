# Runtime: 92 ms, faster than 22.01% of Python3 online submissions for Average of Levels in Binary Tree.
# Difficulty: Easy

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        values = list()
        def helper(tree, level):
            if tree == None:
                return
            if len(values) <= level:
                values.append([tree.val])
            else:
                values[level].append(tree.val)
            helper(tree.left, level + 1)
            helper(tree.right, level + 1)
                
        helper(root, 0)
        averages = list()
        for value in values:
            averages.append(sum(value) / len(value))
        return averages
