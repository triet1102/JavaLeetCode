/*
 * @lc app=leetcode id=26 lang=java
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int k = 0;
        for (int i=1; i< nums.length; i++) {
            if (nums[i] == nums[k]) {
                continue;
            } else {
                k++;
                nums[k] = nums[i];
            }
        }
        return ++k;
    }
}
// @lc code=end

