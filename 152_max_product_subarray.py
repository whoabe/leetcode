'''
152. Maximum Product Subarray
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

def maxProduct(self, nums: List[int]) -> int:
'''


class Solution(object):
    def maxProduct(self, nums):
        '''
        approach
            dynamic programming
        '''
        localMin = localMax = g = nums[0]
        for i in range(1, len(nums)):
            tmp = localMax
            localMax = max(nums[i], localMax*nums[i], localMin*nums[i])
            localMin = min(nums[i], tmp*nums[i], localMin*nums[i])
            g = max(localMax, g)
        return g


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.maxProduct([-2, 3, -4]))
