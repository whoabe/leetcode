'''
238. Product of Array Except Self
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

def productExceptSelf(self, nums: List[int]) -> List[int]:
'''


class Solution(object):
    def productExceptSelf(self, nums):
        '''
        approach
            left and right product lists
        '''
        # TC: O(N), SC: O(N)
        # left, right, res = [0]*len(nums), [0]*len(nums), [0]*len(nums)
        # left[0] = 1
        # for i in range(1, len(nums)):
        #     left[i] = left[i-1]*nums[i-1]
        # right[len(nums)-1] = 1
        # for i in reversed(range(len(nums)-1)):
        #     right[i] = right[i+1] * nums[i+1]
        # for i in range(len(nums)):
        #     res[i] = left[i]*right[i]
        # return res

        # constant space if not counting answer array
        res = [1]*len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1]*nums[i-1]
        tmp = 1
        for i in range(len(nums)-2, -1, -1):
            tmp *= nums[i+1]
            res[i] *= tmp
        return res


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))
