/*
 * @lc app=leetcode id=13 lang=java
 *
 * [13] Roman to Integer
 */

// @lc code=start
class Solution {
    public int romanToInt(String s) {
        int sum = 0;
        int i = 0;
        int l = s.length();
        while (i < l) {
            switch (s.charAt(i)) {
                case 'I':
                    if (i != l - 1) {
                        if (s.charAt(i+1) =='V') {
                            sum += 4;
                            i++;
                        } else if (s.charAt(i+1) == 'X') {
                            sum += 9;
                            i++;
                        } else {
                            sum += 1;
                        }
                    } else {
                        sum += 1;
                    }   
                    i++;
                    break;
                
                case 'V':
                    sum += 5;
                    i++;
                    break;
                
                case 'X':
                    if (i != l - 1) {
                        if (s.charAt(i+1) =='L') {
                            sum += 40;
                            i++;
                        } else if (s.charAt(i+1) == 'C') {
                            sum += 90;
                            i++;
                        } else {
                            sum += 10;
                        }
                    } else {
                        sum += 10;
                    }
                    i++;
                    break;
                
                case 'L':
                    sum += 50;
                    i++;
                    break;                  
                
                case 'C':
                    if (i != l - 1) {
                        if (s.charAt(i+1) =='D') {
                            sum += 400;
                            i++;
                        } else if (s.charAt(i+1) == 'M') {
                            sum += 900;
                            i++;
                        } else {
                            sum += 100;
                        }
                    } else {
                        sum += 100;
                    }
                    i++;
                    break;
                
                case 'D':
                    sum += 500;
                    i++;
                    break;
                
                case 'M':
                    sum += 1000;
                    i++;
                    break;

            }
        }


        return sum;
    }
}
// @lc code=end
