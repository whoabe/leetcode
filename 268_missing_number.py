'''
268. Missing Number
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

def missingNumber(self, nums: List[int]) -> int:
'''


class Solution:
    def missingNumber(self, nums):
        '''
        approach:
            n+1 numbers to take but only n numbers in the array
            when XOR operator ^ is used in res ^= i and res ^= num, two same integers would get result of 0 (x^x=0)
            res contains the number which doesnt have a pair which is the missing number
        '''
        res = 0
        for i in range(len(nums)+1):
            res ^= i
        for num in nums:
            res ^= num
        return res


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.missingNumber([3, 0, 1]))
