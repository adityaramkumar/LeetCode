// Runtime: 1 ms, faster than 95.17% of Java online submissions for Best Time to Buy and Sell Stock II.
// Memory Usage: 36.6 MB, less than 99.94% of Java online submissions for Best Time to Buy and Sell Stock II.

class Solution {
    public int maxProfit(int[] prices) {
        // Greedy Algorithm: One pass
        // Time O(N), Space O(1)
        
        int buyprice = Integer.MAX_VALUE, profit = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] > buyprice) 
                profit += prices[i] - buyprice;
            buyprice = prices[i];
        }
        return profit;
    }
}
