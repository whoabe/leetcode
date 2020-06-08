'''
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
'''


class Solution:
    def minSubArrayLen(self, s, nums):
        '''
        approach
            2 pointers
            initalize minLength to arbitrary large value
            increment the right pointer every iteration of while loop, add the right value to the sum
            check if sum is >= s, if it is then calc minLength, subtract the left value from sum, and increment left by 1
        '''
        left, right, sum, minLength = 0, 0, 0, float('inf')
        while right < len(nums):
            sum += nums[right]
            while sum >= s:
                minLength = min(minLength, right-left+1)
                sum -= nums[left]
                left += 1
            right += 1
        return minLength if minLength <= len(nums) else 0


if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
