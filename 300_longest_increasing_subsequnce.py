'''
300. Longest Increasing Subsequence
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
'''

'''
approach:
    brute force
        find all increasing subsequences and return the max length of the longest subsequence
    dynamic programming bottom up
    
'''


class Solution(object):
    def lengthOfLIS(self, nums):
        # Brute Force
        # TC: O(2^N), SC: O(N)
        # def max_lis(idx, cur_max):
        #     if idx == len(nums):
        #         return 0
        #     if nums[idx] > cur_max:
        #         return max(1 + max_lis(idx + 1, nums[idx]), max_lis(idx + 1, cur_max))
        #     return max_lis(idx + 1, cur_max)
        # return max_lis(0, float('-inf'))

        # dynamic programming
        # TC: O(N ^ 2), SC: O(N)
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
