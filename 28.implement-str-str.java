/*
 * @lc app=leetcode id=28 lang=java
 *
 * [28] Implement strStr()
 */

// @lc code=start
class Solution {
    public int strStr(String haystack, String needle) {
        int needle_len = needle.length();
        if (needle_len == 0) {
            return 0;
        }
        int haystack_len = haystack.length();
        
        for (int i = 0; i <= (haystack_len - needle_len); i++) {
            String sub = haystack.substring(i, i + needle_len);
            if (sub.equals(needle)) {
                return i;
            }
        }
        return -1;
    }
}
// @lc code=end

