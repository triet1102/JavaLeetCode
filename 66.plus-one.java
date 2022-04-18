/*
 * @lc app=leetcode id=66 lang=java
 *
 * [66] Plus One
 */

// @lc code=start
class Solution {
    public int[] plusOne(int[] digits) {
        int[] added_digits = new int[digits.length + 1];
        int check = 1;
        for (int i = added_digits.length - 1; i >= 1; i--) {
            if ((digits[i-1] + check) == 10) {
                added_digits[i] = 0;
                check = 1;
            } else {
                added_digits[i] = digits[i-1] + check;
                check = 0;
            }
        }
        if (check == 1) {
            added_digits[0] = 1;
            return added_digits;
        } else {
            System.arraycopy(added_digits, 1, digits, 0, digits.length);
            return digits;
        }
    }
}
// @lc code=end
