/*
 * @lc app=leetcode id=58 lang=java
 *
 * [58] Length of Last Word
 */

// @lc code=start
class Solution {
    public int lengthOfLastWord(String s) {
        s = s.strip();
        String[] s_split = s.split(" ");
        return s_split[s_split.length-1].length();
    }
}
// @lc code=end

