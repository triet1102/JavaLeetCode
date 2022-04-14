/*
 * @lc app=leetcode id=35 lang=java
 *
 * [35] Search Insert Position
 */

// @lc code=start
class Solution {
    public int searchInsert(int[] nums, int target) {
        int head = 0;
        int tail = nums.length - 1;
        int middle;
        while (head <= tail) {
            middle = (head + tail) /2;
            if (nums[middle] == target) {
                return middle;
            } else if (nums[middle] > target) {
                tail = middle - 1;
            } else {
                head = middle + 1;
            }
        }
        return head;
    }
}
// @lc code=end
