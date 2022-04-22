import java.util.ArrayList;

/*
 * @lc app=leetcode id=3 lang=java
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() <= 1) {
            return s.length();
        }

        ArrayList<Character> sub_string = new ArrayList<Character>();
        sub_string.add(s.charAt(0));
        int max_sub_length = 1;

        for (int i = 1; i < s.length(); i++) {
            if (!sub_string.contains(s.charAt(i))) {
                sub_string.add(s.charAt(i));
            } else {
                if (sub_string.size() > max_sub_length) {
                    max_sub_length = sub_string.size();
                }
                int idx = sub_string.indexOf(s.charAt(i));
                for (int j=0; j <= idx; j++) {
                    sub_string.remove(0);
                }
                sub_string.add(s.charAt(i));
            }
        }
        if (sub_string.size() > max_sub_length) {
            max_sub_length = sub_string.size();
        }
        return max_sub_length;
    }
}
// @lc code=end
