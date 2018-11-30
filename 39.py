# Runtime: 692 ms, faster than 4.73% of Python3 online submissions for Combination Sum.
# Difficulty: Medium

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        solutions = list()
        def cs_helper(path, target):
            if target == 0:
                path.sort()
                if path not in solutions:
                    solutions.append(path)
            elif target < 0:
                return
            else:
                for candidate in candidates:
                    cs_helper(path + [candidate], target - candidate)
        cs_helper([], target)
        return solutions
