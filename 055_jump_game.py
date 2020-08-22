
'''
55. Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 3 * 10^4
0 <= nums[i][j] <= 10^5

def canJump(self, nums: List[int]) -> bool:
'''


class Solution(object):
    def canJump(self, nums):
        '''
        approach:
            DP
                DP is an array of the furthest index it can jump to
                set the first index to the number
                loop through the array
                    if the dp of the previous index is smaller than the current index, the previous index cannot reach the current index, so ret False
                    set the dp of the current index to the max of current index + nums[index] which is the furthest, or the dp[i-1]
                    if dp[i] is greater than the last index, then return True
                return dp of the last index is greater than or equal to the last index
        '''
        # n = len(nums)
        # dp = [0]*n
        # dp[0] = nums[0]
        # for i in range(1, n-1):
        #     if dp[i-1] < i:
        #         return False
        #     dp[i] = max(i+nums[i], dp[i-1])
        #     if dp[i] >= n-1:
        #         return True
        # return dp[n-2] >= n-1

        '''
        loop through the nums array backwards
            if the current index + the nums[i] >= to the goal, set the goal to the current index
            want to see if the goal becomes 0 (if we can reach the last index, we good)
        '''
        goal = len(nums)-1
        for i in reversed(range(len(nums))):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))
