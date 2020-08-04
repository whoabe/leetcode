'''
377. Combination Sum IV
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
 

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

def combinationSum4(self, nums: List[int], target: int) -> int:
'''

'''
approach:
    dynamic programming
        TC: O(n^2), SC: O(n)
'''


class Solution(object):
    def combinationSum4(self, nums, target):
        dp = [0] * (target+1)
        for i in range(1, target+1):
            for n in nums:
                if n == i:
                    dp[i] += 1
                if n < i:
                    dp[i] += dp[i-n]
        return dp[-1]


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.combinationSum4([1, 2, 3], 4))
