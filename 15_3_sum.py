'''
15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

def threeSum(self, nums: List[int]) -> List[List[int]]:
'''

'''
approach
    2 pointers
        loop through the array and check the sum, and increment and decrement the pointers accordingly
'''


class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length-2):
            if nums[i] > 0:
                break
                # if current value is greater than 0, remaining items cannot sum to 0
            if i > 0 and nums[i] == nums[i-1]:
                continue
                # if current value is the same as the one before it, skip it

            l, r = i+1, length-1
            while l < r:
                total = nums[i]+nums[l]+nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
