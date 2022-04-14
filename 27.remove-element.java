/*
 * @lc app=leetcode id=27 lang=java
 *
 * [27] Remove Element
 */

// @lc code=start
class Solution {
    public int removeElement(int[] nums, int val) {
        int nb = 0;
        int i = 0, j = 0;
        while (j<nums.length){
            if (nums[j] == val) {
                j++;
            } else {
                nums[i] = nums[j];
                i++;
                j++;
                nb++;
            }
        }
        return nb;
    }
}
// @lc code=end
