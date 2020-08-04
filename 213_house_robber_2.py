'''
213. House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

def rob(self, nums: List[int]) -> int:
'''

'''
approach:
    like house rob 1 but choose the max of without the first house or without the last house

    dynamic programming
        if there's 1 house, then the amount of money is the amount from the 1st house
        2 houses, take the max of the two houses
        3 houses, take the max of (1st and 3rd) and 2nd
        basically apply this to the last item [-1] to find the max profit
'''


class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def simpleRob(nums):
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                return nums[0]
            nums[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                nums[i] = max((nums[i-2]+nums[i]), nums[i-1])
            return nums[-1]
        return max(simpleRob(nums[1:]), simpleRob(nums[:-1]))


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
