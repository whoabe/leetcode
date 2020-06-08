'''
485. Max Consecutive Ones


Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        '''
        approach:
            check if the right counter  = 0
                if it is, then calculate the count and the maxCount and then set the left counter to right +1
                keep incrementing the right counter every iteration of the while loop
        '''
        left, right, count, max_count = 0, 0, 0, 0
        while right < len(nums):
            if nums[right] == 0:
                count = right - left
                max_count = max(count, max_count)
                left = right + 1
            right += 1
        count = right-left
        return max(count, max_count)


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
