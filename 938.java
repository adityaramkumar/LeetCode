// Runtime: 0 ms, faster than 100.00% of Java online submissions for Range Sum of BST.
// Memory Usage: 45.5 MB, less than 96.74% of Java online submissions for Range Sum of BST.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int rangeSumBST(TreeNode root, int L, int R) {
        if (root == null) return 0;
        int sum = (root.val >= L && root.val <= R) ? root.val : 0;
        if (root.val < R)
            sum += rangeSumBST(root.right, L, R);
        if (root.val > L)
            sum += rangeSumBST(root.left, L, R);
        return sum;
    }
}
