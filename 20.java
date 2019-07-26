// Runtime: 2 ms, faster than 61.00% of Java online submissions for Valid Parentheses.
// Memory Usage: 34.2 MB, less than 100.00% of Java online submissions for Valid Parentheses.

import java.util.HashMap;

class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> openCloseMap = new HashMap<>();
        openCloseMap.put('(', ')');
        openCloseMap.put('{', '}');
        openCloseMap.put('[', ']');
        
        Stack<Character> parenthesis = new Stack<>();
        for (Character c : s.toCharArray()) {
            if (openCloseMap.containsKey(c)) {
                parenthesis.push(openCloseMap.get(c));
            } else {
                if (parenthesis.size() == 0 || !parenthesis.pop().equals(c))
                    return false;
            }
        }
        
        return parenthesis.size() == 0;
    }
}
