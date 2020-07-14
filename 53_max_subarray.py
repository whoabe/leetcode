'''
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

'''
approach:
    greedy/kadane's DP
        taking the max of the current element and the max of the prec local + the current element gives the local max 
'''


class Solution(object):
    def maxSubArray(self, nums):
        local = g = nums[0]
        for i in range(1, len(nums)):
            local = max(nums[i], local + nums[i])
            g = max(local, g)
        return g


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
