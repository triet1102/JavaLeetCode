/*
 * @lc app=leetcode id=14 lang=java
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
class Solution {
    public String longestCommonPrefix(String[] strs) {
        String longestCommon = strs[0];
        for (String s : strs) {
            while (!s.startsWith(longestCommon)) {
                longestCommon = longestCommon.substring(0, longestCommon.length() - 1);
            }
        }
        return longestCommon;
    }
}
// @lc code=end
