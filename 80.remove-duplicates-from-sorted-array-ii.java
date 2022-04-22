/*
 * @lc app=leetcode id=80 lang=java
 *
 * [80] Remove Duplicates from Sorted Array II
 */

// @lc code=start
class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 1;
        int count = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i-1]) {
                if (count < 1) {
                    count++;
                    nums[k++] = nums[i];
                }
            } else {
                count = 0;
                nums[k++] = nums[i];
            }
        }

        return k;
    }
}
// @lc code=end

