// Runtime: 4 ms, faster than 96.28% of Java online submissions for Two Sum.
// Difficulty: Easy

import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> saved = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            if(saved.containsKey(nums[i])) {
                return new int[]{saved.get(nums[i]), i};
            }
            saved.put(target - nums[i], i);
        }
        return new int[]{-1, -1};
    }
}
