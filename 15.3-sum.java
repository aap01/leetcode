/*
 * @lc app=leetcode id=15 lang=java
 *
 * [15] 3Sum
 *
 * https://leetcode.com/problems/3sum/description/
 *
 * algorithms Medium (30.88%) Likes: 16886 Dislikes: 1630 Total Accepted: 1.9M Total Submissions: 6M
 * Testcase Example: '[-1,0,1,2,-1,-4]'
 *
 * Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i !=
 * j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
 * 
 * Notice that the solution set must not contain duplicate triplets.
 * 
 * 
 * Example 1: Input: nums = [-1,0,1,2,-1,-4] Output: [[-1,-1,2],[-1,0,1]] Example 2: Input: nums =
 * [] Output: [] Example 3: Input: nums = [0] Output: []
 * 
 * 
 * Constraints:
 * 
 * 
 * 0 <= nums.length <= 3000 -10^5 <= nums[i] <= 10^5
 * 
 * 
 */

// @lc code=start
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        ArrayList<List<Integer>> res = new ArrayList<List<Integer>>();
        int arrayLen = nums.length;
        if (arrayLen < 3)
            return res;
        Arrays.sort(nums);
        // for (int i : nums)
        // System.out.print(i);

        for (int i = 0; i < arrayLen - 2; i++) {
            // System.out.println("res");
            int l = i + 1;
            int r = arrayLen - 1;
            int cur = nums[i];
            if (i == 0 || (i - 1 >= 0 && nums[i] != nums[i - 1]))
                while (l < r) {
                    int lVal = nums[l];
                    int rVal = nums[r];
                    int sum = lVal + cur + rVal;
                    if (sum == 0) {
                        res.add(Arrays.asList(lVal, cur, rVal));
                        l++;
                        while (l < r && nums[l] == nums[l - 1])
                            l++; // [-7, -7, -1, 1, 1, 1, 6, 6, 8]
                        while (l < r && nums[r] == nums[r - 1])
                            r--;
                    } else if (sum < 0) {
                        l++;
                    } else {
                        r--;
                    }
                }
        }
        return res;
    }
}
// @lc code=end

